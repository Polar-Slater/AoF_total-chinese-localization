# Changelog

Project versions describe translation milestones, not game versions.

## [Unreleased]

### Workspace cleanup
- Removed the obsolete pilot bootstrap, standalone launcher and pilot home. Current setup remains setup_local.py, followed by build_translation.py and optional Workshop packaging.
- Removed disposable Workshop staging after verifying every file was an exact duplicate of the installed mod, reclaiming approximately 11.4 MB. Moved the original font ZIP under source/reference/ without changing it.
- With explicit user approval, removed 25 superseded backup/helper items, reclaiming another 79.6 MB. Retained the latest full rollback backup and active campaign batch recovery snapshot; hash checks verified all 81 protected translation, runtime, asset and retained-backup files unchanged.
- Preserved uncommitted campaign work, runtime/font/license inputs, original archive-separated English references and batch history. The installed game mod is unaffected.

### Undead campaign: Kingdom Patrol
- Added 45 content entries: Level15/Level16/Level17 and the immediate LevelSecret01b defeat-route continuation (15), all three U05 groups (26), UXX_Vision_1a (2) and UXX_Krill_wight (2). Campaign coverage is 251/732 (34.3%).
- Checked the textless Level15b shop, battle-board dialogue references, inclusive turn-12 reward condition, victory and defeat routes, conditional vision, and reused bone-dragon departure dialogue. Downstream branches remain outside this batch.
- Build, source-HTML comparisons, prior-translation preservation and Java four-style font checks passed: 6,678 runtime entries and 1,446 English fallback entries. Main/shared translation and runtime files remain unchanged.
- Updated progress, glossary, coverage reports and the spoiler-free description count. This batch is not installed, committed, pushed or uploaded; in-game review remains deferred. See docs/batches/UNDEAD-CAMPAIGN-BATCH5.md.

### Google Fonts Noto Sans SC package
- Prepared the supplied static Regular font without altering its bytes, retaining the existing runtime filename. Included the matching OFL copyright/license and a provenance notice in build staging and the Workshop package.
- Moved obsolete local SimHei test fonts out of staging into a backup, and excluded the downloaded ZIP from Git. Java decoding and four-style glyph checks passed for 6,633 runtime entries and 1,491 English fallback entries.
- Installed the new static font, OFL license and provenance notice into the local Workshop mod at the user's request, after a verified full backup. Removed the unused installed SimHei font; hash checks confirmed all other files unchanged. Java checks passed against the installed folder. No Steam upload.

### Concise, spoiler-free Workshop description
- Replaced detailed event and campaign summaries with category-level progress counts; removed story, recruitment, reward and location details while preserving bilingual campaign names and setup instructions.
- Added a spoiler-free description rule to project instructions. Updated local installed and staged descriptions with metadata backups; no Steam upload.

### Local Workshop sync through Undead batch 4
- Installed the two campaign resources and updated description at the user's request. Installed content now includes 2,198 shared and 206 Undead content entries, with 6,633 total runtime entries.
- Verified a full backup, staged Java decoding and four-style font coverage, and SHA-256 matches after installation. All other installed files, including shared resources, main messages, font, preview and non-description ownership metadata, were preserved.
- Installed description is 4,970 UTF-8 bytes after newline normalization and trimming. No Steam upload or new in-game test; earlier batch notes retain their historical pre-installation state.

### Merge parallel shared and campaign work
- Combined shared batches through 17 (2,198/3,163 content entries) with Undead batches through 4 (206/732), preserving both workstreams' editable translations and runtime resources.
- Resolved progress, batch-index and testing-history conflicts per resource section; retained both changelog histories. Replaced chat-relative assignments with neutral workstream instructions and documented the merge rules in CONTRIBUTING.md.
- Rebuilt reports and validated 6,633 runtime entries plus 1,491 English fallback entries in four font styles. Installation history remains separate; this merge does not install or upload the combined package.

