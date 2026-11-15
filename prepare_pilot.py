from pathlib import Path
import hashlib
import json
import re
import shutil
import zipfile

ROOT = Path(__file__).resolve().parent
GAME = Path(r'D:\Software\Steam\steamapps\common\AOFTOTAL')
RESOURCE = 'com/aof/resource/text/i18n/'
manifest = []
for archive in [GAME / 'aof.jar', GAME / 'aof-data.zip', *sorted((GAME / 'data').glob('*.zip'))]:
    with zipfile.ZipFile(archive) as z:
        for name in z.namelist():
            if name.startswith(RESOURCE) and name.endswith('.properties'):
                data = z.read(name)
                destination = ROOT / 'source' / archive.stem / Path(name).name
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(data)
                manifest.append({'archive': str(archive), 'entry': name, 'file': str(destination.relative_to(ROOT)), 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
(ROOT / 'source' / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')

ui = {
    'LOCALE': 'zh', 'LANGUAGE': 'Chinese (Simplified) - Test',
    **{key: 'simhei.ttf' for key in ['INTROTEXT_FONT', 'BUTTONTEXT_FONT', 'EFFECTTEXT_FONT', 'DEFAULTTEXT_FONT']},
    'OK_OPTION_ALSO_ESCAPE_KEY': '确定', 'CANCEL_OPTION_ALSO_ESCAPE_KEY': '取消',
    'EXIT_OPTION_ALSO_ESCAPE_KEY': '退出', 'YES_OPTION': '是', 'NO_OPTION_ALSO_ESCAPE_KEY': '否',
    'CONFIRM_OPTION': '确认', 'BACK_OPTION': '返回', 'CONTINUE_OPTION': '继续',
    'NEWCAMPAIGN_OPTION': '新战役', 'LOAD_GAME_OPTION': '读取游戏', 'LOAD_OPTION': '读取',
    'SAVE_OPTION': '保存', 'SAVEGAME_OPTION': '保存游戏', 'OPTIONS_OPTION': '选项',
    'SETUP_OPTION': '设置', 'NEW_OPTION': '新建', 'HELP_OPTION': '帮助',
    'MENU_OPTION': '菜单', 'BESTIARY_OPTION': '生物图鉴', 'EXTRAS_OPTION': '额外内容',
    'CREDITS_OPTION': '制作人员', 'START_OPTION': '开始', 'ENDTURN_OPTION': '结束回合',
    'TAB_SOUND': '声音', 'TAB_SCREEN': '画面', 'TAB_CONTROLS': '操作', 'TAB_MISC': '其他',
    'TAB_INFO': '信息', 'TAB_SAVES': '存档',
    'game.object.vaseempty.name': '空花瓶',
    'game.object.vaseempty.description': '一个装饰花瓶，正等着有人插上几朵鲜花。',
}
campaign = {
    'LOCALE': 'zh', 'CAMPAIGN': 'undeadcampaign', 'title': '死灵法师的崛起',
    'description': '<html><body>第一章<br>这是一个死灵法师学徒的故事。<br>克里尔将穿越遥远的土地，<br>最终直面自己的命运。</body></html>',
    'Level00.conversations.0.name': '克里尔', 'Level00.conversations.0.text': '别来烦我！',
}
dialogue = {
    'LOCALE': 'zh', 'CONVERSATIONS': 'undeadcampaign',
    'U00_Krill_turn.conversations.0.name': '克里尔',
    'U00_Krill_turn.conversations.0.text': '别来烦我！',
    'U01_Goblin_panic.conversations.0.name': '地精',
    'U01_Goblin_panic.conversations.0.text': '快跑！快跑！',
    'U01_Goblin_panic.conversations.1.name': '克里尔',
    'U01_Goblin_panic.conversations.1.text': '<html><body>陪我玩玩如何？<br>哈哈哈！</body></html>',
}
for filename, values, original in [
    ('messages-zh.properties', ui, ROOT / 'source/aof/messages-en.properties'),
    ('undeadcampaign-zh.properties', campaign, ROOT / 'source/aof-undead/undeadcampaign-en.properties'),
    ('undeadcampaign-conversations-zh.properties', dialogue, ROOT / 'source/aof-undead/undeadcampaign-conversations-en.properties'),
]:
    original_keys = {line.split('=', 1)[0] for line in original.read_text(encoding='cp1252').splitlines() if '=' in line and not line.startswith('#')}
    assert set(values) <= original_keys, set(values) - original_keys
    text = '# Simplified Chinese local pilot; untranslated keys fall back to English.\n'
    text += ''.join(f'{key}={value}\n' for key, value in values.items())
    editable = ROOT / 'translation' / filename
    editable.parent.mkdir(parents=True, exist_ok=True)
    if not editable.exists():
        editable.write_text(text, encoding='utf-8')
    text = editable.read_text(encoding='utf-8')
    escaped = ''.join(c if ord(c) < 128 else '\\u%04x' % ord(c) for c in text)
    output = ROOT / 'pilot-mod' / RESOURCE / filename
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(escaped, encoding='ascii')
font = ROOT / 'pilot-mod/com/aof/resource/text/font/simhei.ttf'
font.parent.mkdir(parents=True, exist_ok=True)
shutil.copyfile('C:/Windows/Fonts/simhei.ttf', font)
home = ROOT / 'pilot-home'
home.mkdir(exist_ok=True)
config = home / 'config.properties'
if not config.exists():
    config.write_text('resource.lookup.folder=' + (ROOT / 'pilot-mod').as_posix().replace('/', '//') + '//\nresource.lookup.order=folder,workshop,jar\n', encoding='ascii')
launcher = (GAME / 'aof-total-start-windows.bat').read_text(encoding='ascii')
launcher = re.sub(r'%~dp0', lambda _: str(GAME) + '\\', launcher, flags=re.IGNORECASE)
launcher = launcher.replace('com.aof.Game %ARGUMENTS%', '"-Dgame.home=%~dp0pilot-home" com.aof.Game %ARGUMENTS%')
launcher = launcher.replace('@echo off', '@echo off\nsetlocal\ncd /d "' + str(GAME) + '"', 1)
(ROOT / 'launch-chinese-test.bat').write_text(launcher + '\nendlocal\n', encoding='ascii')
print(f'Extracted {len(manifest)} source files ({sum(x["bytes"] for x in manifest):,} bytes); created 3 pilot translation files.')
