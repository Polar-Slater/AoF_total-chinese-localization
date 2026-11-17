"""Create a compact-line-height button font for the fixed-size inventory UI.

Uses a locally supplied Noto Sans SC Regular font; no glyph outlines or advance
widths are changed. Keep the upstream OFL alongside the generated derivative.
"""
import argparse
from pathlib import Path

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont


def prepare_ui_font(source: Path, destination: Path):
    if source.resolve() == destination.resolve():
        raise ValueError('Use the original font as input, not the output file.')
    with TTFont(source) as font:
        if 'fvar' in font:
            axes = {a.axisTag: 400 if a.axisTag == 'wght' else a.defaultValue
                    for a in font['fvar'].axes}
            instantiateVariableFont(font, axes, inplace=True, updateFontNames=True)
        if 'fvar' in font or font['OS/2'].usWeightClass != 400:
            raise ValueError('Expected a static regular-weight font.')
        family = font['name'].getDebugName(1) or ''
        if 'Noto Sans SC' not in family:
            raise ValueError('Expected Noto Sans SC as the source font.')
        # At 18 pt, leave room for the 8-pixel text border above a 467-pixel
        # inventory panel in its 500-pixel container (line height <= 25).
        em = font['head'].unitsPerEm
        font['hhea'].ascent = em
        font['hhea'].descent = -round(em * .2)
        font['hhea'].lineGap = 0
        font['OS/2'].usWinAscent = em
        font['OS/2'].usWinDescent = round(em * .2)
        font['OS/2'].sTypoAscender = em
        font['OS/2'].sTypoDescender = -round(em * .2)
        font['OS/2'].sTypoLineGap = 0
        # A distinct family avoids Java's font-metrics cache mixing the original
        # and the derivative. Keep copyright, license and attribution records.
        names = {1: 'AoF Han UI', 2: 'Regular', 3: 'AoF Han UI Regular 1.0',
                 4: 'AoF Han UI Regular', 6: 'AoFHanUI-Regular',
                 16: 'AoF Han UI', 17: 'Regular',
                 21: 'AoF Han UI', 22: 'Regular'}
        font['name'].names = [n for n in font['name'].names if n.nameID not in names]
        for name_id, value in names.items():
            font['name'].setName(value, name_id, 3, 1, 0x409)
            font['name'].setName(value, name_id, 1, 0, 0)
        destination.parent.mkdir(parents=True, exist_ok=True)
        font.save(destination)
    print(f'Prepared compact button font: {destination.name}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('font', type=Path, help='Local original Noto Sans SC Regular TTF')
    args = parser.parse_args()
    prepare_ui_font(args.font, Path(__file__).resolve().parent /
                    'pilot-mod/com/aof/resource/text/font/aof-han-ui.ttf')
