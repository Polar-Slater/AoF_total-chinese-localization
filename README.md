# Age of Fear: Total — Simplified Chinese localization

Version **0.1.0** · locale `zh` · work in progress · tested against game v11.0.5.

The main message resource is now fully translated: **4,215/4,215 content keys (100% entry coverage)**, plus six metadata keys, with no missing main keys. Batch 8 adds the remaining 1,065 entries: interface/help, combat logs, effect fragments, faction/person labels and 298 object descriptions. All 326 object names and descriptions are covered. The main resource and retained campaign/conversation samples account for 4,221 + 14 entries; new shared resources are counted below. This is completion of `messages-en.properties` coverage, not of the whole game: separate shared-event and campaign resources remain largely untranslated. The glossary contains 1,630 keyed terms. Automated checks do not replace in-game review; the user reports no errors with the previous uploaded version, without claiming exhaustive text or layout review. The engine still composes number words with English-style spacing and thousand groups, so large numbers can read awkwardly in Chinese. Shared-event translation has started; campaign stories follow, starting with the Undead campaign. See [LOCALIZATION-PLAN.md](LOCALIZATION-PLAN.md), [TERMINOLOGY.md](TERMINOLOGY.md) and [MAIN-TEXT-BATCH8.md](MAIN-TEXT-BATCH8.md). This is a development project, not a ready-to-install Workshop release.

Shared batches 1–7 now cover **1,582/3,163 shared content keys (50.0%)**: 883 shared-level/choice keys and 699 conversation keys. This milestone adds 680 keys: 363 for eight faction bases and 317 for desertion, five minigames, Windmill, weather invocations and common prompts. The two shared runtime files contain 1,586 entries including metadata; all runtime files total 5,821 entries. All 487 `SGE_` conversation keys and 410 `LevelGlobalEvent*` keys remain covered. Some base outcomes belong to separate campaign resources and are still English, as are script-supplied minigame fragments. See [SHARED-TEXT-50-PERCENT.md](SHARED-TEXT-50-PERCENT.md). The 50% figure measures shared resource entries, not words or whole-game completion. The user uploaded the previous version through shared batch 5 and reported no in-game errors; new batches 6–7 have automated validation only. Translation continues without requiring a game test.

Read [AI-HANDOFF.md](AI-HANDOFF.md) for technical context, [PHASE1-NOTES.md](PHASE1-NOTES.md) and [MAIN-TEXT-NOTES.md](MAIN-TEXT-NOTES.md) for scope and terminology, and [CHANGELOG.md](CHANGELOG.md) for version history. This README supersedes historical setup instructions in the pilot notes.

## Setup on Windows

Install your own copy of the game, Python 3.10 or later, and Git. From PowerShell:

```powershell
git clone https://github.com/Polar-Slater/AoF_total-chinese-localization.git
cd AoF_total-chinese-localization
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe setup_local.py --game 'D:\Software\Steam\steamapps\common\AOFTOTAL' --font 'C:\Windows\Fonts\NotoSansSC-VF.ttf'
.\.venv\Scripts\python.exe build_translation.py
```

Replace the game/font paths with your installation. `--font` is optional for text-only work. Supply a locally available Noto Sans SC TTF (regular or variable); `prepare_font.py` converts variable fonts into static regular weight 400 for the Java renderer and saves `noto-sans-sc.ttf`. No font is included in Git; release packaging still needs its appropriate license materials. To prepare only the font, run `.\.venv\Scripts\python.exe prepare_font.py 'C:\path\to\NotoSansSC-VF.ttf'`. Original English text is extracted locally into ignored `source/`; game-version differences may require reviewing source-block coverage checks. The extraction refreshes local references, so review changes when changing game versions.

## Files to edit

| Path | Purpose |
| --- | --- |
| `translation/` | Editable UTF-8 Chinese translations; primary source of truth |
| `pilot-mod/` | Runtime ASCII properties used by the packaging script; fonts are local only |
| `workshop-assets/` | Editable description and selected preview image |
| `inspection/CheckPilot.java` | Java decoding and font-glyph validation |
| `VERSION`, `CHANGELOG.md` | Translation milestone version and history |

Edit translation files, preserve keys/placeholders/functional HTML, then run the build. New batches must be registered in build_translation.py. Shared event scope and linked choices are declared in translation/shared-coverage.json; the build checks complete selected families, metadata, =BR= breaks and runtime key collisions. The build does not rebuild the retained campaign samples; extend it before adding substantial campaign text. Do not edit generated runtime properties directly. `prepare_pilot.py` is a historical bootstrap with original-machine paths, not the recommended setup or translation workflow.

## Local packaging and checking

Create your own local item in the game's Workshop Manager first. Use its directory and actual `owner-user-id` from its config.xml:

```powershell
.\.venv\Scripts\python.exe prepare_workshop.py --item 'D:\path\to\your\workshop\item' --owner-id 'YOUR_OWNER_ID'
& 'D:\Software\Steam\steamapps\common\AOFTOTAL\jre\windows64\bin\java.exe' '-Djava.awt.headless=true' inspection/CheckPilot.java workshop-package source/aof/messages-en.properties source/aof-data/shared-en.properties source/aof-data/shared-conversations-en.properties
.\.venv\Scripts\python.exe inspection/check_shared_events.py --game 'D:\Software\Steam\steamapps\common\AOFTOTAL'
```

Packaging backs up the local item and stages `workshop-package/`; it does not install or upload. Test through Workshop Manager and Steam. Use your own ownership metadata. For local description updates, the PowerShell helper takes `-ItemConfig '...\config.xml' -OwnerId 'YOUR_OWNER_ID'`. It updates local files only.

The user reports successful upload and no in-game errors with the version through shared batch 5. Shared batches 6–7 have not been tested in game. The earlier `Could not load conversations [UXX_Please_review_us]` warning has not been independently diagnosed; the latest smoke test does not prove its cause was fixed. Passing build checks does not establish complete in-game validation.

SimHei lacked U+00A0 and U+2022 used by engine-generated tooltip prefixes. All four font settings now use a static regular Noto Sans SC resource. The expanded Java check verifies configured fonts in plain/bold/italic/bold-italic, those engine symbols, all translated values and (with additional English resource arguments) remaining English text in the main/shared resources. It reproduced the legacy font failure and passes with the replacement. A Swing HTML preview is available through `inspection/RenderFontSample.java`; the latest user smoke test reported no errors; the new shared batches still await eventual layout review.

## Collaboration and versions

See [CONTRIBUTING.md](CONTRIBUTING.md). Each collaborator works on a separate branch and opens a pull request. Agree on translation batches to reduce conflicts. Record changes under Unreleased; at a milestone, update VERSION, move notes into a dated changelog section and tag the matching commit `vX.Y.Z`.

## Included materials

Game binaries, extracted English resources, the supplied game guide, bytecode dumps, fonts, backups, settings and generated Workshop packages are excluded. Recreate local resources with setup_local.py. The selected preview is a game screenshot; underlying game assets belong to their respective owners. No blanket license for third-party materials is granted by this repository. No open-source license for project contributions has been selected yet.
