# 第4批：通用事件

Date: 2026-11-15. Continues on `codex/gameplay-descriptions`. In-game testing remains deferred at the user's request. The user prefers natural, faithful Chinese over added dialect or forced colloquial phrasing; their approved beggar option from batch 3 is preserved.

## Scope

Added 31 event families: BlademasterHero, CemeterySunset, Comet, Crates, Dragon, DwarfGod, DwarfMutant, DwarfRouge, Eclipse, Hangman, HeroBones, HungryGhoul, NecromancerAndMonk, NecromancerZombies, OrcsAndGoblins, OrcsBattle, OrcsCamp, OrcsWarehouse, PaladinAndBlackKnight, RazorEdge, Ruby, Skeletons, Swords, TrainPeasant, Traveller, Treasure, UndeadVillage, VampireAndWerewolf, Vulcano, Winter and Witch.

- `translation/shared-conversations-4.properties`: 122 keys across 40 conversation groups.
- `translation/shared-events-4.properties`: 34 keys, comprising 16 choices/descriptions and the two-entry Blademaster duel introduction.
- Added 156 content keys. Cumulative shared coverage: 638/3,163 (20.2%), comprising 416 standalone conversation and 222 level/choice keys. Counts include repeated speaker labels.
- Cumulative selected scope: 77 event families, 136 standalone conversation groups, 107 linked choices and four follow-up levels. Runtime totals 4,877 entries. Remaining shared fallback: 2,525 keys (1,922 level/choice, 603 conversation).

## Translation and context

Retained the muddy-bootprint joke between the Paladin and Black Knight, the Vampire/Werewolf exchange and the Dwarven Rogue's insinuations about theft. Kept character voices without inventing regional dialect. Translated the Monk's Latin prayer by meaning. In the Vampire dialogue, “bird” refers to a woman, and Count Passionfruit is a teasing nickname rather than an actual title.

Provisional names: Holy Council＝神圣议会, Elsa＝艾尔莎, Isabelle＝伊莎贝尔, Three Devils＝三魔峰, Iceland/Icelands＝冰原. Local Forest campaign text places Three Devils in the southern volcanic area; Greenskins campaign text describes Iceland as northern snowy terrain. These are fictional place names in this context. Reused 剃刀之锋、矮人游荡者、皇家卫士、剑术大师 and 战争食人魔.

Checked choices, initial triggers and commands in the installed shared-event XML. The Blademaster training reward follows a polite refusal, despite the internal `_accept` identifier; the Chinese retains that deliberate humility. Insulting him leads to the translated duel introduction. Knight rivalry first wounds both knights; its later fatal branch removes one, so the narration does not imply both die.

Orc/Goblin feast options retain 100/250 experience amounts. The single-Goblin option opens a manual unit selector and then calls `on-function-14`; the checker now follows that callback and verifies its conversation outcome. Source narration for the Orc duel credits the winner with 200 experience, while the script targets `orc`; the wording follows the narration without changing gameplay. Source “all Goblins” text is retained, but the removal command excludes heroes. These distinctions are recorded for later gameplay review.

Village looting can yield gold or trigger combat, while the Necromancer option recruits Skeletons. Preserved the separate outcomes, battle-risk warnings and the source's implicit narrative details. Removed an unmatched closing parenthesis from the English Necromancer-choice description in the Chinese text. No gameplay XML was modified.

## Validation and installation

Passed exact 156-key source-set checks, build validation, variables, HTML, `=BR=` markers and namespace/coverage checks. XML validation covers all 136 standalone groups and 107 choices, including one manual-unit-selection callback. Java decoded 4,877 runtime entries and checked translated text, engine symbols and 2,525 English fallback entries in four font styles. All previous runtime values are preserved, including the user's approved batch-3 beggar wording; main/campaign files remain byte-identical to the pre-batch snapshot.

Description includes `#4 通用事件`, uses 5,578 UTF-8 bytes and preserves all 32 bilingual campaign/expansion names. BBCode is balanced. Backup: the local installation backup (path omitted). Installed only both shared resources and config, verified against staging by SHA-256; every other installed mod file is unchanged.

No game test, Git commit/push or Steam upload was performed. `items.xlsx` remains untouched. Continue remaining shared travel events and locations, then longer shared stories and the Undead campaign. Deferred game review and the unrelated `UXX_Please_review_us` warning do not block translation.