### Undead campaign: Haunted Church
- Added 89 content entries: Level11b/Level13 (27), both U04 dialogue groups (22), and five linked UXX groups (40). Campaign coverage is 206/732 (28.1%).
- Checked the textless Level12 shop, Noea's recruitment, both reward conditions, serialized battle-board dialogue references and the base unlock. Included the bone dragon's later Level16 departure dialogue without counting that level as translated; base-upgrade campaign dialogue remains pending.
- Build and Java decoding/four-style font checks passed: 6,017 runtime entries and 2,107 English fallback entries. All previous translations, including uncommitted batches 2–3, preserved; main/shared translation and runtime files unchanged. New entries preserve source HTML tag structure.
- Updated glossary, coverage/progress records and local Workshop description. No installation, upload, commit or push; in-game layout testing remains deferred. See docs/batches/UNDEAD-CAMPAIGN-BATCH4.md.

### Undead campaign: Night Assault
- Added 22 content entries: Level09–Level11 (18) and both U03 dialogue groups (4). Campaign coverage is 117/732 (16.0%).
- Checked the Level09b shop, battle-board dialogue references, all three reward conditions and the route to Haunted Church. Turn limits follow the inclusive script conditions; existing recurring dialogue is reused.
- Build, Java decoding and four font-style checks passed: 5,928 runtime entries and 2,196 English fallback entries. All previous translations, including uncommitted batch 2, preserved; main/shared translation and runtime files unchanged.
- Updated local coverage/progress records. No installation, upload, commit or push; in-game layout testing remains deferred. See docs/batches/UNDEAD-CAMPAIGN-BATCH3.md.

### Undead campaign: Bone River / Mistmill
- Added 50 content entries: Level05–Level07 (14), all six U02 dialogue groups (26), and three linked UXX groups (10). Campaign coverage is 95/732 (13.0%).
- Checked the legacy Level04 shop, current Level05b shop, battle-board dialogue references, reward condition and post-battle vision against local game resources. The objective wording reflects the script’s inclusive turn-10 limit.
- Build and Java properties/font checks passed: 5,906 runtime entries and 2,218 English fallback entries. Previous translations preserved; main/shared resources unchanged.
- Updated coverage reports and local progress documentation. No installation, upload, commit or push; in-game layout review remains deferred. See docs/batches/UNDEAD-CAMPAIGN-BATCH2.md.

### Local Workshop sync through shared batch 17
- Installed shared batches 13–17 and the latest description at the user’s request. The local mod now contains 6,472 runtime entries, including 2,198 shared content keys and the existing 45 Undead content keys.
- Updated only the two shared properties files and `config.xml`. Full backup and SHA-256 checks passed; all other files and ownership metadata remain unchanged. The installed description is 4,911 UTF-8 bytes after newline normalization and trimming.
- No Steam upload, Git publication or new in-game test. Earlier batch validation reports record their pre-installation state.

### 通用事件与通用对话 batch 17 (2026-11-16)
- Added 24 keys for the Crystal Mine and Cursed Wights: 14 conversation keys and 10 location/choice keys. Shared coverage reaches 2,198/3,163 (69.5%); conversation coverage is 990/1,019 (97.2%).
- Followed the mine battle and daily income branches, plus the hidden Cursed Sword encounter trigger and Wight battle rewards. Included textless levels in XML checks without inventing resource keys or modifying scripts.
- Updated description, terminology and progress records. Existing translations and campaign resources remain unchanged; shared batches 13–17 remain uninstalled and unpublished. See `docs/batches/SHARED-EVENTS-BATCH17.md`.

