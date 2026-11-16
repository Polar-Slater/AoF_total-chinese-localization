"""Check translated event choices against local game XML, without modifying game data."""
import argparse
import contextlib
import io
import json
from pathlib import Path
import runpy
import xml.etree.ElementTree as ET
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--game', type=Path, required=True)
args = parser.parse_args()
with contextlib.redirect_stdout(io.StringIO()):
    build = runpy.run_path(str(ROOT / 'build_translation.py'))
read = build['read_properties']
manifest = json.loads((ROOT / 'translation/shared-coverage.json').read_text(encoding='utf-8'))
conversations = read(ROOT / 'pilot-mod/com/aof/resource/text/i18n/shared-conversations-zh.properties', 'ascii')
shared = read(ROOT / 'pilot-mod/com/aof/resource/text/i18n/shared-zh.properties', 'ascii')
groups = {k.split('.conversations.')[0] for k in conversations if '.conversations.' in k}
references = set()
indexed = {}
conversation_xml = {}
for archive_path in [args.game / 'aof-data.zip', *sorted((args.game / 'data').glob('*.zip'))]:
    with ZipFile(archive_path) as game_archive:
        for name in game_archive.namelist():
            if name.startswith('com/aof/resource/conversation/') and name.endswith('.xml'):
                group = name.rsplit('/', 1)[-1][:-4]
                raw = game_archive.read(name)
                assert group not in conversation_xml or conversation_xml[group] == raw, ('Conflicting conversation XML', group)
                conversation_xml[group] = raw
            if name.startswith('com/aof/resource/campaign/level/shared/') and name.endswith('.xml'):
                tree = ET.fromstring(game_archive.read(name))
                for level in tree.iter('levels'):
                    if 'name' in level.attrib:
                        level_name = level.attrib['name']
                        assert level_name not in indexed, ('Duplicate shared level', level_name)
                        indexed[level_name] = level
shared_source = read(ROOT / 'source/aof-data/shared-en.properties', 'cp1252')
conversation_source = read(ROOT / 'source/aof-data/shared-conversations-en.properties', 'cp1252')
shared_source_groups = {k.split('.conversations.')[0] for k in conversation_source if '.conversations.' in k}
external_conversations = set()
navigation_targets = set()
def check_conversation(group, prefix):
    assert group in conversation_xml, ('Missing conversation XML', prefix, group)
    if group in shared_source_groups:
        assert group in groups, ('Untranslated shared outcome', prefix, group)
    else:
        external_conversations.add(group)

