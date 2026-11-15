"""Prepare a local regular-weight Noto Sans SC font for the game's Java 17 renderer.

Variable fonts can render at their minimum weight in this engine. Font files
remain local/ignored; license metadata is retained, not a release license bundle.
"""
import argparse
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont


def prepare_font(source: Path, destination: Path):
    with TTFont(source) as font:
        if 'fvar' in font:
            axes = {axis.axisTag: (400 if axis.axisTag == 'wght' else axis.defaultValue)
                    for axis in font['fvar'].axes}
            instantiateVariableFont(font, axes, inplace=True, updateFontNames=True)
        if 'fvar' in font:
            raise ValueError('Font must be static before packaging.')
        if font['OS/2'].usWeightClass != 400:
            raise ValueError('Supply a regular-weight (400) Noto Sans SC font.')
        destination.parent.mkdir(parents=True, exist_ok=True)
        font.save(destination)
    print(f'Prepared static regular font: {destination.name}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('font', type=Path, help='Local Noto Sans SC TTF (variable or regular)')
    args = parser.parse_args()
    prepare_font(args.font, Path(__file__).resolve().parent / 'pilot-mod/com/aof/resource/text/font/noto-sans-sc.ttf')
