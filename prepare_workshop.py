"""Stage the local pilot for the user's existing Workshop item; does not upload."""
from pathlib import Path
import shutil
import xml.etree.ElementTree as ET
import subprocess
import sys
from PIL import Image
import argparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--item', type=Path, required=True, help='Existing local Workshop item directory')
parser.add_argument('--owner-id', required=True, help='Expected owner-user-id from your item config.xml')
args = parser.parse_args()

root = Path(__file__).resolve().parent
item = args.item
tree = ET.parse(item / 'config.xml')
config = tree.getroot()
assert config.findtext('owner-user-id') == args.owner_id, 'Unexpected owner; stop.'
assert (root / 'pilot-mod/com/aof/resource/text/font/simhei.ttf').is_file(), 'Run setup_local.py with --font first.'
label = 'Chinese (Simplified) - Test'
for filename in [root / 'translation/messages-zh.properties', root / 'pilot-mod/com/aof/resource/text/i18n/messages-zh.properties']:
    lines = filename.read_text(encoding='utf-8').splitlines()
    filename.write_text('\n'.join('LANGUAGE=' + label if line.startswith('LANGUAGE=') else line for line in lines) + '\n', encoding='utf-8')

subprocess.run([sys.executable, str(root / 'build_translation.py')], check=True)
package = root / 'workshop-package'
shutil.copytree(root / 'pilot-mod', package, dirs_exist_ok=True)
description = (root / 'workshop-assets/description.txt').read_text(encoding='utf-8').strip()
assert 5 <= len(description) <= 8000, 'Description must contain 5-8000 characters.'
config.find('description').text = description
ET.indent(tree, space='  ')
tree.write(package / 'config.xml', encoding='utf-8', xml_declaration=True)
with Image.open(root / 'workshop-assets/preview.png') as preview:
    assert min(preview.size) >= 100, 'Preview must be at least 100 x 100.'
    preview.convert('RGB').save(package / 'preview.jpg', quality=95, subsampling=0)
backup = root / f'backups/workshop-{item.name}-before-install'
if not backup.exists():
    shutil.copytree(item, backup)
assert ET.parse(package / 'config.xml').findtext('owner-user-id') == args.owner_id
print('Prepared workshop-package; backed up existing item; preserved owner ID.')