### 通用事件与通用对话 batch 16 (2026-11-16)
- Added 105 keys for the Pearl Mermaid and Shaman’s Hut: 18 conversation keys and 87 location/choice keys. Shared coverage reaches 2,174/3,163 (68.7%); conversation coverage is 976/1,019 (95.8%).
- Checked daily pearl trading, the one-time Black Pearl reward, and all 36 hero cleansing menus and their 200-gold costs. Recorded the existing hero-107/hero-17 mismatch in the original `on-select-42` command; preserved source placeholders and scripts.
- Updated description, terminology and progress records. Prior translations and campaign resources remain unchanged; shared batches 13–16 are uninstalled and unpublished. See `docs/batches/SHARED-EVENTS-BATCH16.md`.

### 通用事件与通用对话 batch 15 (2026-11-16)
- Added 53 keys for the Tranquil Grove and Well of Souls: 8 conversation keys and 45 location/choice keys. Shared coverage reaches 2,069/3,163 (65.4%); conversation coverage is 958/1,019 (94.0%).
- Checked four seedling costs and progress-dependent unit rewards, plus nine sacrifice choices, cancellation guards, separate one-time flags and item rewards. Recorded two external campaign dialogue dependencies and an existing duplicated dialogue command in the Dwarf sacrifice branch.
- Updated the description and progress records while preserving prior translations and campaign resources. Shared batches 13–15 remain uninstalled; no publication or new game test. See `docs/batches/SHARED-EVENTS-BATCH15.md`.

### 通用事件与通用对话 batch 14 (2026-11-16)
- Added 12 keys for the three Magic Sources and the World Tree: 4 conversation keys and 8 location keys. Shared coverage reaches 2,016/3,163 (63.7%); conversation coverage is 950/1,019 (93.2%).
- Checked independent daily shard availability and the World Tree’s conditional one-apple reward against active XML commands. Preserved the exploration narrative and existing item terminology.
- Updated the description and progress records. Campaign resources remain unchanged; batches 13–14 are not installed or published. See `docs/batches/SHARED-EVENTS-BATCH14.md`.

### 通用事件与通用对话 batch 13 (2026-11-16)
- Added 45 keys for the Moon Well and Mana Obelisks: 8 conversation keys and 37 location/choice keys. Shared coverage reaches 2,004/3,163 (63.4%); conversation coverage is 946/1,019 (92.8%).
- Verified all seven offering costs and per-unit experience rewards. Distinguished the obelisk’s seven-shard entry threshold from its removal of up to 999 shards; recorded inconsistencies in the original obelisk narration.
- Updated file-based description and progress records, preserving prior translations and campaign resources. Batch 13 is built and validated but not installed or published; the installed mod remains at shared batch 12.
- See `docs/batches/SHARED-EVENTS-BATCH13.md`.

### Local Workshop sync through shared batch 12
- Installed the two shared resources, the existing two Undead opening resources and the updated description at the user’s request. Local package now contains 6,233 runtime entries, including 1,959 shared content keys and 45 Undead content keys.
- Full mod backup and SHA-256 verification passed; all other mod files and ownership metadata were preserved. Description is 4,563 UTF-8 bytes and matches the project source. No Steam upload or new in-game test.
- Earlier batch notes record their pre-installation state.

### 通用事件与通用对话 batch 12
- Added 89 keys for the Runesmith and Transmuter's Laboratory: 28 conversation keys and 61 location/choice keys. Shared coverage is 1,959/3,163 (61.9%); conversation coverage is 938/1,019 (92.1%).
- Matched equipment names, prices and materials to the scripts. Corrected the source helmet menu from 500 to the actual 400 gold cost and its tooltip input from armour to helmet; clarified the shared daily transmutation limit and Talnes's permanent departure.
- Updated file-based Workshop progress, terminology and batch notes. Campaign resources and previous translations remain unchanged; no game test, local Workshop installation, Steam upload or Git publication.
- See `docs/batches/SHARED-EVENTS-BATCH12.md`.

