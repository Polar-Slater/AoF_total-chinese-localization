# Main text: terminology batch 2

Added 396 entries while continuing the terminology-first plan:

| File | New entries | Scope |
| --- | ---: | --- |
| `translation/unit-race-terms.properties` | 368 | Remaining 298 unit/scenery names and 70 race/group labels |
| `translation/battlefield-terms.properties` | 28 | Terrain, Swamp tooltip, battle-start text and related stat/status fragments |

All 326 object names and the 73-label source race/group section are supplied. Existing object descriptions remain at 28/326: completing names does not complete the bestiary. Main coverage is 1,199 content keys out of 4,215 (28.4%); six additional metadata keys produce a 1,205-entry main file. There are 3,016 missing main keys. The 14 campaign sample entries bring the package total to 1,219.

## Terminology review

The 501-key `docs/TERMINOLOGY.md` is the working baseline. Identical short English terms were checked for consistent Chinese labels. Vase was normalized from 空花瓶 to 花瓶. Examples checked against English descriptions:

- Turtle roams dunes and oases: 乌龟, not 海龟.
- Fire Archer shoots burning arrows: 烈焰弓箭手, avoiding the modern rocket reading of 火箭射手.
- Alpha Werewolf leads werewolves: 狼人首领.
- Revenant is an ancient skeletal undead: 复生亡灵. Shade is 暗影幽魂; neither is merged with Wight/尸妖 or Lich/巫妖.
- Dryad/林妖 is distinct from Ent/树人; Drider/蛛人 is distinct from a spider.
- Displayed terminology must follow the source value: key GHOST displays Incorporeal (无实体), while key INCORPOREAL displays Phasing (相位化).
- Grogan/格罗甘 and Mancubus/曼库魔 remain provisional transliterations. Do not infer campaign character names from internal unit IDs.

No full English descriptions or font binaries are added to Git. Campaign samples are retained without translation changes. Further terminology work should cover skills, attributes, item names and crafting materials before expanding long-form gameplay text.

## Font correction

The local test font is now static regular Noto Sans SC. `prepare_font.py` pins the variable font to weight 400 and removes variable axes while preserving license metadata. All four runtime font settings point to `noto-sans-sc.ttf`.

The Java validator now reads the configured font filenames, checks plain/bold/italic/bold-italic, and includes the engine's U+00A0 and U+2022 prefixes. It fails with SimHei and passes with the new font. Supplying the extracted English main file checks all 3,016 fallback entries too. A headless Swing HTML preview was inspected; Swing may use its own fallback fonts, so the explicit glyph regression check is the evidence of missing-symbol coverage, not the old-font preview alone.

Font files are local and ignored. A future distributable release still needs the appropriate font license materials. Stale unused SimHei files may remain in the local test folders; no current font setting references them.

## In-game checks after restart

1. Reopen the Swamp condition tooltip: verify Chinese text, round bullets and no square prefixes.
2. Check main-menu buttons, battle log, compact stat columns and tooltips for changes in font width/height.
3. Browse the bestiary's longer names and confirm they fit or scroll correctly. Unit descriptions not yet translated will still be English.
4. Check the previously translated campaign sample and an English story screen, since the story font also changed.

The `UXX_Please_review_us` validation warning remains unresolved. No Steam upload or GitHub push is part of this batch.

The main runtime file, configured Noto font and local description were installed into the local Workshop item after a fresh backup (the local installation backup (path omitted)). Each installed file matched the package by SHA-256. Other installed files were retained.