with ZipFile(args.game / 'aof-data.zip') as archive:
    for filename in ('shared-en.properties', 'shared-conversations-en.properties'):
        assert archive.read(f'com/aof/resource/text/i18n/{filename}') == (ROOT / 'source/aof-data' / filename).read_bytes(), ('Stale English reference', filename)
    for group in sorted(groups):
        tree = ET.fromstring(conversation_xml[group])
        for ref in tree.iter('trigger-ref'):
            prefix = f"{ref.attrib['level']}.triggers.{ref.attrib['type']}."
            references.add(prefix)
    assert references == set(manifest['trigger_prefixes']), ('Choice references differ from manifest', references)
    followup_prefixes = manifest['level_prefixes'] + manifest.get('textless_level_prefixes', []) + manifest.get('location_prefixes', [])
    for prefix in followup_prefixes:
        assert prefix.endswith('.') and prefix[:-1] in indexed, ('Unknown follow-up level', prefix)
    for prefix in manifest.get('textless_level_prefixes', []):
        assert not indexed[prefix[:-1]].findall('conversations'), ('Textless level contains dialogue', prefix)
    # Battle victories may queue their outcome for the world map rather than
    # open it from a visible choice (for example, the Beastmaster recruitment).
    followup_conversations = set()
    lifecycle_prefixes = manifest['level_prefixes'] + manifest.get('textless_level_prefixes', [])
    for prefix in lifecycle_prefixes:
        for trigger in indexed[prefix[:-1]].findall('triggers'):
            for command in trigger.findall('commands'):
                words = (command.text or '').strip().split()
                if words and words[0] in ('play-conversation', 'play-conversation-on-world-map'):
                    check_conversation(words[1], prefix)
                    followup_conversations.add(words[1])
    pending = list(references)
    # Story pages, textless shops and battles can advance the quest from
    # on-init/on-exit/on-win triggers without any visible choice.
    lifecycle_triggers = {
        f"{prefix}triggers.{node.attrib['type']}."
        for prefix in lifecycle_prefixes
        for node in indexed[prefix[:-1]].findall('triggers')
    }
    pending.extend(lifecycle_triggers)
    location_choices = set()
    for prefix in manifest.get('location_prefixes', []):
        for node in indexed[prefix[:-1]].findall('triggers'):
            if node.attrib.get('text') or node.attrib.get('description'):
                choice = f"{prefix}triggers.{node.attrib['type']}."
                location_choices.add(choice)
                pending.append(choice)
    checked = set()
    callbacks = set()
    while pending:
        prefix = pending.pop()
        if prefix in checked:
            continue
        checked.add(prefix)
        level_name, _, trigger, _ = prefix.split('.')
        node = next(n for n in indexed[level_name].findall('triggers') if n.attrib['type'] == trigger)
        for field in ('text', 'description'):
            if node.attrib.get(field):
                assert prefix + field in shared, ('Missing referenced choice field', prefix, field)
        for command in node.findall('commands'):
            words = (command.text or '').strip().split()
            if words and words[0] in ('play-conversation', 'play-conversation-on-world-map'):
                check_conversation(words[1], prefix)
            if words and words[0] == 'goto':
                target = words[1]
                if target == '*' or '${' in target:
                    navigation_targets.add(target)
                else:
                    assert target in indexed, ('Missing follow-up level', prefix, target)
                    if target + '.' not in followup_prefixes:
                        assert not any(k.startswith(target + '.') for k in shared_source), ('Untranslated follow-up level', prefix, target)
                        navigation_targets.add(target)
            if words and words[0] == 'goto-random-battle':
                # Optional final argument names the battle's opening conversation.
                assert 3 <= len(words) <= 10, ('Unexpected random-battle arguments', prefix, words)
                if len(words) >= 7 and words[6] != '*':
                    check_conversation(words[6], prefix)
            if words and words[0] in ('select-unit-manual', 'exec-trigger'):
                expected_length = 3 if words[0] == 'select-unit-manual' else 2
                assert len(words) == expected_length, ('Unexpected trigger-reference arguments', prefix, words)
                callback_level, callback_trigger = words[-1].split('/')
                if callback_level == '*':
                    callback_level = level_name
                callback_prefix = f'{callback_level}.triggers.{callback_trigger}.'
                callbacks.add(callback_prefix)
                pending.append(callback_prefix)

# Regression checks for the new shared-resource validation boundaries.
def rejects(call):
    try:
        call()
    except AssertionError:
        return
    raise AssertionError('Invalid localization input was accepted')

validate = build['validate_values']
rejects(lambda: validate({'k': 'You have ${gold} gp'}, {'k': '你有金币'}))
rejects(lambda: validate({'k': 'A=BR=B'}, {'k': '甲乙'}))
rejects(lambda: validate({'k': '{0} {0}'}, {'k': '{0}'}))
rejects(lambda: validate({'k': '<b>A</b>'}, {'k': '<b>甲'}))
namespaces = build['check_runtime_namespaces']
rejects(lambda: namespaces({'bad': {'LOCALE': 'zh', 'CAMPAIGN': 'shared', 'CONVERSATIONS': 'shared'}}))
rejects(lambda: namespaces({'a': {'LOCALE': 'zh', 'CONVERSATIONS': 'shared', 'k': '甲'},
                           'b': {'LOCALE': 'zh', 'CONVERSATIONS': 'other', 'k': '乙'}}))
namespaces({'a': {'LOCALE': 'zh', 'CAMPAIGN': 'shared', 'k': '甲'},
            'b': {'LOCALE': 'zh', 'CAMPAIGN': 'undeadcampaign', 'k': '乙'}})
print(f'PASS: {len(groups)} conversation groups; {len(references)} XML-linked choices and their outcomes covered.')
print(f'PASS: {len(callbacks)} callback/trigger targets followed; {len(followup_prefixes)} follow-up levels verified.')
print(f'PASS: {len(location_choices)} location choices checked; {len(external_conversations)} campaign-resource conversations remain outside shared-resource scope.')
(ROOT / 'inspection/shared-xml-validation.json').write_text(json.dumps({
    'conversation_groups': len(groups), 'conversation_linked_choices': len(references),
    'location_choices': len(location_choices), 'callback_targets': sorted(callbacks),
    'followup_level_conversations': sorted(followup_conversations),
    'followup_level_triggers': sorted(lifecycle_triggers),
    'external_campaign_conversations': sorted(external_conversations),
    'navigation_or_textless_targets': sorted(navigation_targets),
    'in_game_test': 'Not performed for new translations'
}, indent=2) + '\n', encoding='utf-8')
print('PASS: rejects lost variables/format arguments/engine breaks, malformed HTML, invalid metadata and runtime key collisions.')
