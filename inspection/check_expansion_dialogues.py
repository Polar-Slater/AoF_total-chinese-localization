"""Validate declared expansion dialogue groups and their XML-linked choices."""
import argparse
import contextlib
import html
import io
import json
from pathlib import Path
import re
import runpy
import xml.etree.ElementTree as ET
import zlib
from zipfile import ZipFile
from expansion_levels import level_values, read_simple

ROOT = Path(__file__).resolve().parents[1]


def normalize(value):
    return ''.join(html.unescape(re.sub(r'<[^>]+>', ' ', value)).split())


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', type=Path, required=True)
    args = parser.parse_args()
    with contextlib.redirect_stdout(io.StringIO()):
        build = runpy.run_path(str(ROOT / 'build_translation.py'))
    read = build['read_properties']
    scopes = json.loads((ROOT / 'translation/expansion-coverage.json').read_text(encoding='utf-8'))
    shared = build['runtime_values']['shared-zh.properties']
    shared_source = read(ROOT / 'source/aof-data/shared-en.properties', 'cp1252')
    reports = {}
    for expansion, scope in scopes.items():
        groups = set(scope['conversation_families'])
        stem = expansion + '-conversations'
        source_path = ROOT / 'source' / scope['source_directory'] / (stem + '-en.properties')
        source = read(source_path, 'cp1252')
        translated = read(ROOT / 'translation' / (stem + '-zh.properties'))
        choice_values, choice_source = shared, shared_source
        if scope.get('level_reference'):
            choice_values = build['runtime_values'][expansion + '-zh.properties']
            choice_source = read(ROOT / 'source' / scope['source_directory'] / scope['level_reference'], 'cp1252')
        external = scope.get('external_dialogue_archives', {})
        source_only = scope.get('source_only_groups', {})
        unlinked = scope.get('unlinked_groups', {})
        assert set(unlinked) <= groups and all(unlinked.values())
        assert set(external) <= groups and set(source_only) <= groups
        assert not (external.keys() & source_only.keys())
        refs, images, expected = [], [], {'CONVERSATIONS', 'LOCALE'}
        with ZipFile(args.game / 'data' / (scope['source_directory'] + '.zip')) as archive:
            assert archive.read('com/aof/resource/text/i18n/' + stem + '-en.properties') == source_path.read_bytes(), ('Stale reference', stem)
            campaign_xml = archive.read(scope.get('campaign_xml', 'com/aof/resource/campaign/level/shared/' + expansion + '.xml'))
            campaign = ET.fromstring(campaign_xml)
            level_report = None
            if scope.get('level_reference'):
                original_path = ROOT / 'source' / scope['source_directory'] / (expansion + '-en.properties')
                assert archive.read('com/aof/resource/text/i18n/' + expansion + '-en.properties') == original_path.read_bytes()
                original = read_simple(original_path)
                # A canonical campaign reference may preserve different paragraph breaks.
                formatting_reference = choice_source if scope.get('excluded_xml_fields') else original
                current = level_values(campaign_xml, formatting_reference, scope['campaign_marker'])
                excluded_fields = scope.get('excluded_xml_fields', {})
                assert set(excluded_fields) <= current.keys() and all(excluded_fields.values())
                current = {k: v for k, v in current.items() if k not in excluded_fields}
                assert current == choice_source, ('Stale derived level reference', expansion)
                if scope.get('canonical_level_source'):
                    canonical_path = ROOT / 'source' / scope['canonical_level_source']
                    with ZipFile(args.game / 'data' / (canonical_path.parent.name + '.zip')) as canonical_archive:
                        assert canonical_archive.read('com/aof/resource/text/i18n/' + canonical_path.name) == canonical_path.read_bytes()
                    canonical = read_simple(canonical_path)
                    assert {k: canonical[k] for k in current} == current, ('Campaign source mismatch', expansion)
                assert choice_values.keys() == current.keys(), ('Current level fields missing', expansion)
                level_report = {'xml_content_entries': len(current) - 2,
                                'excluded_xml_fields': excluded_fields,
                                'added_keys_vs_bundled_properties': sorted(current.keys() - original.keys()),
                                'retired_keys_vs_bundled_properties': sorted(original.keys() - current.keys()),
                                'changed_keys_vs_bundled_properties': sorted(k for k in current.keys() & original.keys() if current[k] != original[k])}
            levels = {n.attrib['name']: n for n in campaign.iter('levels') if 'name' in n.attrib}
            level_choices = []
            for choice, reviewed in scope.get('reviewed_level_choices', {}).items():
                level, trigger = choice.split('.', 1)
                node = next(n for n in levels[level].findall('triggers') if n.get('type') == trigger)
                commands = [(n.text or '').strip() for n in node.findall('commands')]
                assert commands == reviewed, ('Level choice commands changed', choice)
                for field in ('text', 'description'):
                    key = f'{level}.triggers.{trigger}.{field}'
                    if node.get(field):
                        assert key in choice_values and normalize(node.get(field)) == normalize(choice_source[key])
                outcomes = []
                for command in commands:
                    words = command.split()
                    if words[0] == 'goto':
                        target = level if words[1] == '*' else words[1]
                        keys = {k for k in choice_source if k.startswith(target + '.')}
                        if not keys:
                            reviewed_exit = scope.get('textless_choice_outcomes', {}).get(target)
                            assert reviewed_exit, ('Unreviewed textless choice outcome', target)
                            exit_commands = [(c.text or '').strip() for c in levels[target].findall("triggers[@type='on-exit']/commands")]
                            assert exit_commands == reviewed_exit, ('Textless choice exit changed', target)
                            for exit_command in exit_commands:
                                follow = exit_command.split()
                                assert follow[0] == 'goto', ('Review textless choice command', exit_command)
                                next_keys = {k for k in choice_source if k.startswith(follow[1] + '.')}
                                assert next_keys and next_keys <= choice_values.keys(), ('Missing textless choice continuation', follow[1])
                        else:
                            assert keys <= choice_values.keys(), ('Missing level choice outcome', target)
                        outcomes.append(target)
                level_choices.append({'choice': choice, 'commands': commands, 'outcomes': outcomes})
            if scope.get('reviewed_level_choices'):
                actual = {f'{name}.{t.get("type")}' for name, level in levels.items()
                          for t in level.findall('triggers') if t.get('type', '').startswith('on-select-')}
                assert actual == scope['reviewed_level_choices'].keys(), ('Unreviewed level choices', expansion)
            for group in sorted(groups):
                dialogue_path = 'com/aof/resource/conversation/' + group + '.xml'
                if group in source_only:
                    assert source_only[group], ('Missing source-only explanation', group)
                    expected.update(k for k in source if k.startswith(group + '.'))
                    continue
                if group in external:
                    with ZipFile(args.game / external[group]) as external_archive:
                        raw = external_archive.read(dialogue_path)
                else:
                    raw = archive.read(dialogue_path)
                root = ET.fromstring(raw)
                for i, node in enumerate(root.findall('conversations')):
                    has_text = False
                    for field in ('name', 'text', 'selection-text'):
                        child = node.find(field)
                        if child is not None and (child.text or '').strip():
                            key = f'{group}.conversations.{i}.{field}'
                            expected.add(key)
                            assert key in source and key in translated, ('Missing XML dialogue field', key)
                            assert normalize(child.text) == normalize(source[key]), ('XML/reference text differs', key)
                            has_text = True
                    if not has_text:
                        images.append(f'{group}.conversations.{i}')
                        assert node.find('event-file-name') is not None, ('Unexplained empty dialogue', group, i)
                # A new command-bearing dialogue must be explicitly reviewed before adding it.
                assert not list(root.iter('commands')), ('Review dialogue commands', group)
                for ref in root.iter('trigger-ref'):
                    level, trigger = ref.attrib['level'], ref.attrib['type']
                    node = next(n for n in levels[level].findall('triggers') if n.attrib['type'] == trigger)
                    prefix = f'{level}.triggers.{trigger}.'
                    for field in ('text', 'description'):
                        if node.attrib.get(field):
                            assert prefix + field in choice_values
                            assert normalize(node.attrib[field]) == normalize(choice_source[prefix + field])
                    commands = [(n.text or '').strip() for n in node.findall('commands')]
                    reviewed = scope.get('reviewed_choice_commands', {}).get(f'{level}.{trigger}')
                    if reviewed is not None:
                        assert commands == reviewed, ('Reviewed choice commands changed', level, trigger)
                    outcomes = []
                    for command in commands:
                        words = command.split()
                        if reviewed is not None and words[0] != 'goto':
                            continue
                        assert words[0] == 'goto', ('Review choice command', command)
                        target = words[1]
                        outcome_keys = {k for k in choice_source if k.startswith(target + '.')}
                        assert outcome_keys and outcome_keys <= choice_values.keys(), ('Missing outcome translation', target)
                        outcomes.append({'level': target, 'content_entries': len(outcome_keys),
                                         'exit_commands': [(n.text or '').strip() for n in levels[target].findall("triggers[@type='on-exit']/commands")]})
                    refs.append({'group': group, 'trigger': prefix, 'commands': commands, 'outcomes': outcomes})
            assert translated.keys() == expected, ('XML/source coverage mismatch', stem)
            calls = []
            for level, node in levels.items():
                for trigger in node.findall('triggers'):
                    for command in trigger.findall('commands'):
                        words = (command.text or '').split()
                        if words and words[0] in ('play-conversation', 'play-conversation-on-world-map') and words[1] in groups:
                            calls.append({'level': level, 'trigger': trigger.attrib['type'], 'group': words[1],
                                          'condition': command.attrib.get('condition', trigger.attrib.get('condition', ''))})
            board_refs = []
            for board, board_groups in scope.get('board_conversations', {}).items():
                assert set(board_groups) <= groups, ('Undeclared board groups', board)
                packed = archive.read('com/aof/resource/board/' + board + '.brd')
                assert packed.startswith(b'BAT-ZIP-'), ('Unknown board encoding', board)
                raw = zlib.decompress(packed[8:])
                assert raw.startswith(b'\xac\xed\x00\x05'), ('Unknown board stream', board)
                for group in board_groups:
                    encoded = group.encode('ascii')
                    # Check the exact serialized Java string, without executing/deserializing game objects.
                    marker = b'\x74' + len(encoded).to_bytes(2, 'big') + encoded
                    assert marker in raw, ('Missing board dialogue reference', board, group)
                    board_refs.append({'board': board, 'group': group})
            linked = {c['group'] for c in calls} | {c['group'] for c in board_refs}
            # Core-game return greetings are defined outside this expansion's campaign/boards.
            assert not set(unlinked) & linked, ('Previously unlinked group is now linked', expansion)
            assert linked | set(external) | set(source_only) | set(unlinked) == groups, ('Unlinked expansion groups', groups - linked - set(external) - set(source_only) - set(unlinked))
        remaining = sorted(source.keys() - translated.keys())
        reports[stem] = {'complete_groups': sorted(groups), 'translated_content_entries': len(translated) - 2,
                         'source_content_entries': len(source) - 2, 'remaining_content_entries': len(remaining),
                         'remaining_groups': sorted({k.split('.')[0] for k in remaining}),
                         'image_only_indices_preserved': images, 'choice_references': refs,
                         'level_choices': level_choices,
                         'campaign_calls': calls, 'board_string_references': board_refs,
                         'board_check_scope': 'Serialized dialogue names only; runtime trigger behavior not tested.',
                         'external_dialogue_archives': external,
                         'source_only_groups': source_only,
                         'unlinked_groups': unlinked,
                         'xml_checked_groups': len(groups) - len(source_only),
                         'xml_checked_content_entries': len(translated) - 2 - sum(k.split('.')[0] in source_only for k in translated),
                         'level_resource': level_report,
                         'in_game_test': False}
        print(f'PASS: {stem}: {len(groups)} groups, {len(translated)-2} content entries, {len(groups)-len(source_only)} XML-checked groups, {len(source_only)} source-only groups, {len(refs)} choices, {len(images)} image-only entries preserved.')
    (ROOT / 'inspection/expansion-xml-validation.json').write_text(json.dumps(reports, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
