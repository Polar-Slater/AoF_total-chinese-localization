# AI handoff: Age of Fear Total Simplified Chinese translation

Last updated: 2026-11-15. Read this before continuing the project. This document records prior work, not authorization to publish or change another person's Steam account.

## Latest description layout: grouped by resource files

The user requested grouping 总体进度 by game resource files instead of translation batches. The description now lists messages-en.properties → messages-zh.properties (4,215/4,215; 100%), shared-en.properties → shared-zh.properties (883/2,144; 41.2%), and shared-conversations-en.properties → shared-conversations-zh.properties (699/1,019; 68.6%), followed by the shared total (50.0%). All campaign sections and bilingual names remain unchanged. Current description: 4,699 UTF-8 bytes; source, package and installed config match. Only the installed description changed; other metadata and mod files were verified unchanged. Backup: backups/description-by-file. No Steam upload. Description byte counts and batch headings in the milestone notes below are historical.

## Current milestone: shared text 50% (2026-11-15)

The user uploaded the previous version through shared batch 5 to Steam Workshop and reported no in-game errors, then set today's target to 50%. This is a user smoke test, not exhaustive review. Shared batches 6–7 add 680 keys and reach 1,582/3,163 shared content keys (50.0%): 883 level/choice and 699 conversation keys, plus four metadata keys. Total runtime entries: 5,821. Main messages remain complete at 4,215 content keys; the 14 campaign samples remain unchanged.

New editable files: `shared-bases-6.properties` (363), `shared-systems-7.properties` (110), `shared-conversations-7.properties` (207). Eight faction bases, desertion, five minigames, Windmill, weather invocations and common prompts. See `SHARED-TEXT-50-PERCENT.md` for scope and source discrepancies. Continue remaining shared locations/side stories, then the Undead campaign. No need to request game tests before further translation.

