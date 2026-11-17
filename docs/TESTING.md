# Validation and game testing

Run commands from the project root after building translations. Prepare the font first; see [setup](SETUP.md).

## Automated checks

```powershell
.\.venv\Scripts\python.exe build_translation.py
& 'C:\path\to\AOFTOTAL\jre\windows64\bin\java.exe' '-Djava.awt.headless=true' inspection/CheckPilot.java pilot-mod source/aof/messages-en.properties source/aof-data/shared-en.properties source/aof-data/shared-conversations-en.properties source/aof-undead/undeadcampaign-en.properties source/aof-undead/undeadcampaign-conversations-en.properties
& 'C:\path\to\AOFTOTAL\jre\windows64\bin\java.exe' '-Djava.awt.headless=true' inspection/CheckInventoryLayout.java pilot-mod
.\.venv\Scripts\python.exe inspection/check_shared_events.py --game 'C:\path\to\AOFTOTAL'
git diff --check
```

Use `workshop-package` instead of `pilot-mod` to check a staged package. The Java check verifies properties decoding and font coverage for translated text, supplied English fallback resources and engine symbols in four font styles.

## In-game review

After local installation, launch through Steam and select **Options → Screen → Language → Chinese (Simplified) - Test**. Check story pages, dialogue, choices and long tooltips for missing glyphs, clipping and awkward wording.

The version through shared batch 5 had a successful smoke test. Shared batches 6–17 and Undead batches 1–5 have automated validation but await in-game review. Translation may continue while game testing is deferred. Undead batch 5 is built locally (6,678 runtime entries) but is not installed; installation records below describe the earlier deployed version.

The shared collaborator recorded the following installation before this merge: at the user’s request, shared batches through 17 and the latest description are now synced to the local Workshop folder. This sync changed the two shared properties files and `config.xml`; a full mod backup and SHA-256 checks verified installation and preservation of every other file, including main messages, the existing 45-key Undead opening batch, fonts and preview. The installed package contains 6,472 runtime entries and 2,198 shared content keys. The description stored in XML is 4,911 UTF-8 bytes after newline normalization and trimming, and matched that revision of the description source under the same normalization. The merged development resources contain newer campaign text; this merge does not update the installed package. No Steam upload or new game test was performed. Earlier batch notes and validation reports retain their historical pre-installation state.

## Latest local installation

The subsequent authorized sync installed Undead batches 2–4 alongside shared batches through 17. It updated only the two campaign properties files and the description in config.xml. The installed mod now contains 6,633 runtime entries, including 206 campaign and 2,198 shared content entries. The description is 4,970 UTF-8 bytes after normalization and trimming. A full backup and SHA-256 comparisons verified the changed files against staging and preserved all other installed files. The staged Java check passed for all runtime entries, 1,491 English fallback entries and four font styles. No Steam upload or new in-game test was performed.

The description was subsequently shortened to remove spoilers (3,247 UTF-8 bytes). The supplied Google Fonts static Noto Sans SC Regular font and its OFL license/notice were installed after another full backup; the unused SimHei font was removed. Hash checks verified preservation of all unrelated installed files, and the Java/font checks above passed against the installed folder itself. These local updates have not been uploaded to Steam or reviewed in game.

## Inventory layout fix

The reported narrow inventory columns were reproduced in a headless Swing layout fixture: the original font requires 502 pixels in a 500-pixel container. A button-only font with compact line metrics needs 497 pixels and retains the 590×467 item panel. `CheckInventoryLayout.java` accepts an optional original font path to reproduce the failing case as well. This check supplements glyph coverage; it does not replace in-game review.

The fix was installed locally after a full backup and hash verification, changing only the button-font property, adding `aof-han-ui.ttf`, and updating the font notice. All existing translations, the body font, metadata and other mod files were preserved, including campaign files newer than the current checkout. Restart and inspect the inventory; that in-game confirmation remains pending. See [details](batches/INVENTORY-LAYOUT-FIX.md).

## Known issues

- The original Shaman's Hut `on-select-42` menu targets hero 107, while its unequip command targets hero 17. Translation preserves the source placeholders; the script mismatch is recorded in shared batch 16 and remains unfixed.
- Large numbers still follow the engine's English-style grouping and spacing.
- Some minigame fragments come directly from scripts and remain English.
- Some shared locations call campaign dialogue that is not translated yet.
- The earlier `UXX_Please_review_us` loading warning remains undiagnosed.