### 通用事件与通用对话 batch 11
- Added 43 keys for Demon City: 31 conversation keys and 12 location/choice keys, covering discovery, entry, pact negotiation and post-pact recruitment. Shared coverage reaches 1,870/3,163 (59.1%); conversation coverage is 910/1,019 (89.3%).
- Kept the permanent base-HP cost explicit and distinguished postponing from rejecting the pact. Recorded the separate Chaos campaign entry conversation as an untranslated campaign dependency.
- Updated terminology, file-based Workshop progress and batch notes. Previous translations and campaign files are preserved; no game test, local Workshop installation, Steam upload or Git publication.
- See `docs/batches/SHARED-EVENTS-BATCH11.md`.

### 通用事件与通用对话 batch 10
- Added the complete Dark Castle dinner quest: 76 keys across eight conversation groups plus 13 location/choice keys, totaling 89. Shared coverage is 1,827/3,163 (57.8%); conversation coverage reaches 879/1,019 (86.3%).
- Covered arrival, three delivery stages, menu reminders and departure, preserving the dark comedy and bilingual location name. Verified manual-selection callbacks and cancellation guards against the game XML.
- Updated terminology, file-based Workshop progress and batch documentation. Prior translations and campaign files are preserved; no game test, local Workshop installation, Steam upload or Git publication.
- See `docs/batches/SHARED-EVENTS-BATCH10.md`.

### 通用事件与通用对话 batch 9
- Added 74 keys for the Black Dragon prerequisite encounter and Darius’s recruitment, letter, tower rescue and ending: 41 conversation keys plus 33 shared-level keys. Shared coverage reaches 1,738/3,163 (54.9%); conversation coverage is 803/1,019 (78.8%).
- Preserved bilingual map labels and the bard’s theatrical voice. Declared textless shop/battle intermediates and extended XML checks through story entry/exit and battle-result triggers.
- Updated the file-based Workshop description and progress documents. Prior translations and campaign files are preserved. No game test, local Workshop installation, Steam upload or Git publication for this batch.
- See `docs/batches/SHARED-EVENTS-BATCH9.md`.

### 通用事件与通用对话 batch 8
- Added the complete Djinn wish and Beastmaster Tayah event families: 63 conversation keys and 19 linked choices/follow-up keys, including the petrification ending and battle introduction. Shared coverage is 1,664/3,163 (52.6%); conversation coverage is 762/1,019 (74.8%).
- Extended follow-up validation to conversations queued on the world map after battle, including Tayah’s recruitment offer. Preserved prior shared translations and all campaign resources.
- Updated file-based Workshop progress and collaboration scope: this chat handles shared resources; the user’s friend handles campaigns. No game test, local Workshop installation, Steam upload or Git publication for this batch.
- See `docs/batches/SHARED-EVENTS-BATCH8.md`.

### Documentation layout
- Simplified the main README and replaced the old pilot README with current setup and testing guides.
- Grouped the plan, glossary and batch notes under docs/; added a documentation index and updated references.
- Moved the local modding guide into ignored source/reference/. Build scripts and translation resource paths are unchanged.


### Project instructions and privacy
- Consolidated current agent instructions into AGENTS.md and removed the historical handoff file. Updated documentation references.
- Removed personal account/item identifiers and installation-specific paths from tracked documentation; setup examples use placeholders. Historical backup paths are omitted.
- The legacy pilot bootstrap now requires an explicit --game argument instead of a machine-specific installation path.


### Undead campaign opening and work split
- Assigned shared events/conversations to the user's friend; campaign stories are now our active work. Renamed Chinese labels to 通用事件 / 通用对话 while preserving technical names.
- Added 35 opening story/dialogue entries; Undead coverage is 45/732 (6.1%), excluding metadata. Existing sample translations preserved.
- Added declared campaign coverage and source/placeholder/HTML/namespace checks to the build; both campaign runtime files now regenerate. Total runtime entries: 5,856.
- Updated editable Workshop description and progress documentation. No installation or upload; game layout review pending.


