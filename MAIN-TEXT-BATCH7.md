# 第7批：正文

Date: 2026-11-15. Continues on `codex/gameplay-descriptions`, retaining uncommitted batches 4–6.

## Scope and progress

Added 297 entries in `translation/skill-item-effects-3.properties`, covering the remaining source sequence from `IMMUNE_TO_PARALYZE` through `S_ATTACK_SPELLCASTERS_ONLY`. Includes immunity and wake-up conditions, movement/use restrictions, cooldowns, status application, summons, target categories, typed damage, regeneration and spell interactions.

Main runtime: 3,156 entries including six metadata entries. Content coverage: 3,150/4,215 (74.7% by entries), with 1,065 English fallback keys. All runtime files: 3,170 entries. Glossary: 1,543 keyed rows. Campaign samples and font remain unchanged; object descriptions remain at 28/326. Workshop description now includes `#7 正文` and retains every campaign name.

## Context and corrections

- Corrected the existing `COMMAND` label in batch 5 from 指挥 to 统御. The game uses it in `ActionableAttribute` control-type arrays; the new immunity text and established Command-item names now agree. This is the only intentional change to a prior main value.
- Checked local `MarkOfDeath.getNameString()` and `MarkOfHunted.getNameString()`: they use `MARKOFDEATH_SPELL` (Mark of Pain/痛苦印记) and `MARKOFHUNTED_SPELL` (Deathmark/死亡印记). Their effect descriptions follow those actual names rather than the outdated English description labels.
- Preserve source values over key names: the wave effect doubles damage, not attack; the Storm/Vortex description applies Overloaded/过载; Song of Bravery is 勇气之歌 despite the SIRENS key; the expiration text says after the battle, not necessarily after the next battle.
- Distinguish on-attack from on-hit, defender/attacker effects, guaranteed effects from chance, typed resistance from immunity, per-turn effects from duration, and non-physical defence from general damage protection. Generic damage fragments do not invent a recipient.
- Reuse 严重失误, 生命充盈, 冰冻光环, 石肤术, 腐朽, 惩戒, 勇气之歌 and other established terms. Added target-group labels to the glossary; Black Guards is 黑卫士 and remains distinct from Black Knights/黑骑士.
- Checked summon helper arguments: some adjacent placeholders are count plus a tag, not two numbers. Retain every placeholder. The existing English-style number-word generator and untranslated number/conjunction strings remain a separate task, as documented in batch 6.

## Validation and next review

Validation passed: exact 297-key selection and placeholder multiplicities, build/markup/coverage checks, Java decoding of 3,170 runtime entries and four-style font coverage including 1,065 English fallbacks. All 2,859 prior main keys remain; COMMAND is the only changed prior value. Campaign samples are unchanged. All 32 campaign names are retained; the balanced Workshop description is 4,671 UTF-8 bytes. Glossary and staged runtime comparisons passed, as did `git diff --check`.

Backed up and installed the main runtime and config locally. Backup: `backups/workshop-3840511924-before-gameplay-batch7-2956908c`. Both installed files match the staged package by SHA-256, and the backed-up main file matches the pre-batch snapshot. Batches 4–7 remain uncommitted/unpublished; no Steam upload was performed.

User feedback confirms normal appearance through batch 5. Batches 6–7 still require in-game review, especially composed status tooltips, target lists, control immunity and paired duration/count tags. The `UXX_Please_review_us` warning remains unresolved.

Next: remaining effect fragments and help, number/conjunction composition, unit descriptions, then shared events and the Undead campaign.