Automated checks do not prove that every screen fits or every branch works in game. Record what was actually tested in the relevant [batch note](README.md).

## Shared batch 18 validation (2026-11-17)

The local build now contains 2,222 shared content entries and 6,657 runtime entries in total. The batch adds 24 keys for the Jungle Pyramid and Mages Bazaar; all existing editable translations and runtime key values are preserved, and main/campaign runtime files are byte-identical to the pre-batch backup. XML checks cover 304 conversation groups and 94 follow-up levels, with 30 separate campaign conversation references outside shared scope. Java decoding and all four font styles passed, including 1,467 English fallback entries. See [batch 18](batches/SHARED-EVENTS-BATCH18.md) and `inspection/shared-batch18-validation.json`. This batch and its updated description have not been installed or uploaded. In-game event review remains deferred.

## Shared batch 19 validation (2026-11-17)

The local build contains 2,253 shared content entries and 6,688 runtime entries. The batch adds 31 keys for the circus dancer and shared Sandworm encounter, leaving 17 shared conversation keys untranslated. XML checks cover 306 conversation groups and 99 follow-up levels; the external campaign reference count remains 30. Java decoding and four font styles passed, including 1,436 English fallback entries. Existing editable translations and runtime values are preserved; main and campaign runtime files are byte-identical to the pre-batch backup. See [batch 19](batches/SHARED-EVENTS-BATCH19.md) and `inspection/shared-batch19-validation.json`. Batches 18–19 and their description updates have not been installed or uploaded. The shared Sandworm encounter does not resolve the separate open-campaign resource gap recorded in `GAME-BUGS.md`.

## Shared batch 20 validation (2026-11-17)

The local build contains 2,287 shared content entries and 6,722 runtime entries. World Knot adds 34 keys across three conversation groups and four text-bearing levels, with three textless shops included in dependency checks. XML validation covers 309 conversation groups and 106 follow-up levels; 30 external campaign conversation references remain separately tracked. Java decoding and four font styles passed, including 1,402 English fallback entries. All old editable translations and runtime values are preserved; main/campaign runtime files remain byte-identical to the pre-batch backup. See [batch 20](batches/SHARED-EVENTS-BATCH20.md) and `inspection/shared-batch20-validation.json`. Batches 18–20 have not been installed; game review remains deferred.

## Shared conversation completion, batch 21 (2026-11-17)

All 1,019 shared conversation content keys are now translated; the build requires exact source-key coverage for this file. The final 9 dialogue entries and 14 associated choice entries bring shared content to 2,310/3,163, leaving 853 shared event keys untranslated. XML validation covers 317 conversation groups, 281 conversation-linked choices and 116 follow-up levels. Java decoded 6,745 runtime entries and checked four font styles, including 1,379 remaining English fallback entries across the supplied resources; shared conversation fallback is zero. Existing translations and main/campaign runtime files are preserved. See [batch 21](batches/SHARED-EVENTS-BATCH21.md) and `inspection/shared-batch21-validation.json`. This milestone excludes separate campaign dialogue, script-generated English and in-game visual verification. Batches 18–21 have not been installed or uploaded.

## Installed shared batches 18–21 (2026-11-17)

The authorized local sync installed 112 new shared entries and the updated shared progress/date in the description. Installed shared content is now 2,310, with all 1,019 shared conversation entries translated. The installed campaign remains at 251 content entries and its description retains 251/732; these newer translations were preserved rather than replaced by the repository’s 206-entry baseline. Main messages, fonts, preview and non-description metadata are unchanged. A complete backup and SHA-256 verification passed. The staged package decoded 6,790 runtime entries and covered 1,334 English fallback entries in all four font styles; the inventory layout fixture passed. Installed files match staging. See `inspection/shared21-installation-validation.json`. No Steam upload or in-game retest was performed. Earlier batch reports retain their pre-installation status.

## Shared batch 22 validation (2026-11-17)

The local build contains 2,353 shared content entries and 6,788 runtime entries. The Barbarian King tomb and Fountain of Happiness add 43 shared event keys across seven levels. Shared conversations remain fully translated; 810 shared event keys remain. XML checks cover 317 conversation groups and 123 follow-up levels. External campaign dialogue references increase to 31 with `DXX_FountainOfHappiness_rebuild`, which is outside this batch. Java decoding and all four font styles passed, including 1,336 fallback entries. Earlier editable translations are unchanged; main, shared-conversation and campaign runtime files are byte-identical to the pre-batch backup. See [batch 22](batches/SHARED-EVENTS-BATCH22.md) and `inspection/shared-batch22-validation.json`. The installed mod remains through shared batch 21; this batch has not been installed or uploaded.

