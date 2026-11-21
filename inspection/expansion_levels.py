"""Select current expansion level references and compare them with the level XML."""
import html
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile


def normalize(value):
    return ''.join(html.unescape(re.sub(r'<[^>]+>', ' ', value)).split())


def read_simple(path):
    return dict(line.split('=', 1) for line in path.read_text(encoding='cp1252').splitlines()
                if line and not line.startswith('#') and '=' in line)


def level_values(xml, original, marker):
    result = {'CAMPAIGN': marker, 'LOCALE': 'en'}

    def add(key, value, block=False):
        if not value or not value.strip():
            return
        if key in original and normalize(original[key]) == normalize(value):
            result[key] = original[key]
            return
        lines = [line.strip() for line in value.strip().splitlines()]
        # Match the game's text-resource convention: explicit source lines become HTML breaks.
        value = '<br>'.join(lines)
        result[key] = '<html><body>' + value + '</body></html>' if block or len(lines) > 1 else value

    for level in ET.fromstring(xml).iter('levels'):
        name = level.get('name')
        if not name:
            continue
        for field in ('text', 'selection-text'):
            add(name + '.' + field, level.findtext(field), True)
        add(name + '.location.name', level.findtext('location/name'))
        for i, conversation in enumerate(level.findall('conversations')):
            for field in ('name', 'text', 'selection-text'):
                add(f'{name}.conversations.{i}.{field}', conversation.findtext(field))
        for trigger in level.findall('triggers'):
            for field in ('text', 'description'):
                add(f"{name}.triggers.{trigger.get('type')}.{field}", trigger.get(field))
    return result


def extract_current_levels(game, root):
    directory = root / 'source/aof4-zombiefranky-dlc'
    with ZipFile(game / 'data/aof4-zombiefranky-dlc.zip') as archive:
        xml = archive.read('com/aof/resource/campaign/level/vampirehuntercampaign/zombiefrankydlc.xml')
        original = read_simple(directory / 'zombiefrankydlc-en.properties')
        derived = level_values(xml, original, 'vampirehuntercampaign')
    # The enclosing campaign contains the current text; keep archive precedence explicit.
    canonical = read_simple(root / 'source/aof4-vampirehunter/vampirehuntercampaign-en.properties')
    values = {k: v for k, v in canonical.items() if k in ('CAMPAIGN', 'LOCALE') or k.startswith('LevelZombieFranky')}
    assert values == derived, 'Current campaign properties and expansion XML differ; review before translating.'
    target = directory / 'current/zombiefrankydlc-en.properties'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(''.join(f'{key}={value}\n' for key, value in values.items()), encoding='cp1252')
    extract_storm_levels(game, root)
    extract_quick_levels(game, root)
    extract_machine_levels(game, root)
    return values


def extract_storm_levels(game, root):
    directory = root / 'source/aof4-newseapeople-dlc'
    canonical = read_simple(root / 'source/aof4-vampirehunter/vampirehuntercampaign-en.properties')
    values = {k: v for k, v in canonical.items() if k in ('CAMPAIGN', 'LOCALE') or k.startswith('LevelNewSeaPeople')}
    with ZipFile(game / 'data/aof4-newseapeople-dlc.zip') as archive:
        xml = archive.read('com/aof/resource/campaign/level/vampirehuntercampaign/newseapeopledlc.xml')
    derived = level_values(xml, values, 'vampirehuntercampaign')
    excluded = storm_internal_fields()
    assert derived.keys() - values.keys() == excluded.keys()
    assert {k: v for k, v in derived.items() if k not in excluded} == values
    target = directory / 'current/newseapeopledlc-en.properties'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(''.join(f'{key}={value}\n' for key, value in values.items()), encoding='cp1252')
    return values


def storm_internal_fields():
    return {
        'LevelNewSeaPeopleTriggerClose.location.name': 'Hidden control-level label, absent from the canonical English resource.',
        **{f'LevelNewSeaPeople{i:02d}.text': 'Battle setup summary, absent from the canonical English resource.'
           for i in (4, 9, 12, 15, 18, 22, 24, 26)}
    }


def quick_internal_fields():
    return {
        'LevelQuickFemaleAssassinTriggerClose.location.name': 'Hidden control-level label, absent from the canonical English resource.',
        **{f'LevelQuickFemaleAssassin{i:02d}.text': 'Battle setup summary, absent from the canonical English resource.'
           for i in (3, 7, 10, 14, 18)}
    }


def extract_quick_levels(game, root):
    directory = root / 'source/aof5-quickfemaleassassin-dlc'
    canonical = read_simple(root / 'source/aof5-ratmen/ratmencampaign-en.properties')
    values = {k: v for k, v in canonical.items() if k in ('CAMPAIGN', 'LOCALE') or k.startswith('LevelQuickFemaleAssassin')}
    with ZipFile(game / 'data/aof5-quickfemaleassassin-dlc.zip') as archive:
        xml = archive.read('com/aof/resource/campaign/level/ratmencampaign/quickfemaleassassindlc.xml')
    derived = level_values(xml, values, 'ratmencampaign')
    excluded = quick_internal_fields()
    assert derived.keys() - values.keys() == excluded.keys()
    assert {k: v for k, v in derived.items() if k not in excluded} == values
    target = directory / 'current/quickfemaleassassindlc-en.properties'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(''.join(f'{key}={value}\n' for key, value in values.items()), encoding='cp1252')
    return values


def machine_internal_fields():
    return {
        'LevelMachineWarTriggerClose.location.name': 'Hidden control-level label, absent from the canonical English resource.',
        **{f'LevelMachineWar{suffix}.text': 'Battle setup summary, absent from the canonical English resource.'
           for suffix in ('03', 'BrinWorkshop02', 'DragonSkull02', 'MechanicalDragon02')}
    }


def extract_machine_levels(game, root):
    directory = root / 'source/aof5-machinewar-dlc'
    canonical = read_simple(root / 'source/aof5-ratmen/ratmencampaign-en.properties')
    values = {k: v for k, v in canonical.items() if k in ('CAMPAIGN', 'LOCALE') or k.startswith('LevelMachineWar')}
    with ZipFile(game / 'data/aof5-machinewar-dlc.zip') as archive:
        xml = archive.read('com/aof/resource/campaign/level/ratmencampaign/machinewardlc.xml')
    derived = level_values(xml, values, 'ratmencampaign')
    excluded = machine_internal_fields()
    assert derived.keys() - values.keys() == excluded.keys()
    assert {k: v for k, v in derived.items() if k not in excluded} == values
    target = directory / 'current/machinewardlc-en.properties'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(''.join(f'{key}={value}\n' for key, value in values.items()), encoding='cp1252')
    return values