### Description helper review
- Added `-WhatIf` support and a missing-description check; prepare output directories before updating installed metadata.
- Back up both existing configs and restore them on save failure. Document explicit item/owner arguments.
- Tested Windows PowerShell with isolated fixtures: Chinese/Steam markup/XML round trip, wrong owner, oversized UTF-8 description, no-write dry run, missing package folder and repeated updates. Checked the actual target with `-WhatIf` only; no installed metadata changed.

### 创意工坊简介：按文件展示进度
- Replaced batch history in 总体进度 with the main message file and two shared resource files, including source/Chinese filenames, scope and per-file counts. Shared total remains 50.0%.
- Preserved all campaign sections and names. Description is 4,699 UTF-8 bytes; backed up and synced to local/staged config, with all other metadata and mod files unchanged. No Steam upload.

### 共享地点与玩法 batches 6–7 — shared text 50%
- Added 680 content keys: eight faction bases (363), systems/choices (110) and conversations (207). Cumulative shared coverage is 1,582/3,163 (50.0%); all runtime files contain 5,821 entries.
- Includes desertion, cards, cups, dice, fishing, roulette, Windmill, weather invocations and common prompts. Preserved established terminology and bilingual place names; checked fishing and card rules against scripts.
- Extended branch checks across the game's data archives, recording 22 referenced campaign-resource conversations outside shared coverage and remaining script-supplied English fragments.
- Updated the description to 6,164 UTF-8 bytes without changing campaign names. Previous batch 5 was uploaded and tested successfully by the user. New batches have automated validation and local installation only; no new Steam upload or game test.
- See `docs/batches/SHARED-TEXT-50-PERCENT.md` for scope, validation and installation details.

### 通用事件 batch 5 — global-event text milestone
- Added 264 keys across the remaining 40 SGE travel-event families and the gambler event. Cumulative shared coverage: 902/3,163 (28.5%); 5,141 runtime entries.
- Completed all 487 `SGE_` conversation keys and 410 `LevelGlobalEvent*` keys. Shared locations, generic shops and longer side stories remain pending.
- Preserved natural phrasing and bilingual place names; documented the Drunken Dwarf source probability mismatch. Extended branch checking to recursive trigger callbacks and explicitly declared battles with no text.
- Passed source, build, XML, decoding, font and preservation checks. Updated `#5 通用事件` description (5,776 UTF-8 bytes), preserved campaign names, backed up and installed two shared files plus config with hash verification. Game tests remain deferred; no publication.

### 地名格式
- Adopted the user's `中文名 (English)` convention for place names. Updated 三魔峰 (Three Devils) and 冰原 (Iceland) in the shared volcanic-event narration and recorded the rule for future translation.

### 通用事件 batch 4
- Added 156 content keys in 31 event families: 122 conversation keys and 34 choice/follow-up keys. Shared coverage reaches 638/3,163 (20.2%); 4,877 total runtime entries.
- Translated knight rivalry, Vampire/Werewolf dialogue, Orc encounters, Blademaster training and short travel events. Preserved the user's approved natural wording for the batch-3 beggar option and recorded new provisional names.
- Extended XML checking through the Orc feast's manual-unit-selection callback. Passed text, branch, Java decoding, font and preservation checks.
- Updated `#4 通用事件` description (5,578 UTF-8 bytes), preserving campaign names. Backed up and installed two shared resources plus config with hash verification. Game testing remains deferred; no Git or Steam publication.

### 通用事件 batch 3
- Added 226 content keys in 20 event families: 142 conversation keys and 84 choice/follow-up keys. Shared coverage reaches 482/3,163 (15.2%); 4,721 total runtime entries.
- Includes recruitment encounters, Dryad/bear and Unicorn/Undead interactions, stolen gold, archery wagers, old monastery, Prime Source and Undead altar. Preserves linked choices and battle introductions, source costs and established unit/item terminology.
- Passed text, XML branch, Java decoding, four-style font and preservation checks. Updated `#3 通用事件` description to 5,423 UTF-8 bytes with campaign names intact; backed up and installed two shared resources plus config with hash verification.
- User requested prioritizing translation and deferring in-game testing. No game test, Git publication or Steam upload was performed.

