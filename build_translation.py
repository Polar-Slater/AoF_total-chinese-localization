"""Validate editable translations and build ASCII Java-properties resources."""
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent

def read_properties(path, encoding='utf-8'):
    result = {}
    for number, line in enumerate(path.read_text(encoding=encoding).splitlines(), 1):
        if not line.strip() or line.lstrip().startswith(('#', '!')):
            continue
        assert '=' in line, (path, number, 'Expected key=value')
        key, value = line.split('=', 1)
        assert key not in result, (path, number, 'Duplicate key', key)
        assert not line.endswith('\\'), (path, number, 'Unexpected continuation')
        result[key] = value
    return result

class MarkupCheck(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
    def handle_starttag(self, tag, attrs):
        if tag not in {'br', 'hr', 'img', 'input', 'meta', 'link'}:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        assert self.stack and self.stack.pop() == tag, ('Unbalanced HTML', tag)

def validate_values(source, translated):
    for key, value in translated.items():
        assert key in source, ('Unknown key', key)
        assert value.strip(), ('Empty value', key)
        tokens = r'\{\d+\}|\$\{[^}]+\}'
        assert Counter(re.findall(tokens, value)) == Counter(re.findall(tokens, source[key])), ('Placeholder mismatch', key)
        assert value.count('=BR=') == source[key].count('=BR='), ('Engine line-break mismatch', key)
        markup = MarkupCheck()
        markup.feed(value)
        assert not markup.stack, ('Unclosed tags', key, markup.stack)

def check_runtime_namespaces(resources):
    """Mirror the engine's campaign prefix and global conversation key spaces."""
    seen = {}
    for name, values in resources.items():
        assert values.get('LOCALE') == 'zh', ('Wrong locale', name)
        markers = [k for k in ('LANGUAGE', 'CAMPAIGN', 'CONVERSATIONS') if values.get(k, '').strip()]
        assert len(markers) == 1, ('Expected one resource type marker', name, markers)
        prefix = values.get('CAMPAIGN', '')
        for key in values.keys() - {'LOCALE', 'CAMPAIGN', 'CONVERSATIONS'}:
            effective = f'{prefix}.{key}' if prefix else key
            assert effective not in seen, ('Runtime key collision', effective, seen.get(effective), name)
            seen[effective] = name

source = read_properties(ROOT / 'source/aof/messages-en.properties', 'cp1252')
merged = read_properties(ROOT / 'translation/messages-zh.properties')
phase = {}
phase1_files = ['ui-phase1.properties', 'settings-tooltips.properties', 'menu-dialogs.properties']
main_text_files = ['gameplay-basics.properties', 'bestiary-basics.properties', 'combat-log-basics.properties']
terminology_files = ['unit-race-terms.properties', 'battlefield-terms.properties']
item_skill_files = ['item-name-terms.properties', 'skill-attribute-terms.properties']
gameplay_description_files = ['gameplay-descriptions.properties']
combat_effect_files = ['combat-tutorials.properties', 'skill-item-effects.properties']
advanced_effect_files = ['skill-item-effects-2.properties']
status_effect_files = ['skill-item-effects-3.properties']
completion_files = ['remaining-interface.properties', 'remaining-gameplay.properties', 'remaining-names.properties', 'remaining-bestiary.properties']
batch_counts = {}
for name in phase1_files + main_text_files + terminology_files + item_skill_files + gameplay_description_files + combat_effect_files + advanced_effect_files + status_effect_files + completion_files:
    part = read_properties(ROOT / 'translation' / name)
    assert not phase.keys() & part.keys(), ('Duplicate batch keys', name, phase.keys() & part.keys())
    phase.update(part)
    batch_counts[name] = len(part)
merged.update(phase)
validate_values(source, merged)

lines = (ROOT / 'source/aof/messages-en.properties').read_text(encoding='cp1252').splitlines()
settings = {line.split('=', 1)[0] for line in lines[1130:1523] if '=' in line and not line.startswith('#')}
buttons = {line.split('=', 1)[0] for line in lines[296:565] if '=' in line and not line.startswith('#')}
assert not settings - merged.keys(), ('Untranslated settings', settings - merged.keys())
assert not buttons - merged.keys(), ('Untranslated buttons', buttons - merged.keys())
object_names = {key for key in source if key.startswith('game.object.') and key.endswith('.name')}
race_keys = list(source)[list(source).index('DRAGONS'):list(source).index('GIANTS') + 1]
assert not object_names - merged.keys(), ('Untranslated object names', object_names - merged.keys())
assert not set(race_keys) - merged.keys(), ('Untranslated race/group labels', set(race_keys) - merged.keys())
source_order = list(source)
label_keys = set(source_order[source_order.index('ACIDBLOOD'):source_order.index('ANCIENTCOAL_ITEM') + 1])
material_keys = set(source_order[source_order.index('LIVERWORM_ITEM'):source_order.index('WHITEYARROW_ITEM') + 1])
crafting_keys = set(source_order[source_order.index('CRAFTINGBLACKSMITH'):source_order.index('CRAFTINGJEWELER') + 1])
item_name_keys = {key for key in label_keys | material_keys if key.endswith('_ITEM')}
item_set_keys = {key for key in source if key.startswith('GROUP_SET_')}
assert not (label_keys | material_keys | crafting_keys | item_set_keys) - merged.keys(), ('Untranslated terminology', (label_keys | material_keys | crafting_keys | item_set_keys) - merged.keys())
tutorial_keys = {key for key in source if key.startswith(('BATTLE_TUTORIAL_', 'WORLDMAP_TUTORIAL_'))}
assert not tutorial_keys - merged.keys(), ('Untranslated battle/world-map tutorial pages', tutorial_keys - merged.keys())
assert source.keys() == merged.keys(), ('Incomplete main messages', source.keys() - merged.keys(), merged.keys() - source.keys())
object_descriptions = {key for key in source if key.startswith('game.object.') and key.endswith('.description')}

out = ROOT / 'pilot-mod/com/aof/resource/text/i18n/messages-zh.properties'
text = '# Generated by build_translation.py; edit translation/*.properties instead.\n'
text += ''.join(f'{key}={merged[key]}\n' for key in source if key in merged)
# Encode non-ASCII as UTF-16 code-unit escapes, as required by Java Properties.
def escape(text):
    encoded = text.encode('utf-16-be')
    return ''.join(chr(code) if code < 128 else f'\\u{code:04x}' for code in [int.from_bytes(encoded[i:i+2], 'big') for i in range(0, len(encoded), 2)])
runtime_outputs = {out: text}
runtime_values = {out.name: merged}
shared_coverage = json.loads((ROOT / 'translation/shared-coverage.json').read_text(encoding='utf-8'))
for category, entries in shared_coverage.items():
    assert entries and len(entries) == len(set(entries)), ('Empty or duplicate coverage declarations', category)
shared_report = {}
for stem, marker, files in [
    ('shared', 'CAMPAIGN', ['shared-events-1.properties', 'shared-events-2.properties', 'shared-events-3.properties', 'shared-events-4.properties', 'shared-events-5.properties', 'shared-bases-6.properties', 'shared-systems-7.properties', 'shared-events-8.properties', 'shared-events-9.properties', 'shared-events-10.properties', 'shared-events-11.properties', 'shared-events-12.properties', 'shared-events-13.properties', 'shared-events-14.properties', 'shared-events-15.properties', 'shared-events-16.properties', 'shared-events-17.properties', 'shared-events-18.properties', 'shared-events-19.properties', 'shared-events-20.properties', 'shared-events-21.properties', 'shared-events-22.properties', 'shared-events-23.properties', 'shared-events-24.properties', 'shared-events-25.properties', 'shared-events-26.properties', 'shared-events-27.properties', 'shared-events-28.properties', 'shared-events-29.properties', 'shared-events-30.properties', 'shared-events-31.properties']),
    ('shared-conversations', 'CONVERSATIONS', ['shared-conversations-1.properties', 'shared-conversations-2.properties', 'shared-conversations-3.properties', 'shared-conversations-4.properties', 'shared-conversations-5.properties', 'shared-conversations-7.properties', 'shared-conversations-8.properties', 'shared-conversations-9.properties', 'shared-conversations-10.properties', 'shared-conversations-11.properties', 'shared-conversations-12.properties', 'shared-conversations-13.properties', 'shared-conversations-14.properties', 'shared-conversations-15.properties', 'shared-conversations-16.properties', 'shared-conversations-17.properties', 'shared-conversations-18.properties', 'shared-conversations-19.properties', 'shared-conversations-20.properties', 'shared-conversations-21.properties']),
]:
    reference = read_properties(ROOT / f'source/aof-data/{stem}-en.properties', 'cp1252')
    translated = {marker: 'shared', 'LOCALE': 'zh'}
    for filename in files:
        part = read_properties(ROOT / 'translation' / filename)
        assert not part.keys() & translated.keys(), ('Duplicate shared keys', filename)
        translated.update(part)
    validate_values(reference, translated)
    assert reference.keys() == translated.keys(), ('Incomplete shared resource', stem, reference.keys() - translated.keys(), translated.keys() - reference.keys())
    if stem == 'shared-conversations':
        for family in shared_coverage['event_families']:
            assert any(k.startswith(family + '.') or k.startswith(family + '_') for k in reference), ('Unknown event family', family)
        expected = {k for k in reference if any(k.startswith(f + '.') or k.startswith(f + '_') for f in shared_coverage['event_families'])}
    else:
        prefixes = shared_coverage['trigger_prefixes'] + shared_coverage['level_prefixes'] + shared_coverage.get('location_prefixes', [])
        for prefix in prefixes:
            assert any(k.startswith(prefix) for k in reference), ('Unknown shared coverage prefix', prefix)
        for prefix in shared_coverage.get('textless_level_prefixes', []):
            assert prefix not in prefixes, ('Duplicate textless level declaration', prefix)
            assert not any(k.startswith(prefix) for k in reference), ('Textless level has source text', prefix)
        expected = {k for k in reference if any(k.startswith(p) for p in prefixes)}
    actual = translated.keys() - {marker, 'LOCALE'}
    assert actual == expected, ('Shared event coverage mismatch', stem, expected - actual, actual - expected)
    global_prefix = 'SGE_' if stem == 'shared-conversations' else 'LevelGlobalEvent'
    global_event_keys = {k for k in reference if k.startswith(global_prefix)}
    assert global_event_keys <= actual, ('Incomplete global-event milestone', stem, global_event_keys - actual)
    target = out.with_name(f'{stem}-zh.properties')
    runtime_outputs[target] = '# Generated by build_translation.py; edit translation/*.properties instead.\n' + ''.join(
        f'{k}={translated[k]}\n' for k in reference if k in translated)
    runtime_values[target.name] = translated
    shared_report[stem] = {'translated_content_entries': len(actual),
                           'global_event_content_entries_covered': len(global_event_keys),
                           'source_content_entries': len(reference) - 2,
                           'untranslated_content_entries': len(reference.keys() - translated.keys()),
                           'complete_conversation_groups': len({k.split('.conversations.')[0] for k in actual if '.conversations.' in k})}

campaign_report = {}
campaign_coverage = json.loads((ROOT / 'translation/campaign-coverage.json').read_text(encoding='utf-8'))
for campaign, scope in campaign_coverage.items():
    for suffix, marker, groups in [('', 'CAMPAIGN', scope['levels']),
                                    ('-conversations', 'CONVERSATIONS', scope['conversation_families'])]:
        stem = campaign + suffix
        reference = read_properties(ROOT / f"source/{scope['source_directory']}/{stem}-en.properties", 'cp1252')
        translated = read_properties(ROOT / f'translation/{stem}-zh.properties')
        assert translated.get(marker) == campaign and translated.get('LOCALE') == 'zh', ('Campaign metadata', stem)
        assert groups and len(groups) == len(set(groups)), ('Duplicate or empty campaign scope', stem)
        expected = {marker, 'LOCALE'} | ({'title', 'description'} if not suffix else set())
        for group in groups:
            keys = {k for k in reference if k.startswith(group + '.')}
            assert keys, ('Unknown campaign group', stem, group)
            expected.update(keys)
        assert translated.keys() == expected, ('Campaign coverage mismatch', stem, expected - translated.keys(), translated.keys() - expected)
        validate_values(reference, translated)
        target = out.with_name(f'{stem}-zh.properties')
        runtime_outputs[target] = '# Generated by build_translation.py; edit translation/*.properties instead.\n' + ''.join(
            f'{k}={translated[k]}\n' for k in reference if k in translated)
        runtime_values[target.name] = translated
        campaign_report[stem] = {'translated_content_entries': len(translated) - 2,
                                 'source_content_entries': len(reference) - 2,
                                 'untranslated_content_entries': len(reference.keys() - translated.keys()),
                                 'complete_groups': groups}

for existing in out.parent.glob('*.properties'):
    if existing.name not in runtime_values:
        runtime_values[existing.name] = read_properties(existing, 'ascii')
check_runtime_namespaces(runtime_values)
for target, content in runtime_outputs.items():
    target.write_text(escape(content), encoding='ascii', newline='\n')
(ROOT / 'inspection/campaign-validation.json').write_text(json.dumps(campaign_report, indent=2), encoding='utf-8', newline='\n')
shared_report['selected_event_families'] = shared_coverage['event_families']
shared_report['total_translated_content_entries'] = sum(shared_report[s]['translated_content_entries'] for s in ('shared', 'shared-conversations'))
shared_report['total_source_content_entries'] = sum(shared_report[s]['source_content_entries'] for s in ('shared', 'shared-conversations'))
shared_report['total_runtime_entries_all_files'] = sum(map(len, runtime_values.values()))
shared_report['checks'] = ['complete shared events and shared conversations', 'complete selected event families and declared choices', 'placeholder multiplicities', 'engine =BR= markers', 'balanced HTML', 'locale/type markers', 'no effective runtime key collisions', 'ASCII Java properties']
shared_report['in_game_layout'] = 'Pending user test'
(ROOT / 'inspection/shared-validation.json').write_text(json.dumps(shared_report, indent=2), encoding='utf-8', newline='\n')
report = {'phase1_entries': sum(batch_counts[name] for name in phase1_files),
          'main_text_batch1_entries': sum(batch_counts[name] for name in main_text_files),
          'terminology_batch2_entries': sum(batch_counts[name] for name in terminology_files),
          'terminology_batch3_entries': sum(batch_counts[name] for name in item_skill_files),
          'gameplay_descriptions_batch4_entries': sum(batch_counts[name] for name in gameplay_description_files),
          'combat_tutorials_effects_batch5_entries': sum(batch_counts[name] for name in combat_effect_files),
          'advanced_effects_batch6_entries': sum(batch_counts[name] for name in advanced_effect_files),
          'status_effects_batch7_entries': sum(batch_counts[name] for name in status_effect_files),
          'main_completion_batch8_entries': sum(batch_counts[name] for name in completion_files),
          'batch_entries': batch_counts,
          'source_main_entries_including_metadata': len(source),
          'total_ui_entries_including_metadata': len(merged),
          'untranslated_main_entries': len(source.keys() - merged.keys()),
          'object_name_keys_covered': len(object_names), 'race_group_keys_covered': len(race_keys),
          'object_description_keys_covered': len(object_descriptions),
          'item_resource_name_template_keys_covered': len(item_name_keys),
          'main_attribute_skill_condition_label_keys_covered': len(label_keys - item_name_keys),
          'crafting_profession_keys_covered': len(crafting_keys),
          'item_set_label_keys_covered': len(item_set_keys),
          'battle_worldmap_tutorial_keys_covered': len(tutorial_keys),
          'button_and_tab_keys_covered': len(buttons), 'settings_section_keys_covered': len(settings),
          'checks': ['unique keys', 'English-source key existence', 'placeholder counts', 'balanced HTML', 'complete button/tab and settings section coverage', 'complete object-name and race/group coverage', 'complete main label, crafting material and profession blocks', 'complete battle/world-map tutorial prefix coverage', 'complete main messages and object descriptions', 'ASCII runtime encoding'],
          'in_game_layout': 'Pending user test',
          'known_source_issues': ['Proxy username/password labels swapped in English source; preserved pending UI review.', 'AI animation label and tooltip disagree in English source; preserved pending behavior review.']}
(ROOT / 'inspection/phase1-validation.json').write_text(json.dumps(report, indent=2), encoding='utf-8', newline='\n')
print(json.dumps(report, indent=2))
print(json.dumps(shared_report, indent=2))