## Shared batch 23 validation (2026-11-17)

The local build contains 2,375 shared content entries and 6,810 runtime entries. Training Dummy revenge and Shadow Realm add 22 shared event keys; 788 event keys remain. XML checks cover 317 conversation groups and 128 follow-up levels. External campaign conversation references increase to 33 with the Dwarven and Forest Shadow Realm entry dialogues. Java decoding and four font styles passed, including 1,314 English fallback entries; shared conversation fallback remains zero. Existing editable translations and runtime values are preserved, and main/shared-conversation/campaign runtime files are byte-identical to the pre-batch backup. See [batch 23](batches/SHARED-EVENTS-BATCH23.md) and `inspection/shared-batch23-validation.json`. Batches 22–23 have not been installed; no new in-game review or upload.

## Shared batch 24 validation (2026-11-17)

The local build contains 2,482 shared content entries and 6,917 runtime entries. The Necromancer guild and secluded monastery add 107 event keys across nine text-bearing levels and two textless shop dependencies. XML checks cover 139 follow-up levels; external campaign references remain 33. Java decoding and four font styles passed, including 1,207 English fallback entries. Existing editable translations and runtime values are preserved; main/shared-conversation/campaign runtime files remain byte-identical. See [batch 24](batches/SHARED-EVENTS-BATCH24.md), `inspection/shared-batch24-validation.json`, and `GAME-BUGS.md` TXT-004 for the prayer/shop narrative mismatch. Batches 22–24 have not been installed; game review remains deferred.

## Shared batch 25 validation (2026-11-17)

The local build contains 2,549 shared content entries and 6,984 runtime entries. Elementalist shared levels and the Artificer's Shop add 67 keys across 17 text-bearing levels and four textless shop dependencies. XML checks cover 160 follow-up levels and report 36 external campaign/expansion conversation references; three EXX groups remain outside this batch. Java decoding and four font styles passed, including 1,140 English fallback entries. Existing editable translations and runtime values are preserved; main/shared-conversation/campaign runtime files remain byte-identical. The inventory fixture still fits at 497/500 pixels. See [batch 25](batches/SHARED-EVENTS-BATCH25.md) and `inspection/shared-batch25-validation.json` for the duplicate-source comparison and branch/reward checks. Batches 22–25 have not been installed; game review remains deferred.

## Shared batch 26 validation (2026-11-17)

The local build contains 2,603 shared content entries and 7,038 runtime entries. The Blood and Moon opening and Wolf in Distress stages, including their defeat page, add 54 keys across eight text-bearing levels and one shop dependency. XML checks cover 169 follow-up levels and report 39 external campaign/expansion conversation references; three newly encountered W groups remain outside this batch. Java decoding and four font styles passed, including 1,086 English fallback entries. Existing editable translations and runtime values are preserved; main/shared-conversation/campaign runtime files remain byte-identical. The inventory fixture fits at 497/500 pixels. See [batch 26](batches/SHARED-EVENTS-BATCH26.md) and `inspection/shared-batch26-validation.json` for source comparisons, party restoration, rewards and defeat routes. LevelWerewolf08 is the next untranslated world-map stage. Batches 22–26 have not been installed; game review remains deferred.

## Shared batch 27 validation (2026-11-17)

The local build contains 2,704 shared content entries and 7,139 runtime entries. Bloody Letter and Kidnappers Trail add 101 keys across nine text-bearing levels and two shop dependencies, including both campaign-specific battle variants. XML checks cover 180 follow-up levels and report 43 external campaign/expansion conversation references; four newly encountered WXX groups remain outside this batch. Java decoding and four font styles passed, including 985 English fallback entries. Existing editable translations and runtime values are preserved; main/shared-conversation/campaign runtime files remain byte-identical. The inventory fixture fits at 497/500 pixels. See [batch 27](batches/SHARED-EVENTS-BATCH27.md) and `inspection/shared-batch27-validation.json` for source comparisons, rewards, party restoration and the shared Naga victory/defeat story route. LevelWerewolf18 is the next untranslated world-map stage. Batches 22–27 have not been installed; game review remains deferred.

## Shared batch 28 validation (2026-11-17)