### 通用事件 batch 2
- Added 179 content keys across 13 travel-event families: 91 conversation keys and 88 linked choice/description keys. Cumulative shared coverage is 256/3,163 (8.1%), with 4,495 total runtime entries.
- Included caravan encounters, candles, crows, Dwarven runes, ghosts, potions, Troll encounters and the wounded Ogre. Extended XML checking to random-battle opening conversations and documented context-specific unit terminology.
- Passed source/markup/placeholders, 53 conversation groups and 51 XML-linked choices, Java decoding, four-style font coverage and preservation checks. All previous main/campaign/shared translations remain unchanged.
- Updated the description to `#2 通用事件` (5,243 UTF-8 bytes), retaining all campaign names. Backed up and installed only two shared resources and config, verifying hashes and all other files unchanged. In-game review remains pending; no publication was performed.

### 通用事件 batch 1
- Added 77 shared content keys across 13 event families: 61 conversation keys and 16 linked choice/follow-up keys. Includes the ancient temple, drinking contest, acid rain and party interactions. Shared coverage: 77/3,163 (2.4%); 4,316 total runtime entries including metadata.
- Added two shared runtime resources, source coverage declarations, shared metadata/namespace validation and an XML-based choice/outcome check. Preserved variables, placeholders, HTML and `=BR=` markers; added regression checks for rejected malformed input.
- Extended Java font checking to multiple English resources. All 4,316 runtime entries and 3,086 remaining shared fallback entries pass in four styles. Main text and campaign samples remain unchanged.
- Updated the Workshop description to include `#1 通用事件` (5,063 UTF-8 bytes), retaining all campaign names. Backed up config and installed the two shared resources plus config with hash verification. In-game review remains pending; no publication was performed.

### 正文 batch 8 — main messages complete
- Added the remaining 1,065 main entries, including 298 object descriptions, remaining interface/help, effect fragments, combat logs and faction/person names. Main coverage is 4,215/4,215 content keys, plus six metadata keys; 4,235 runtime entries including retained campaign samples. All 326 object descriptions are covered.
- Registered four editable translation files and added an exact main-key coverage requirement to the build. Expanded the glossary to 1,630 keyed rows; retained all prior translations.
- Checked duration arguments and Magic Channel log context against local game code. Repaired malformed source HTML in translated prompts. Translated number words while documenting the engine's remaining English-style spacing/thousand grouping limitation.
- Updated the description to `#8 正文` (4,899 UTF-8 bytes), preserving all 32 bilingual campaign names. Passed key/placeholder/markup, Java decoding, four-style font and preservation checks; backed up and installed two local files with hash verification. No publication was performed. Batches 6–8 still require in-game review; separate shared-event and campaign resources remain pending.

### 正文 batch 7
- Added 297 immunity, status, targeting, damage and spell-restriction entries. Main content coverage: 3,150/4,215 (74.7%), with 3,156 main runtime entries, 3,170 total runtime entries and 1,065 English fallback keys.
- Standardized the existing control-type label COMMAND to 统御; aligned the two mark-effect descriptions with their actual game names, 痛苦印记 and 死亡印记. Added 14 glossary rows (1,543 total).
- Updated `#7 正文` in the Chinese Workshop description while preserving all campaign names. User appearance feedback covers batch 5; batches 6–7 still need in-game review.
- Passed key/placeholder/markup checks, Java decoding and four-style font coverage for 3,170 runtime entries and 1,065 fallbacks. Backed up and installed the runtime/config locally, verifying installed hashes against the package. Description: 4,671 UTF-8 bytes. No publication was performed.

