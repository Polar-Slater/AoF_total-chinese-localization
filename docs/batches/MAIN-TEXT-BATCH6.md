# 第6批：正文

Date: 2026-11-15. The user tested the version through batch 5 and reported normal in-game appearance. This is positive feedback for that version, not exhaustive text/layout approval or validation of this new batch.

## Scope and progress

Added 254 entries in `translation/skill-item-effects-2.properties`: 252 consecutive remaining effect fragments from `UNIT_CAN_CARRY_TWO_ADDITIONAL_ARTEFACTS_OR_TROPHIES` through `UNAFFECTED_BY_BEING_SURROUNDED`, plus the invisible-unit and burrowed-unit help dialogs. Covers summons, corpse/soul mechanics, life/experience transfers, action limits, movement, stealth, traps, weather, morale, immunity and equipment exceptions.

Main runtime: 2,859 entries including six metadata entries. Content coverage: 2,853/4,215 (67.7% by entries); 1,362 main keys still use English fallback. All runtime files: 2,873 entries. Existing translations, campaign samples and font are preserved. Unit descriptions remain at 28/326; no shared-event or campaign story content was added.

Workshop headings are now `#4 正文`, `#5 正文` and `#6 正文`, following the user's Main text＝正文 preference. Every campaign/expansion name is retained.

## Wording and mechanics

- Reuse 时间偏移, 后备队, 被催眠, 被附身, 受诱惑, 忠诚, 潜地中, 网缚, 熔岩尖刺 and established weather names.
- Preserve enemies-versus-all-units distinctions, living-enemy restrictions, recipients of transferred resources, per-turn/per-battle limits, guaranteed versus chance-based effects and nonlethal damage clauses.
- Preserve equipment exceptions: the relevant effect permits dual-wielding two two-handed weapons, or using a two-handed weapon with a shield. Do not replace these with the general equipment restrictions from batch 4.
- Translate source values over internal key names. The continuous-area effect ends when the caster is incapacitated, not only when dead. The slipping line does not explicitly mention lost actions. The Parry/Riposte upgrade says permanently active, not invulnerable. `CANNOT_BE_ENTANGLED_OR_ENSNARED_TAMED` mentions only Entangled and Ensnared, not Tamed.
- The game code supplies two arguments for `UNIT_RESTORES_UP_TO_S_ACTIONS_THIS_TURN`: an action count and a formatted duration. Preserve both rather than limiting it to this turn from the key name. `PLUS_UP_TO_S_S_DEFENCE` receives a number and a separate tag; do not assume both placeholders are numeric.
- The general invisibility effect says actions other than movement reveal the unit; its detailed help also lists trap placement, potions and Camouflage as exceptions. Preserve both source statements, including those explicit exceptions.
- Some generated number words and conjunctions remain untranslated. `StringHelper.numberToString` uses an English-style composition algorithm, so this needs separate context review rather than treating every numeric argument as an integer or blindly rewriting the global conjunctions.

## Validation and next review

Check all selected keys/placeholders, HTML, previous main values, the configured font in four styles and English fallback text. Compare installed files with the package after backup and retain all 32 bilingual campaign/expansion names.

New in-game checks: summoned-unit durations, transfer recipients, action counts, trap damage, weather effects, immunity tooltips and invisible/burrowed-unit help. The user's previous successful test does not cover this batch. The existing `UXX_Please_review_us` warning remains unresolved.

Next: remaining effects and help, generated number/conjunction fragments, and unit descriptions; then shared events and the Undead campaign.

Completed validation: all 254 selected keys and placeholder multiplicities, build/HTML/coverage checks, Java decoding of 2,873 runtime entries and four-style font coverage including 1,362 English fallback entries. All 2,605 previous main values and campaign samples were unchanged. All 32 campaign/expansion names were retained; the description is 4,560 UTF-8 bytes and uses the agreed 正文 headings. `git diff --check` passed.

Backed up the two changed installed files to the local installation backup (path omitted), then installed the main runtime and `config.xml`. SHA-256 checks confirm package/installed equality and no changes to other mod files. No Git commit, GitHub push or Steam upload was performed for batch 6. Batches 4–6 remain uncommitted on the working branch.
