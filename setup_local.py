"""Extract local reference resources and optionally install a local test font.

Does not modify the game, editable translations, or Steam Workshop items.
Extracted game resources and fonts are intentionally excluded from Git.
"""
import argparse
import hashlib
import json
from pathlib import Path
import zipfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--game', type=Path, required=True, help='AOFTOTAL installation directory')
    parser.add_argument('--font', type=Path, help='Local Noto Sans SC TTF matching the configured test font (not redistributed)')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    archives = [args.game / 'aof.jar', args.game / 'aof-data.zip', *sorted((args.game / 'data').glob('*.zip'))]
    for archive in archives:
        if not archive.is_file():
            parser.error(f'Missing game archive: {archive}')
    if args.font and not args.font.is_file():
        parser.error(f'Missing font: {args.font}')
    manifest = []
    for archive in archives:
        with zipfile.ZipFile(archive) as bundle:
            for name in bundle.namelist():
                if name.startswith('com/aof/resource/text/i18n/') and name.endswith('.properties'):
                    data = bundle.read(name)
                    destination = root / 'source' / archive.stem / Path(name).name
                    destination.parent.mkdir(parents=True, exist_ok=True)
                    destination.write_bytes(data)
                    manifest.append({'archive': str(archive), 'entry': name,
                                     'file': str(destination.relative_to(root)),
                                     'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
    (root / 'source/manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    from inspection.expansion_levels import extract_current_levels
    extract_current_levels(args.game, root)
    if args.font:
        from prepare_font import prepare_font
        target = root / 'pilot-mod/com/aof/resource/text/font/noto-sans-sc.ttf'
        prepare_font(args.font, target)
    print(f'Extracted {len(manifest)} reference files. Next: python build_translation.py')


if __name__ == '__main__':
    main()
