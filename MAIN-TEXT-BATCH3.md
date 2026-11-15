# Main text: terminology batch 3

Adds 1,027 entries while establishing the core terminology baseline:

| Editable file | New entries | Scope |
| --- | ---: | --- |
| `translation/item-name-terms.properties` | 449 | Item/resource names and name templates, including 51 crafting materials |
| `translation/skill-attribute-terms.properties` | 578 | Skills, attributes, statuses, conditions, crafting professions, set names and short cost/duration/targeting fragments |

All 1,205 previously deployed main entries are preserved. Main coverage is now 2,232 keys including six metadata keys: 2,226/4,215 content entries, or 52.8%. Another 1,989 main entries use English fallback. The 14 unchanged campaign sample entries bring the runtime total to 2,246. This is entry coverage, not word coverage; long descriptions remain a substantial part of the remaining work.

## Defined coverage

- `ACIDBLOOD` through `ANCIENTCOAL_ITEM`: all 937 labels (399 item names/templates, 538 skill/attribute/condition and related labels).
- `LIVERWORM_ITEM` through `WHITEYARROW_ITEM`: all 51 crafting material names.
- `CRAFTINGBLACKSMITH` through `CRAFTINGJEWELER`: all nine crafting-profession labels.
- All 30 `GROUP_SET_` item-set labels.
- Previous 326 object-name and 73 race/group-label checks remain active. Object descriptions remain at 28/326.

The correct item/resource name/template total is 450, including a generated scroll-name template and the random-item label. The old 455 estimate counted every `_ITEM` suffix and included five UI prompts. Do not report these counts as distinct item objects or as completed item descriptions.

## Context decisions

`TERMINOLOGY.md` now contains 1,528 keyed entries. Existing translations were retained. Meaning is taken from displayed English text and relevant descriptions or engine inspection:

| Source | Chinese | Reason |
| --- | --- | --- |
| Regrowth | 复生 | The tutorial says the killed unit recovers after battle; distinguish from Regeneration/再生 and Resurrection/复活术. |
| Battle Frenzy / Battle Rage / Bloodlust | 战斗狂乱 / 战斗狂怒 / 嗜血 | Separate names and effects; internal BLOODLUST actually displays Battle Rage. |
| Precision | 精准 | Internal key CRITICALHIT; do not confuse it with the combat result Critical Hit/暴击. |
| Infravision | 红外视觉 | Internal key STEALTHATTACK is misleading. |
| Executioner | 刽子手 | Internal key HEADHUNTER is misleading. The Headhunter item set remains 猎头者. |
| Shitanto | 希坦刀 | Provisional transliteration. Engine item type is two-handed weapon; no basis for calling it a short blade. |
| Elemental | 元素生物 / 元素 | Creature/attribute versus item-set context. |
| Slow | 慢 / 迟缓术 | Speed option versus spell context. |

Invulnerability Formula retains an evocative name (无敌配剂), but the engine description says it protects against physical attacks and not elemental attacks. Future effect text must preserve that limitation. Pyradyne/派拉丁, Elowan/埃洛万 and item-related character names remain provisional; they are working translations, not user-approved names.

## Validation and next work

The build checks every declared coverage block, source-key existence, duplicates, placeholders, HTML and runtime escaping. Validate the package with the configured regular Noto font in all four styles and include remaining English fallback text.

After restart, check skill menus, inventory names, long item names, crafting professions/materials, set labels, scroll names, costs and durations. Automatic validation does not prove labels fit on screen or replace human translation review.

The next content stage is gameplay explanations and tooltips, using this glossary and revising ambiguous names when the full effect requires it. Shared events and campaign stories follow the recorded plan; campaign build support still needs extension. The unresolved `UXX_Please_review_us` warning is not addressed by this batch. No Steam upload or GitHub push is included.

Completed checks: build/placeholder/HTML coverage; Java decoding of all 2,246 runtime entries; configured-font glyph coverage in four styles, engine symbols and 1,989 English fallback entries; all 1,528 glossary rows matched the English source and generated Chinese runtime. The 1,205 previous main values, campaign files and font were retained.

Installed the main runtime file and local description into item 3840511924 after a fresh backup (`backups/workshop-3840511924-before-terminology-batch3-26bef6fd`). Both installed files matched the package by SHA-256. Actual game layout and wording review remain pending.
