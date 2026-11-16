# 第4批：正文说明 / Gameplay descriptions

Date: 2026-11-15. Continuation after terminology baseline and PR #1.

## Scope

Added 164 entries in `translation/gameplay-descriptions.properties`, registered in the build. This batch translates shared gameplay text, not campaign story text:

- Environmental descriptions and weather announcements, including darkness, snow, acid rain, wind, earthquakes and the Blood Moon.
- Potion timing, equipment slots, cursed items, shield restrictions, relics, souls and physical versus elemental protection.
- Crafting recipes, gathering materials, Mutagen, recruitment, upgrades, traits and serious wounds.
- Team morale, racial animosities, desertion, transformation, invisibility, passive units and effect restrictions.
- Completion/failure/mandatory objective markers and related help headings.

Main runtime now contains 2,396 entries, including six metadata entries. Content coverage is 2,390/4,215 (56.7% by entry count); 1,825 main keys remain in English. All three runtime files contain 2,410 entries. Prior translations, campaign samples and configured font are preserved. Unit descriptions remain at 28/326; this batch does not complete skill/item effect descriptions or the combat tutorial.

## Wording and source details

Reuse the established glossary and actual UI labels: 进阶, 解散, 技能, 特性, 圣物, 宝物, 物品仓库, 诱变剂, 岩石形态, 魔法护盾 and 灵魂捕获. Affinity/alignment is 阵营倾向 (Evil/Holy/Neutral), distinct from Faction/阵营; prestige is 资历 (Regular/Veteran/Elite).

Preserve the rules and qualifiers: non-stacking poison/magic regeneration; no shield with staves or two-handed weapons; no weapons/shields/staves on ranged units; items that cannot be removed; proportional HP transfer during transformation; temporary attributes lost when the new form is immune; physical protection does not imply elemental protection. Potions do not consume the unit's action, but the source limits their use to before attacking/casting.

Source key names do not always describe displayed text. `BLIZZARD_DESCRIPTION` describes falling ice, `AT_HIGHER_LEVELS_LARGER_GROUPS_ARE_SUMMONED` describes stronger groups rather than more units, and `HAPPY_DESCRIPTION` describes racial morale penalties. Translate the source value, not a guessed meaning of its key.

The general crafting tutorial describes learning related recipes after first crafting, whereas `CRAFTING_ITEM_HINT_UNLOCKS` explicitly says this is a chance. Both source statements are preserved; do not invent a guaranteed unlock rate. `COUNTER_MELEE_DESCRIPTION` says activation follows a melee strike; do not add a hit-only condition without engine evidence.

## Validation and next review

Check build key/placeholder/markup/coverage validation, Java decoding and four-style font coverage, and unchanged existing runtime values. Compare the full set of 164 selected source keys and retain all 32 bilingual campaign/expansion names in the Workshop description.

In-game review should cover long recruitment/crafting/morale help panels, equipment restrictions and weather tooltips. Source line breaks were adjusted for Chinese wording; automated checks do not prove text fits. The existing `UXX_Please_review_us` warning remains unresolved.

Next: detailed skill/item effect fragments and combat tutorials, then remaining unit descriptions. Shared events and campaign stories follow, starting with the Undead campaign.

Completed validation: all 164 selected source keys present; placeholders preserved; build key/HTML/coverage checks passed; Java decoded 2,410 runtime entries and checked four font styles plus 1,825 English fallback entries. All 2,232 prior main values and campaign samples were unchanged. All 32 campaign/expansion names were retained, and the Workshop description is 4,296 UTF-8 bytes. `git diff --check` passed.

Installed only the main runtime properties and `config.xml` into the local test item after backing up both files to the local installation backup (path omitted). Installed files match the package by SHA-256; all other existing mod files were verified unchanged. No Steam upload, commit or GitHub push was performed for this batch. Actual game layout remains pending.
