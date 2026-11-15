# AI handoff: Age of Fear Total Simplified Chinese translation

Last updated: 2026-11-15. Read this before continuing the project. This document records prior work, not authorization to publish or change another person's Steam account.

## Latest user direction: restored translation order

Terminology preference: translate “Main text” as “正文” in Chinese descriptions and progress labels (for example, `#1 正文`).

The user has restored the original order: establish consistent terminology for units, stats, items and skills; then translate gameplay descriptions, shared events and campaign stories, starting with the Undead campaign. This supersedes the earlier campaign-deferral direction. Follow `LOCALIZATION-PLAN.md`. The core terminology baseline is now established in `TERMINOLOGY.md`; continue reviewing context and provisional names while moving into gameplay descriptions. Keep all completed translation batches.

A later screenshot showed square prefixes in the Swamp tooltip. Inspection confirmed the engine inserts `&nbsp;` and U+2022, while SimHei lacks U+00A0/U+2022. The earlier validator only checked translation values. This is now addressed with a local static regular Noto Sans SC font and expanded checks; confirm actual game appearance after restart.

## Latest upload issue: description byte limit

Subsequent user preference: remove English explanatory text from the Workshop description, but retain all campaign names. The current description is Chinese with all 32 bilingual campaign/expansion names preserved, plus the English game title and exact menu/language labels needed for setup. Source, staged package and installed config match at 4,134 UTF-8 bytes. The previous 7,062-byte version below is historical. Local config was backed up before this update; no upload was performed.

The user's Workshop Manager upload returned `InvalidParam` on 2026-11-15. Steam's workshop log at 17:30 shows content/preview transfer followed by Invalid Parameter. The description was 6,381 characters but 8,341 UTF-8 bytes; Steam documents an 8,000-byte maximum (https://partner.steamgames.com/doc/api/ISteamRemoteStorage#constants). This is a likely cause, not yet confirmed by a successful retry. Both packaging and the local PowerShell helper now enforce a conservative 7,999-byte maximum before writes. The original description and 8,000/8,001-byte cases are rejected by both scripts; normal packaging passes. Repeated open-campaign and expansion status table rows were compacted into lists without dropping campaign names. Source, package and installed descriptions are now 7,062 bytes. Local metadata was backed up and updated; user should reopen Workshop Manager and retry. No assistant upload was performed. Original description text is backed up at `backups/workshop-description-before-byte-limit-fix.txt`.

## Terminology batch 3 (current, unreleased)

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