### 正文 batch 6
- User reported normal in-game appearance through batch 5. Added 254 summon, life-transfer, stealth, trap, weather, immunity and restriction entries; new content still requires in-game review.
- Content coverage is 2,853/4,215 (67.7% by entries), with 2,859 main runtime entries, 2,873 total runtime entries and 1,362 English fallback keys.
- Standardized Workshop headings to `#4 正文`, `#5 正文`, `#6 正文`, retained all campaign names and recorded the user's test feedback separately from new-batch validation.
- Passed build/HTML/placeholders, Java decoding and four-style font checks for 2,873 runtime entries and 1,362 English fallbacks. Preserved all prior main values and campaign samples; backed up and installed two local mod files with hash verification. No publication was performed.

### 正文说明 batch 5
- Added 20 battle/world-map tutorial pages and 189 skill/item effect fragments and supporting entries (209 total). Reused terminology, added the Slayer label, and clarified dynamic attack type/value ordering and Parry/Riposte backstab exclusions from local game code.
- Content coverage: 2,599/4,215 (61.7% by entries), with 2,605 main runtime entries, 2,619 total runtime entries and 1,616 English fallback keys. Glossary: 1,529 keyed rows.
- Updated the Chinese Workshop progress description, preserving all campaign names. All named battle/world-map tutorial keys are translated; other help and effect text remains in progress.
- Validated source keys, placeholders, markup, all 21 named tutorial keys, 2,619 Java runtime entries and 1,616 English fallback entries in four font styles. Preserved every prior main value and campaign sample; backed up and installed the runtime/description locally with hash verification. In-game layout remains pending; no publication was performed.

### 正文说明 batch 4
- Added 164 shared gameplay entries: environmental effects, equipment and potion restrictions, crafting/resources, recruitment/upgrades, traits, team morale and related effect text.
- Main content coverage is now 2,390/4,215 (56.7% by entries), with 2,396 main runtime entries including metadata, 2,410 total runtime entries and 1,825 English fallback keys.
- Reused existing terminology and UI labels; documented affinity, prestige and source-text ambiguities. Updated the Chinese Workshop progress description while retaining all campaign names.
- Build, placeholder/HTML and Java font checks passed for 2,410 runtime entries and 1,825 English fallback entries. Preserved all prior main values and campaign samples; backed up and installed the runtime/description locally, verifying hashes and unchanged remaining mod files. In-game layout remains pending; no publication was performed for this batch.

### Workshop description upload fix
- Latest wording: removed English explanatory text while preserving all 32 bilingual campaign/expansion names and setup labels. “Main text” is now “正文”; the current description is 4,134 UTF-8 bytes.
- The user's upload returned `InvalidParam`; the local description was 8,341 UTF-8 bytes, exceeding Steam's 8,000-byte limit although the character-count check passed.
- Compacted repeated campaign-status rows to lists, retaining every campaign name and progress heading. Description is now 7,062 UTF-8 bytes.
- Packaging and the local description helper now check UTF-8 bytes before changing files, with a conservative 7,999-byte maximum. Both reject the original description and boundary overflow cases; normal packaging passes.
- Backed up and updated local installed/package metadata. A successful Workshop retry remains unconfirmed; no upload was performed by the assistant.

### Terminology batch 3
- Added 1,027 main entries: 449 item/resource names and templates plus 578 skills, attributes, conditions, crafting professions, set names and short display fragments.
- Completed the 937-key main label block (399 item names/templates and 538 other labels), the 51 crafting-material labels, nine crafting-profession labels and 30 item-set labels. The 450 item/resource-name total replaces the earlier 455 suffix-based estimate, which accidentally included five UI prompts.
- Consolidated 1,528 glossary keys. Documented context-sensitive meanings, provisional proper names, and misleading internal identifiers; preserved all previously deployed main translations.
- Current coverage: 2,226/4,215 content entries (52.8% by entries, not words), 2,232 main runtime entries including metadata, 2,246 runtime entries including campaign samples, and 1,989 missing main keys.
- Expanded build coverage checks for the terminology blocks; long descriptions and in-game layout remain incomplete.
- Batch 3 passed text/build checks, Java decoding of 2,246 runtime entries, four-style font coverage including engine symbols and 1,989 English fallback entries, and a 1,528-row glossary comparison. Installed locally after backup and verified by SHA-256; no Steam upload or GitHub push.