The local build contains 2,800 shared content entries and 7,235 runtime entries. The final Werewolf battle variants, aftermath and recruitment choices add 96 keys across five text-bearing levels and one shop dependency. All 251 LevelWerewolf keys in shared-en.properties are covered; seven separately stored expansion conversation groups remain untranslated. XML checks cover 186 follow-up levels and still report 43 external campaign/expansion conversation references. Java decoding and four font styles passed, including 889 English fallback entries. Existing editable translations and runtime values are preserved; main/shared-conversation/campaign runtime files remain byte-identical. The inventory fixture fits at 497/500 pixels. See [batch 28](batches/SHARED-EVENTS-BATCH28.md) and `inspection/shared-batch28-validation.json` for source comparisons, rewards and recruitment routes. Batches 22–28 have not been installed; game review remains deferred.

## Shared batch 29 validation (2026-11-17)

The local build contains 2,981 shared content entries and 7,416 runtime entries. All 181 LevelAlchemist keys in shared-en.properties are now translated, including the well, mine, sea portal, rescue/sacrifice endings and defeat page. XML checks cover 211 follow-up levels and report 57 external campaign/expansion conversation references; 14 AXX groups remain untranslated. The external ritual conversation's two trigger references were checked directly against the translated hidden-level buttons. Java decoding and four font styles passed, including 708 English fallback entries. Existing editable translations and runtime values are preserved; main/shared-conversation/campaign runtime files remain byte-identical. The inventory fixture fits at 497/500 pixels. See [batch 29](batches/SHARED-EVENTS-BATCH29.md) and `inspection/shared-batch29-validation.json` for source-version differences, coin/item consumption, mine progress, seal conditions and ending outcomes. Batches 22–29 have not been installed; game review remains deferred.

## Shared batch 30 validation (2026-11-17)

The local build contains 3,159 shared content entries and 7,594 runtime entries. All 178 LevelPirates keys in shared-en.properties are translated, including the tavern, capture/escape, treasure hunt, night raid and Executioner side quest. XML checks cover 235 follow-up levels and report 71 external campaign/expansion conversation references; 14 PXX groups remain untranslated. The external Executioner conversation's two trigger references were checked directly against the translated hidden-level buttons. Java decoding and four font styles passed, including 530 English fallback entries; four shared location labels remain. Existing editable translations and runtime values are preserved; main/shared-conversation/campaign runtime files remain byte-identical. The inventory fixture fits at 497/500 pixels. See [batch 30](batches/SHARED-EVENTS-BATCH30.md), `inspection/shared-batch30-validation.json`, and `GAME-BUGS.md` BUG-003 for the confirmed static mismatch between the night raid's Divers objective and Elementals condition. Reward behavior has not been reproduced in game. Batches 22–30 have not been installed; game review remains deferred.

## Shared batch 31 validation (2026-11-17)

The final four location labels bring shared events to 2,144/2,144 and shared conversations to 1,019/1,019: 3,163 content entries across the two fully covered files. The build now requires complete source key sets for both shared resources. Java decoded 7,598 runtime entries; main and both shared files have zero English fallback, while the supplied campaign references still have 526 fallback entries. Existing editable translations and runtime values are preserved; main/shared-conversation/campaign runtime files remain byte-identical. XML checks cover 239 follow-up levels and report 73 external campaign/expansion conversation references, including the two newly checked Smugglers Den introductions. Four font styles and the inventory fixture passed (497/500 pixels). See [batch 31](batches/SHARED-EVENTS-BATCH31.md) and `inspection/shared-batch31-validation.json`. Complete shared resource coverage does not establish complete game localization or in-game layout correctness. Batches 22–31 have not been installed; game review remains deferred.

## Installed shared content through batch 31 (2026-11-17)

The authorized sync installed 936 shared event entries and updated the local description. Before installation, actual shared coverage was 2,227 entries (1,208 events and 1,019 conversations), 83 fewer than the existing description reported. Only the shared event file differed from the previous installation manifest; the cause is unknown. Coverage is now 3,163/3,163. All existing shared values and the newer 251 campaign entries are preserved; the installed campaign description still reports 251/732. Only the shared event resource and description changed. The complete backup and installed directory match their SHA-256 inventories; fonts, licenses, preview and non-description metadata remain unchanged. Staging and installed-package Java checks decoded 7,643 entries, with zero main/shared fallback and 481 campaign fallback entries. All four font styles and the inventory fixture passed (497/500 pixels). The installed description is 3,396 UTF-8 bytes. See `inspection/shared31-installation-validation.json`. Earlier batch reports describe their pre-installation state. No Steam upload, Git push or in-game retest was performed.