The manifest now declares location_prefixes. XML validation indexes shared levels and conversation XML across aof-data.zip and data/*.zip, follows callbacks, and reports 22 referenced conversations in separate campaign resources. They still fall back to English; do not claim every base interaction is translated. Dynamic minigame fragments assigned directly in XML also remain English. Do not rewrite gameplay scripts merely to hide those fragments. Prior shared values, the approved beggar sentence and bilingual place names must remain unchanged.

Description updated to 6,164 UTF-8 bytes, with `#6 共享地点`, `#7 共享玩法`, accurate cumulative coverage and user feedback; all 32 bilingual campaign names preserved. Source/package/install validation and backup details are recorded in the milestone note. New translations have no game test or Steam upload. Earlier upload/no-test statements below describe historical work. Previous batch 5 has now been uploaded successfully by the user. Main 4–8 and shared 1–7 are included in the 50% milestone Git submission requested by the user; historical uncommitted/unpublished notes below refer to their original completion dates. Do not touch the pre-existing `items.xlsx`.

## Latest user direction: prioritize translation; defer game tests

Place-name preference: use `中文名 (English)` in location labels and narrative/dialogue, preserving the original English spelling/case. The user's `斯托斯 (Storrs)` is a format example, not evidence of a game location. Updated the shared volcanic-event narration to 三魔峰 (Three Devils) and 冰原 (Iceland). Carry this convention into subsequent translations.

After completion of main messages, the user asked for shared-event examples and counts, accepted starting with common travel events and party interactions, and said to proceed at our pace. Shared batches 1–7 are now installed locally; continue in complete event families with their linked choices/results.

Standing instruction: put in-game testing aside and focus on translation. Continue autonomously through complete event families; automated text/branch validation continues, but do not stop for screenshots or ask the user to test before continuing. No game session was launched for batches 3–5.

Latest wording feedback: user preferred “这个乞丐在浪费我们的时间，我们走吧。” to “这乞丐净耽误工夫，我们走。” Updated `shared-events-3.properties` line 2, regenerated and synced the one runtime value locally. Use natural, faithful Chinese; avoid forced colloquialism. This correction is preserved in batch 4.

Terminology preference: translate “Main text” as “正文” in Chinese descriptions and progress labels (for example, `#1 正文`).

Latest user feedback: the user tested the version through batch 5 in game and said everything looked normal, then asked to continue. Treat this as a successful user smoke test of that version, not exhaustive review. The user questioned “正文说明”; public headings have been simplified to “正文”.

The user has restored the original order: establish consistent terminology for units, stats, items and skills; then translate gameplay descriptions, shared events and campaign stories, starting with the Undead campaign. This supersedes the earlier campaign-deferral direction. Follow `LOCALIZATION-PLAN.md`. The core terminology baseline is now established in `TERMINOLOGY.md`; continue reviewing context and provisional names while moving into gameplay descriptions. Keep all completed translation batches.

A later screenshot showed square prefixes in the Swamp tooltip. Inspection confirmed the engine inserts `&nbsp;` and U+2022, while SimHei lacks U+00A0/U+2022. The earlier validator only checked translation values. This is now addressed with a local static regular Noto Sans SC font and expanded checks; confirm actual game appearance after restart.

## Latest upload issue: description byte limit

Subsequent user preference: remove English explanatory text from the Workshop description, but retain all campaign names. The description is Chinese with all 32 bilingual campaign/expansion names preserved, plus the English game title and exact menu/language labels needed for setup. The initial Chinese-only description was 4,134 UTF-8 bytes; the historical shared batch 5 description was 5,776 bytes; the current description is 6,164 bytes. The 7,062-byte version below is historical. Local config was backed up before this update; no upload was performed.

The user's Workshop Manager upload returned `InvalidParam` on 2026-11-15. Steam's workshop log at 17:30 shows content/preview transfer followed by Invalid Parameter. The description was 6,381 characters but 8,341 UTF-8 bytes; Steam documents an 8,000-byte maximum (https://partner.steamgames.com/doc/api/ISteamRemoteStorage#constants). This was a likely cause; the user has since reported a successful upload, though this does not independently isolate the original cause. Both packaging and the local PowerShell helper now enforce a conservative 7,999-byte maximum before writes. The original description and 8,000/8,001-byte cases are rejected by both scripts; normal packaging passes. Repeated open-campaign and expansion status table rows were compacted into lists without dropping campaign names. Source, package and installed descriptions are now 7,062 bytes. Local metadata was backed up and updated; user should reopen Workshop Manager and retry. No assistant upload was performed. Original description text is backed up at `backups/workshop-description-before-byte-limit-fix.txt`.

## 共享事件 batch 5 (historical; user has since uploaded): global-event text milestone

Added remaining 40 SGE families plus SXX_Gambler, 264 keys: 76 in `shared-conversations-5.properties` (55 groups), 188 in `shared-events-5.properties` (87 choices with 172 fields, plus 16 follow-up dialogue keys). Cumulative: 118 families, 191 standalone groups, 194 choices, eight follow-up levels (seven have dialogue; Three Witches has no text). Shared content: 902/3,163 (28.5%), 492 conversation + 410 level/choice keys. Runtime total: 5,141. Remaining shared fallback: 2,261 (1,734 level/choice, 527 conversation).

All 487 SGE_ conversation keys and all 410 LevelGlobalEvent* source keys are covered; build enforces this milestone. Next: shared locations and longer side stories, then Undead campaign. Generic shops reached by travel choices and Windmill rebuilding text are outside completed scope. Do not claim all shared content or the whole game is translated.

XML checker now follows exec-trigger callbacks with cycle protection, covering Blood Sisters cancellation as well as the sacrifice outcome. Manifest textless_level_prefixes declares LevelGlobalEventThreeWitches01.; build rejects source text under that prefix and XML checker verifies the actual level exists without dialogue. Drunken Dwarf source says 50% success, but script has two reward branches and one battle branch: Chinese omits the inaccurate numeric probability and records the difference. Place names include 伊凯乌斯家具 (IKEUS FURNITURE) and 风车磨坊 (Windmill); previous bilingual names and approved beggar wording remain unchanged.

All source/build/XML/Java/font/preservation checks passed. Description is 5,776 UTF-8 bytes with all campaign names intact. Backup: `backups/workshop-3840511924-before-shared-batch5-e8f18176`; additional pre-Windmill-suffix snapshot: `backups/before-windmill-place-label`. Installed only both shared resources and config, final hashes recorded, all other installed files unchanged. Main 4–8 and shared 1–5 remain uncommitted/unpublished, items.xlsx untouched. No game test or upload. Continue translation without requesting game testing.

## 共享事件 batch 4 (historical, unreleased)

Added 31 event families and 156 content keys: 122 in `shared-conversations-4.properties` (40 groups), 34 in `shared-events-4.properties` (16 choices/descriptions plus Blademaster battle introduction). Cumulative: 77 families, 136 standalone groups, 107 choices, four follow-up levels, 638/3,163 shared keys (20.2%). Shared resources contain 416 conversation and 222 level/choice content keys, plus four metadata entries. All runtime files total 4,877 entries. Remaining shared fallback: 2,525 (1,922 level/choice, 603 conversation). Previous values, including the approved beggar correction, are preserved. See `SHARED-EVENTS-BATCH4.md`.

Includes knight rivalry, Vampire/Werewolf dialogue, Orc encounters and Blademaster training. The training reward follows a polite refusal; `_accept` is an internal identifier, not the choice's meaning. The Orc feast's manual selector calls on-function-14; XML validation now follows that callback. New provisional names and source/gameplay distinctions are documented in the batch notes and glossary. Iceland means a northern snowy region in local campaign context; Three Devils is a southern volcanic region.

Exact source sets, build, HTML/variables/engine breaks, XML references including callback, Java decoding and four-style font checks passed. Description is 5,578 UTF-8 bytes with all campaign names intact. Backup: `backups/workshop-3840511924-before-shared-batch4-e681802c`. Installed only both shared resources and config; hashes verified, every other installed file unchanged. Main 4–8 and shared 1–4 remain uncommitted/unpublished. `items.xlsx` untouched. Game tests remain deferred; do not request a test before continuing translation. Next: remaining shared travel events/locations, longer shared stories, then Undead campaign.

## 共享事件 batch 3 (historical, unreleased)

Added 20 event families and 226 keys: 142 in `shared-conversations-3.properties` (43 groups), 84 in `shared-events-3.properties` (40 choices/descriptions plus two battle introductions). Cumulative: 46 families, 96 standalone groups, 91 choices, 482/3,163 shared content keys (15.2%): 294 conversation and 188 level/choice keys. Generated shared files contain 296 and 190 entries including metadata; all runtime files total 4,721. Remaining shared fallback: 2,681 (1,956 level/choice, 725 conversation). All earlier runtime values are preserved; main/campaign files are byte-identical to their pre-batch snapshot. See `SHARED-EVENTS-BATCH3.md`.

Scope includes Dryad/bear and Unicorn/Undead interactions, Dwarf Beggar, Forest Elf, stolen gold, ghost lights, wagers, monastery, outpost ruins, Prime Source and Undead altar. Terminology: Prime Source＝原初之源, Bartolome＝巴托洛梅 (provisional), Gnomish＝侏儒的. Forest Elf upgrades two Bowmen. Stolen-gold branch awards 1,000 after initial loss of 500; do not call that 1,000 net profit. Source narration/gameplay distinctions for Dryad bear type and Fire Archer progression are documented, not silently rewritten.

All automated checks passed: exact new keys, HTML/variables/engine breaks, XML choice/outcome references, Java decoding, four-style glyph coverage, unchanged older translations and campaign names. Description includes `#3 共享事件`, 5,423 UTF-8 bytes. Backup: `backups/workshop-3840511924-before-shared-batch3-f1b6a75a`. Installed only both shared resources and config; staging hashes match and all other mod files are unchanged. Batches 4–8 and shared 1–3 remain uncommitted/unpublished, `items.xlsx` untouched. Game review is deferred by user request. Continue translation, first remaining travel encounters, then shared locations/side stories and Undead campaign.

## 共享事件 batch 2 (historical, unreleased)

Added 13 event families and 179 keys: 91 in `shared-conversations-2.properties` (37 conversation groups), 88 in `shared-events-2.properties` (44 choices/descriptions). Cumulative: 26 families, 53 standalone groups, 51 choices, 256/3,163 shared content keys (8.1%). Generated shared files have 106 and 154 entries including metadata; all runtime files total 4,495. Remaining shared fallback is 2,907 keys (2,040 level/choice, 867 conversation). Main messages and campaign samples, plus all 81 prior shared entries, are unchanged. See `SHARED-EVENTS-BATCH2.md`.

Events: candles, caravan, crows, dead Hydra, demonic writing/altar, Dwarven runes, lost ghost, Love Potion, mysterious potion, Troll bridge/cook, wounded Ogre. Reviewed actual commands and consistent display names: unit Runemaster＝符文锻造师, distinct from crafting profession 符文大师; reward bansheeancient＝高等报丧女妖; Brute’s Brew＝蛮力药液. Lexa＝莱克莎 is provisional. Generic shops remain outside this batch; some shared-resource events are campaign-restricted.

Build, exact new-key sets, XML references/outcomes (now including random-battle opening conversations), Java decoding, four-style font checks and preservation checks all passed. Description `#2 共享事件` is 5,243 UTF-8 bytes with all campaign names unchanged. Backed up and installed only both shared runtime files and config, verified hashes and every other installed file unchanged. Backup: `backups/workshop-3840511924-before-shared-batch2-0a5ad842`. Batches 4–8 and shared 1–2 remain uncommitted/unpublished; `items.xlsx` remains untouched. No Steam upload. Main 6–8 and shared 1–2 still require in-game review. Next: more complete travel events, then shared locations/side stories, then Undead campaign.

Current machine paths (supersede historical D:\Software paths below): workspace `C:\Users\chenn\OneDrive\Documents\ChatGPT\CD game chinese localization`; game `D:\Steam\steamapps\common\AOFTOTAL`; Workshop item `D:\Steam\steamapps\workshop\content\431520\3840511924`.

## 共享事件 batch 1 (historical, unreleased)

Translated 13 event families, 77 content keys: `shared-conversations-1.properties` has 61 (16 conversation groups); `shared-events-1.properties` has 16 (seven choices/descriptions and the acid-rain battle introduction). The new generated `shared-zh.properties` and `shared-conversations-zh.properties` contain 18 and 63 entries respectively including metadata. Shared coverage: 77/3,163 (2.4%), with 3,086 English fallback keys. All runtime resources total 4,316 entries. Main coverage remains complete; no prior main/campaign values changed. See `SHARED-EVENTS-BATCH1.md`.

Checked the modding guide and installed engine loader: CAMPAIGN=shared prefixes level keys with `shared.`, while standalone conversation IDs share a global namespace; CONVERSATIONS is a marker. Missing translated keys use English fallback. Source archives were scanned for duplicates, and the two English files were matched byte-for-byte against aof-data.zip. The build now generates shared resources, validates full selected families/declared choices, metadata, variables, HTML, =BR= and effective key collisions. `inspection/check_shared_events.py --game ...` verifies actual XML choice references/outcomes and exercises rejection cases. `CheckPilot.java` now accepts multiple English files for fallback font checks.

Validation passed: 4,316 Java-decoded entries, four-style font coverage and 3,086 English shared fallbacks, XML-linked choices, preservation and description checks. Installed only the two new shared files and config; all other installed files remain byte-identical. Backup: `backups/workshop-3840511924-before-shared-batch1-54240407`, including a manifest recording the previously absent shared files. Current description has `#1 共享事件`, is 5,063 UTF-8 bytes and preserves all 32 campaign names. Batches 4–8 plus shared batch 1 remain uncommitted/unpublished. The pre-existing untracked `items.xlsx` was not touched. In-game review is pending. Next: more complete travel events, shared locations/side stories, then Undead campaign.

## 正文 batch 8 (main milestone, unreleased): main messages complete

The user requested completion of the remaining main messages. Added 1,065 keys in `remaining-interface.properties` (165), `remaining-gameplay.properties` (490), `remaining-names.properties` (112) and `remaining-bestiary.properties` (298). All are registered in `build_translation.py`, which now requires exact main-source key coverage. Main totals: 4,221 including six metadata keys; content 4,215/4,215 (100% key coverage); zero main fallbacks; 4,235 total runtime entries. All 326 object descriptions are covered. Glossary: 1,630 unique keyed rows. All 3,156 prior main values and campaign samples are unchanged. See `MAIN-TEXT-BATCH8.md`.

Verified two attribute templates' final parameters are durations and corrected their wording to “持续{2}”. Magic Channel log avoids asserting transfer direction. New labels reuse established terminology and campaign faction names. Number words are translated, but actual engine probes confirm English-style spaces and thousand groups remain (101 → “一 百 一”, 10,000 → “十 千”); idiomatic Chinese grouping needs engine support, not incorrect magnitude translations. No engine binary was changed.

Full validation passed: exact new/main key sets, placeholder counts, HTML, Java decoding of 4,235 entries and font coverage in all four styles, glossary checks, preserved campaign samples and all 32 campaign/expansion names. Current description includes `#8 正文` and is 4,899 UTF-8 bytes. Backed up and installed runtime/config at `backups/workshop-3840511924-before-gameplay-batch8-224ac56d`; installed hashes match staging and all other mod files are unchanged. Batches 4–8 remain uncommitted/unpublished on `codex/gameplay-descriptions`. No Steam upload was performed. User smoke-test feedback covers batch 5 only; batches 6–8 need in-game review. Next are independent shared events, then the Undead campaign; do not claim the entire game is translated.

## 正文 batch 7 (historical, unreleased)

Added `skill-item-effects-3.properties` (297 keys) on the existing working branch, preserving batches 4–6. Current totals: 3,156 main entries including metadata, 3,150/4,215 content entries (74.7%), 1,065 English fallback keys, 3,170 total runtime entries; glossary 1,543 rows. Corrected one existing main value: `COMMAND=统御` in batch 5, aligned with the control effect type and new immunity descriptions. All other previous main values should remain unchanged. MarkOfDeath/MarkOfHunted descriptions follow their actual displayed spell names (痛苦印记/死亡印记), verified from local class methods. See `MAIN-TEXT-BATCH7.md`. No campaign story text changed; remaining effects/help, generated number words and unit descriptions are next. User's positive appearance feedback covers batch 5, not batches 6–7. Workshop description includes `#7 正文`.

Batch 7 validation passed: exact selected keys/placeholders, build/markup/coverage, Java decoding of 3,170 runtime entries and four-style font coverage including 1,065 English fallbacks. All 2,859 prior main keys remain, with only COMMAND changed; campaign samples and all 32 campaign names are preserved. The description is 4,671 UTF-8 bytes. Installed runtime/config after backup at `backups/workshop-3840511924-before-gameplay-batch7-2956908c`; installed hashes match the package and the backed-up runtime matches the pre-batch snapshot. Batches 4–7 remain uncommitted/unpublished. Actual layout of batches 6–7 still needs user review.

## 正文 batch 6 (historical, unreleased)

On `codex/gameplay-descriptions`, added `skill-item-effects-2.properties` (254 keys) and registered it in the build. Current totals: 2,859 main entries including metadata, 2,853/4,215 content entries (67.7%), 1,362 English fallback keys and 2,873 total runtime entries. Preserves batches 4–5, older translations and campaign samples. Scope: summons, transfers, stealth/burrowing, traps, weather, action restrictions, immunities and two help dialogs. See `MAIN-TEXT-BATCH6.md` for mechanics and remaining generated-number limitations. Public Workshop headings now use `#4 正文`, `#5 正文` and `#6 正文`. New batch 6 content still needs user layout testing; prior pending statements for batch 5 are superseded by the user's normal-appearance report above.

Batch 6 validation passed: exact 254-key set/placeholders, build/HTML/coverage, Java decoding of 2,873 entries and four-style font coverage including 1,362 English fallbacks. All 2,605 prior main values, campaign samples and 32 campaign/expansion names are unchanged. Description is 4,560 UTF-8 bytes. Installed runtime/config after backup at `backups/workshop-3840511924-before-gameplay-batch6-d0eab54f`; installed hashes match the package and other mod files are unchanged. Batches 4–6 remain uncommitted/unpublished.

## 正文说明 batch 5 (historical, unreleased)

Continued on `codex/gameplay-descriptions`, preserving uncommitted batch 4. Added `combat-tutorials.properties` (20) and `skill-item-effects.properties` (189), both registered in the build. Added 209 keys; current totals are 2,605 main entries including six metadata keys, 2,599/4,215 content entries (61.7%), 1,616 English fallback keys and 2,619 entries across runtime files. Glossary has 1,529 keyed rows. All `BATTLE_TUTORIAL_` and `WORLDMAP_TUTORIAL_` keys are covered, but other help dialogs and many detailed effects remain. Campaign story/shared event content remains unchanged. See `MAIN-TEXT-BATCH5.md` for scope, dynamic-argument checks and Parry/Riposte wording. Next: remaining effects, help and unit descriptions before shared events and the Undead campaign. Workshop description now includes `#5 正文说明`.

Batch 5 validation passed: exact selected keys/placeholders, build/HTML, all 21 named tutorial keys, Java decoding of 2,619 runtime entries and four-style glyph coverage including 1,616 English fallbacks. All 2,396 prior main values, campaign samples and all 32 campaign/expansion names were preserved. Description is 4,430 UTF-8 bytes. Installed runtime/config after backup at `backups/workshop-3840511924-before-gameplay-batch5-1f486da2`; hashes match the package and other mod files are unchanged. Batches 4 and 5 remain uncommitted/unpublished. Actual layout is still pending.

## 正文说明 batch 4 (historical, unreleased)

After PR #1 was merged into main, the user asked to continue translation. Working branch: `codex/gameplay-descriptions`. Added 164 entries in `translation/gameplay-descriptions.properties` and registered them in the build. Coverage: 2,396 main entries including metadata, 2,390/4,215 content entries (56.7%), 1,825 main fallbacks; 2,410 entries across all runtime files. Scope: shared environmental/equipment/crafting/recruitment/trait/morale descriptions and effect rules, plus objective markers. Existing translations and campaign samples are preserved. See `MAIN-TEXT-BATCH4.md` for source ambiguities and test scope. Next: detailed effect fragments, combat tutorials and unit descriptions, before shared events and the Undead campaign. The Workshop description now includes `#4 正文说明`; the prior description byte counts above are historical.

Batch 4 validation passed: build/HTML/placeholders; Java decoding and four-style font coverage for 2,410 entries plus 1,825 English fallbacks; all 2,232 prior main values unchanged; all 32 campaign/expansion names retained. Description is 4,296 UTF-8 bytes. Installed main runtime and config locally after a verified backup at `backups/workshop-3840511924-before-gameplay-batch4-f40a5a9d`; installed SHA-256 hashes match the package and other mod files are unchanged. In-game layout is still pending. Batch 4 is uncommitted and unpublished.

## Terminology batch 3 (historical, unreleased)

Added `item-name-terms.properties` (449 entries) and `skill-attribute-terms.properties` (578 entries): 1,027 new main keys. Total main entries: 2,232 including six metadata keys; content coverage 2,226/4,215 (52.8%), with 1,989 remaining. All runtime files together: 2,246 entries. Existing 1,205 deployed main values are preserved; campaign samples unchanged. Glossary: 1,528 keys.

Completed source blocks: ACIDBLOOD..ANCIENTCOAL_ITEM (937 keys: 399 item names/templates, 538 other labels); LIVERWORM_ITEM..WHITEYARROW_ITEM (51 materials); CRAFTINGBLACKSMITH..CRAFTINGJEWELER (9 professions); all 30 GROUP_SET_ labels. The correct item/resource name/template count is 450; earlier 455 counts included five UI prompts whose keys also end in `_ITEM`. Do not claim 450 distinct physical items or full effect-description coverage. See `MAIN-TEXT-BATCH3.md` for decisions, validation and next tests.

Source display names take precedence over IDs: HEADHUNTER=Executioner, CRITICALHIT=Precision, STEALTHATTACK=Infravision. Regrowth is 复生 (post-battle recovery), distinct from Regeneration/再生 and Resurrection/复活术. Shitanto is a two-handed item, provisionally 希坦刀, not 短刀. Slow has separate UI-speed and spell meanings; Elemental has separate creature and set-name meanings. Next work: gameplay effect descriptions, item/skill tooltips, remaining bestiary descriptions and tutorials; keep the same font and validate engine symbols as before.

## Terminology batch 2 (historical, unreleased)

Added `unit-race-terms.properties` (368 entries: 298 names and 70 race labels) and `battlefield-terms.properties` (28 entries), both registered in the build. All 326 unit/scenery name keys and the 73-label base race/group section are covered. Main runtime: 1,205 keys including six metadata keys; 3,016 keys still use English fallback. All three runtime files: 1,219 entries. Object descriptions remain at 28/326. The glossary now has 501 keyed entries; item and skill terminology remains incomplete. Campaign source/runtime samples are unchanged.

All four font settings use `noto-sans-sc.ttf`, prepared from the local `NotoSansSC-VF.ttf` with `prepare_font.py` (fontTools, regular weight 400, no variable axes). Direct use of the variable font rendered too thin in Java. Font binaries remain ignored. `setup_local.py --font` now calls this preparation helper; packaging checks the configured font filenames. `CheckPilot.java package-root source/aof/messages-en.properties` checks four font styles, engine NBSP/bullet, all translated entries and remaining English main entries. Legacy SimHei failed as expected; the static replacement passes. `RenderFontSample.java` creates a headless Swing HTML sample, not an in-game screenshot. Do not claim complete layout validation.

See `MAIN-TEXT-BATCH2.md` for terminology decisions and test checklist. These totals and font instructions supersede the historical SimHei/503-entry/823-entry notes below.

## Main-text continuation (unreleased)

The first new batch, completed while campaigns were deferred, adds 320 entries across `translation/gameplay-basics.properties`, `translation/bestiary-basics.properties` and `translation/combat-log-basics.properties`. `build_translation.py` registers these files and reports their counts separately from the original 481 Phase 1 entries. Runtime totals are now 809 main-text entries (including metadata) and 823 entries across all three runtime files; 3,412 of the current main source's 4,221 keys remain untranslated.

See `MAIN-TEXT-NOTES.md` for scope, terminology and the test checklist. The user supplied screenshots confirming Chinese labels in the status monitor, story-screen buttons and bestiary; those screenshots predate this batch and do not validate its layout. Preserve the existing campaign samples. Focus subsequent batches on remaining unit, skill, item, tutorial and combat text in `messages-en.properties`. The historical counts and continuation order below are superseded by this update.

## Repository handoff update (0.1.0)

The public collaboration repository is https://github.com/Polar-Slater/AoF_total-chinese-localization. Follow README.md for current fresh-checkout instructions and CONTRIBUTING.md for branches and pull requests. VERSION and CHANGELOG.md track translation milestones.

The sections below describe the original local workspace. Git intentionally excludes source/, the game guide, bytecode dumps, fonts, workshop-package/, backups/, pilot-home/ and the generated launcher. Use setup_local.py with your own game installation to regenerate English references and optionally supply your own local test font. The tracked pilot-mod/ runtime translation files remain packaging inputs. Do not upload excluded third-party materials as part of a handoff.

prepare_workshop.py now requires --item and --owner-id, checked against the existing item's config.xml before staging. update-workshop-description.ps1 now requires -ItemConfig and -OwnerId. These replace the hardcoded Workshop targets described below. Original-machine paths are historical context, not required destinations. The historical prepare_pilot.py still has original-machine paths; do not use it for fresh-checkout setup.

## Objective and current milestone

Create a complete Simplified Chinese localization of **Age of Fear: Total**, usable through its **Workshop Manager**. The installed version shown in the user's screenshots is **v11.0.5**. The supplied modding guide is **v10.6.9**, so verify behavior against the installed game when the guide is unclear.

Completed: a working Chinese-font pilot and the first interface translation batch. Do not start over or replace the existing translations with the older third-party mod.

- Phase 1 contains **481 translated entries**: menus, common buttons/tabs, settings and tooltips, battle controls and shortcut/touch help, save/load confirmations, difficulty selection, and multiplayer setup.
- Coverage checks include all **135 entries** in the main button/tab block and **197 entries** in the main settings block of the extracted English file. These are source-block coverage counts, not proof that every interface string in the game is translated.
- Built UI file: **489 entries including metadata and retained pilot entries**. All three runtime translation files together: **503 entries**.
- Small Undead campaign and conversation samples are retained. Most stories, tutorials, unit/item/skill descriptions and detailed combat logs still fall back to English.
- The user confirmed the pilot worked in game and supplied screenshots of Chinese battle menus. A later screenshot shows Chinese main-menu buttons. Full Phase 1 layout testing, especially settings tooltips and multiplayer dialogs, remains incomplete.
- All files were installed locally. This assistant has **not uploaded or published** the mod to Steam.

## Current machine and Workshop identity

| Purpose | Current value |
|---|---|
| Project | `D:\Documents\ChatGPT\AoF_Total Chinese Translation` |
| Installed game | `D:\Software\Steam\steamapps\common\AOFTOTAL` |
| Active Workshop item | `3840511924` |
| Active item directory | `D:\Software\Steam\steamapps\workshop\content\431520\3840511924` |
| Steam app ID shown by Workshop Manager | `431520` |
| Current item's owner-user-id | `201037459` |
| Mod title | `Age of Fear Total - Simplified Chinese (Test)` |
| Language selector label | `Chinese (Simplified) - Test` |
| Locale | `zh` |

`3732397478` is the previous item and is no longer the deployment target. The user created a new item and relocated the mod; project scripts were updated accordingly.

On another computer, inspect the new installation and Workshop item first. Update hardcoded paths and owner checks in the scripts to match the actual user's item. Preserve the owner ID generated by Workshop Manager; do not copy the original user's identity into somebody else's item. A new collaborator may need to create their own Workshop item.

## Files and sources of truth

| Path | Role |
|---|---|
| `translation/messages-zh.properties` | Editable UTF-8 baseline UI pilot and language/font metadata. |
| `translation/ui-phase1.properties` | Editable menu/buttons/settings-label/battle-control translations. |
| `translation/settings-tooltips.properties` | Editable settings explanations. |
| `translation/menu-dialogs.properties` | Editable dialogs, difficulty, multiplayer and touch-control help. |
| `translation/undeadcampaign-zh.properties` | Editable pilot campaign sample. |
| `translation/undeadcampaign-conversations-zh.properties` | Editable pilot conversation sample. |
| `source/` | 62 original English resource files, separated by archive; keep unchanged. |
| `source/manifest.json` | Archive origins, resource paths, byte lengths and SHA-256 hashes. Paths reference the original machine. |
| `pilot-mod/` | Runtime resource tree, font and generated ASCII properties; build staging despite its historical name. |
| `workshop-package/` | Installable package: `com/`, `config.xml`, `preview.jpg`. |
| `workshop-assets/description.txt` | Editable UTF-8 Workshop description. |
| `workshop-assets/preview.png` | User-selected main-menu screenshot. Preserve this preview choice. |
| `inspection/CheckPilot.java` | Java properties decoding and font-glyph verification. |
| `inspection/phase1-validation.json` | Latest build validation summary. |
| `inspection/*-bytecode.txt` | Read-only inspection evidence from bundled Java `javap`. |
| `PHASE1-NOTES.md` | First milestone scope, testing and initial glossary. |
| `AOFModdingGuide.pdf` | Localization chapter: pages 56–58; local resource lookup: page 10. |

`README-CHINESE-TEST.md` contains historical pilot notes beneath its current-status notice. Some old counts and test descriptions there are superseded by this handoff and `PHASE1-NOTES.md`.

## What was learned about localization

1. UI text comes from `aof.jar` at `com/aof/resource/text/i18n/messages-en.properties`. Shared text is in `aof-data.zip`; campaign resources are in `data/*.zip`.
2. Inspection of this build confirmed `I18nMessagesFactory` uses `java.util.Properties.load(InputStream)`. Editable translations are UTF-8, but runtime files must use **ASCII with Java `\uXXXX` escapes** for non-ASCII text. Do not write raw UTF-8 Chinese into runtime properties files.
3. `LOCALE=zh` works. System-language detection uses `Locale.getLanguage()`, so separate Simplified/Traditional automatic detection has not been implemented.
4. Keep `LANGUAGE=Chinese (Simplified) - Test` in ASCII. The original Chinese language label appeared as squares before switching languages because the current English font could not render it. Using an English label fixed selection; Chinese then rendered correctly.
5. Fonts are resource filenames, not Windows font-family names. All four font fields currently use `simhei.ttf`, loaded from `com/aof/resource/text/font/` via `Font.createFont`.
6. `simhei.ttf` was copied from this PC's Windows fonts for **local testing only**. Before redistribution/publication, choose a suitable redistributable Chinese font, include its license, update all four font fields, and recheck glyphs/layout. Do not assume the bundled test font may be published.
7. Missing translation keys fall back to English. Keep partial batches genuinely partial rather than copying English values and counting them as translated.
8. Keep keys, placeholders such as `{0}`, and functional HTML intact. Repair demonstrably malformed source markup carefully; first-run, restart and smart-camera messages already needed repairs.

## Build and install workflow

Python requires Pillow for packaging. The original machine's working interpreter was:

`C:\Users\chenx\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe`

Use an available Python interpreter on the receiving computer; `python` on the original machine resolved to an unusable Windows Store alias.

From the project directory:

```powershell
python build_translation.py
python prepare_workshop.py
& 'D:\Software\Steam\steamapps\common\AOFTOTAL\jre\windows64\bin\java.exe' '-Djava.awt.headless=true' inspection/CheckPilot.java workshop-package
```

Adjust the Java path on another computer. The game bundles Java 17 and `javap`.

- `build_translation.py` merges the baseline with the three named Phase 1 files; batch entries override baseline entries. It validates duplicates, source-key existence, placeholder multiplicity, balanced HTML, and coverage of the button/settings source blocks, then writes the runtime UI file. New batch files must be added to its input list.
- Coverage ranges currently use line positions in the preserved English snapshot. When refreshing English sources, replace or review these ranges; do not silently treat them as version-independent coverage.
- The parser supports the project's one-line `key=value` format, not arbitrary Java-properties syntax. Do not introduce multiline continuations without updating the parser.
- `prepare_workshop.py` invokes the UI build, copies `pilot-mod` into `workshop-package`, reads title/tags/owner from the installed item's `config.xml`, and sets the description from `workshop-assets/description.txt`. It converts the user's full screenshot to JPEG without cropping. It **requires an existing local Workshop item** and correct owner check.
- `prepare_workshop.py` does **not** copy the result into Steam's item folder or upload it. Back up the current target before installing. Compare installed files with the package afterwards. Copying uses merge semantics; stale resources are not automatically removed. Inspect before removing obsolete files.
- `prepare_pilot.py` is the original extraction/pilot bootstrap. It preserves existing editable baseline files but regenerates pilot runtime resources and the test launcher. Run the current build afterwards. It still contains embedded pilot translations and machine-specific paths; **do not use it as the primary translation editor**.
- **Campaign build limitation:** `build_translation.py` currently builds only the UI file. Campaign/conversation runtime files are generated by `prepare_pilot.py` for the pilot. Extend the build to validate and encode campaign files before substantial campaign translation; merely editing their UTF-8 sources and running `prepare_workshop.py` does not rebuild them.
- `update-workshop-description.ps1` reads the editable description, validates length, backs up the installed config, and updates local installed/package metadata. It does not upload. Its item path and owner check must be adapted on another machine.

The normal testing route is now **Workshop Manager + launching through Steam**, rather than the historical standalone pilot launcher. The latter uses a separate `pilot-home`; normal game saves were not intentionally changed. An early launcher bug involved case-sensitive replacement of `%~DP0` and was fixed using case-insensitive replacement. Keep the JVM `-Dgame.home=...` argument before `com.aof.Game`.

## Validation and unresolved issues

- The latest Phase 1 build checks passed; the game's bundled Java decoded all 503 package entries, and the local font covered every translated character.
- Deployed package contents were compared byte-for-byte after installation. The user-selected screenshot later replaced the generated preview; its JPEG is **986 × 761** pixels.
- Workshop validation previously reported: `Could not load conversations [UXX_Please_review_us]`. Its cause has **not** been established or fixed. Do not claim Workshop validation is clean. Investigate whether the reference comes from base game resources or another loaded mod before changing anything.
- English proxy username/password labels appear swapped. Translation currently preserves English displayed semantics pending call-site/UI verification.
- The English AI-during-animation label and tooltip contradict one another. Translation preserves this ambiguity pending behavioral verification.
- Automated glyph checks do not prove dialogs fit. Check every settings tab, long tooltip, battle menu, F1 help, difficulty screen and multiplayer setup in-game.
- Inspect current files/logs before assuming the state is unchanged since this document was written.

## Third-party example

The user supplied `D:\Software\Steam\steamapps\workshop\content\431520\2989258288`, titled **Chinese localization MOD**, as an incomplete example. It uses `LOCALE=CN`, the selector name `Chinese`, a `guifont.ttf`, and 19 translation files. It was inspected to understand packaging and the ASCII selector label. Its translation was **not merged into this project**. Do not claim authorship or redistribution permission for that mod's text/font. Our `zh` locale and its `cn` locale are separate choices.

## Recommended continuation

1. Review Phase 1 in-game, correct awkward terminology or clipping, and diagnose the existing validation warning.
2. Establish consistent terminology for stats, races, units, items, skills and status effects. Start from the glossary in `PHASE1-NOTES.md`.
3. Translate gameplay descriptions/tooltips in `messages-en.properties` using that glossary.
4. Translate shared events/conversations, then campaign stories/dialogue, starting with the Undead campaign used for testing.
5. Reconcile duplicate source filenames across archives using actual resource precedence before producing complete campaign bundles. Do not flatten `source/` blindly.
6. Keep the user's screenshot preview and editable description. Update milestone notes and coverage counts after each validated batch. Publish only when the user requests it and release assets are ready.

## Handoff packaging

Include this file, all editable translations, `source/`, build scripts, `pilot-mod/`, `workshop-package/`, `workshop-assets/`, `inspection/`, guide and notes. `pilot-mod/` is currently a packaging input and must not be omitted unless the build is refactored to recreate it. `.git`, `backups/` and `pilot-home/` are not needed for a basic handoff; game binaries and personal saves are unnecessary.