### Terminology batch 2
- Added 396 main entries: 298 remaining object names, 70 remaining race/group labels, and 28 battlefield/stat fragments. All 326 object names and the 73-label source race/group section are covered. Descriptions remain at 28 of 326.
- Consolidated 501 keyed glossary entries. Preserved displayed-name distinctions such as GHOST=Incorporeal versus INCORPOREAL=Phasing; standardized Vase to 花瓶.
- Current totals: 1,205 main entries including metadata, 1,219 runtime entries including retained campaign samples, and 3,016 main keys remaining (28.4% text-entry coverage).
- Replaced SimHei in all four settings with local static regular Noto Sans SC, fixing missing NBSP/bullet glyph coverage. Added reproducible variable-to-static font preparation and configured-font packaging checks.
- Expanded Java validation to engine tooltip symbols, four font styles and remaining English main text. The old font fails this regression check; the replacement passes all 1,219 runtime entries and 3,016 English fallback entries. Headless Swing preview inspected; in-game confirmation remains pending.

### Added
- 320 main-text translations: 129 gameplay/statistics/inventory/skill entries, 54 bestiary entries covering 27 units, and 137 combat-log entries.
- Main-text scope and glossary notes. The initial campaign deferral was superseded by the user's restored order: terminology, gameplay descriptions, shared events, then campaigns starting with Undead.
- Consolidated terminology baseline and localization plan, with explicit remaining terminology work.

### Changed
- Register three new main-text batches in the build and report their counts separately from the original 481 Phase 1 entries.
- Record source coverage: 809 of 4,221 main-text entries supplied (including metadata); 3,412 remain untranslated. The full runtime has 823 entries including retained campaign samples.
- Generate UI properties and the validation report with LF line endings for reproducible Windows builds.

### Validation
- Source keys, duplicate keys, placeholder counts, balanced HTML and original button/settings coverage passed.
- The game's bundled Java decoded all 823 runtime entries and the local test font covered every character. All 489 previous main entries were retained; campaign runtime files were unchanged.
- Installed the main runtime file and updated description into the local test item after backing it up; installed files matched the staged package by SHA-256. No Steam upload was performed.
- New batch requires in-game review, particularly compact stat columns, long tooltips and bestiary descriptions. The earlier conversation validation warning remains unresolved.
- Later screenshot investigation confirmed SimHei lacks U+00A0/U+2022 used in engine-generated tooltip prefixes. Batch 2 addresses these with a replacement font and broader checks; game layout confirmation remains pending.

## [0.1.0] - 2026-11-15

### Added
- Initial collaborative repository for Age of Fear: Total Simplified Chinese localization.
- 481 Phase 1 translations covering menus, settings, tooltips, battle controls, difficulty and multiplayer dialogs.
- Chinese language/font metadata and small Undead campaign and conversation samples: 489 UI entries, 503 runtime entries in total.
- Validation of duplicate keys, source keys, placeholders, HTML, selected source-block coverage and ASCII Java-properties encoding.
- Project handoff, milestone notes, contributor workflow, dependency list and local-resource setup script.
- Explicit Workshop item and expected-owner arguments for packaging and description updates.

### Known limitations
- Most campaign text and gameplay descriptions remain untranslated and fall back to English.
- Full in-game layout review is pending; a conversation validation warning remains unresolved.
- Campaign edits are not rebuilt by the UI build script; extend validation/build support before substantial campaign work.
- Font files and original game resources are not distributed. A redistributable font is needed for a public playable release.
- Original pilot bootstrap retains machine-specific paths; use setup_local.py for a fresh checkout.
