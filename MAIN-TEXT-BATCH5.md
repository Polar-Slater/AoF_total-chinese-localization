# 第5批：战斗教程与效果说明

Date: 2026-11-15. Continues batch 4 on `codex/gameplay-descriptions`; both batches remain local work pending commit/publication.

## Scope and progress

- `translation/combat-tutorials.properties`: 20 battle and world-map tutorial pages. Covers movement, melee/backstab, ranged attacks, morale/panic, damage types, combat logs/dice, burrowing, spell targeting/cooldowns, unit details/upgrades, campaign locations and open-world events. This translates event-system help, not shared-event story content.
- `translation/skill-item-effects.properties`: 189 shared effect fragments and supporting entries. Covers prestige scaling, healing/magic restoration, morale, damage/defence/resistance modifiers, targeting, duration, transformation, detection, teleportation, dispelling and Slayer.

Added 209 keys. Main runtime: 2,605 entries including six metadata entries. Content: 2,599/4,215 (61.7% by entry count), with 1,616 English fallback keys. All runtime files: 2,619 entries. The glossary now has 1,529 keyed rows. Existing batches, campaign samples and font are retained. Object descriptions remain at 28/326.

All keys with the `BATTLE_TUTORIAL_` and `WORLDMAP_TUTORIAL_` prefixes are now translated, including the previously translated closing page. Other tutorial/help keys and many detailed effects still remain; do not claim complete gameplay localization.

## Context and terminology

Use 地精, 步兵, 法师, 牵制, 敏锐感官, 灵视术, 潜地, 钢铁之肺, 紫心勋章, 幸存者 and existing status labels. Slayer is 杀手, with the dynamic name `{0}杀手`, distinct from the Assassin/刺客 unit. Keep the actual UI labels 保存游戏 and 结束战斗 in menu help.

Checked the local game's `Attribute` class for dynamic arguments: in `S_ATTACK_S` and `S_ATTACK_S_S_ATTACK_PER_LEVEL`, `{0}` is the attack type and `{1}` is its value. The Chinese order is therefore `{0}攻击{1}`, not `攻击{0}{1}`. `S_DEFENCE_FOR_S` supplies a signed defence modifier and a formatted turn duration, so no extra unit is appended to the duration placeholder.

`BACKSTAB_ATTACKS_ARE_IGNORED` is used in Parry and Riposte descriptions, alongside melee-only restrictions. It means the effect excludes backstab attacks, not that the unit is immune to backstabs. The separate source `IMMUNE_TO_BACKSTAB` covers immunity. `ATTACK_CAUSE_S_DAMAGE_SELF` belongs to Retribution; retain self-damage and its supporting statement that both successful and failed attacks cause damage.

Retain source qualifiers: movement-before-backstab checks, unblocked/idle morale regeneration, movement allowed during idle MP recovery, failed spells causing no cooldown, poison immunity still receiving direct acid damage, range/target restrictions, reductions never eliminating damage/statuses, and all signed values and paired placeholders.

The tutorial calls SHARPSENSES “Sharp Senses” while the current label is “Fine Senses”; both use the established 敏锐感官. Retain the original English dice example as a literal log example and explain Hit as 命中. It is an example, not untranslated instructional prose.

## Validation and next review

Validate the exact selected key sets, placeholder multiplicities, HTML, complete named tutorial-prefix coverage, font glyphs and unchanged prior runtime values. Check all 32 campaign/expansion names remain in the Workshop description.

In-game checks remain necessary for the long tutorial pages and composed effect tooltips, especially type/value order, duration, prestige columns, Parry/Riposte exceptions and paired placeholders. The existing `UXX_Please_review_us` conversation warning is outside this batch.

Next: remaining detailed effects, help dialogs and unit descriptions, then shared events and the Undead campaign.

Completed checks: all 209 selected keys and placeholder multiplicities; build/HTML validation and coverage of all 21 named tutorial keys; Java decoding of 2,619 runtime entries, four-style font coverage and 1,616 English fallback entries; all 2,396 prior main values and campaign samples unchanged. Glossary row count is 1,529. All 32 campaign/expansion names remain, and the Workshop description is 4,430 UTF-8 bytes. `git diff --check` passed.

Installed the main runtime and `config.xml` after backing up both files to `backups/workshop-3840511924-before-gameplay-batch5-1f486da2`. SHA-256 checks confirm the installed files match the staged package and all other mod files are unchanged. No Steam upload, Git commit or GitHub push was performed for this batch. Long-page and composed-tooltip layout still requires in-game review after restart.
