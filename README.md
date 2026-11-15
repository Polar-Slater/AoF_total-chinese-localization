# Age of Fear: Total — Simplified Chinese localization

Version **0.1.0** · locale `zh` · work in progress · tested against game v11.0.5.

481 Phase 1 entries translate menus, settings, tooltips and battle controls. The runtime includes 489 UI entries and 14 campaign/conversation sample entries. Most story and detailed gameplay text still falls back to English. This repository is a development project, not a ready-to-install Workshop release.

Read [AI-HANDOFF.md](AI-HANDOFF.md) for technical context, [PHASE1-NOTES.md](PHASE1-NOTES.md) for scope and terminology, and [CHANGELOG.md](CHANGELOG.md) for version history. This README supersedes historical setup instructions in the pilot notes.

## Setup on Windows

Install your own copy of the game, Python 3.10 or later, and Git. From PowerShell:

```powershell
git clone https://github.com/Polar-Slater/AoF_total-chinese-localization.git
cd AoF_total-chinese-localization
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe setup_local.py --game 'D:\Software\Steam\steamapps\common\AOFTOTAL' --font 'C:\Windows\Fonts\simhei.ttf'
.\.venv\Scripts\python.exe build_translation.py
```

Replace the game path with your installation. `--font` is optional for text-only work. It supplies a locally available SimHei font for local testing; no font is included in Git. Do not distribute this local font without appropriate permission. Original English text is extracted locally into ignored `source/`; game-version differences may require reviewing the build's source-block coverage checks. The extraction refreshes local reference files, so review source changes when changing game versions.

## Files to edit

| Path | Purpose |
| --- | --- |
| `translation/` | Editable UTF-8 Chinese translations; primary source of truth |
| `pilot-mod/` | Runtime ASCII properties used by the packaging script; fonts are local only |
| `workshop-assets/` | Editable description and selected preview image |
| `inspection/CheckPilot.java` | Java decoding and font-glyph validation |
| `VERSION`, `CHANGELOG.md` | Translation milestone version and history |

Edit translation files, preserve keys/placeholders/functional HTML, then run the build. New UI batches must be registered in build_translation.py. The UI build does not rebuild campaign samples; extend it before adding substantial campaign text. Do not edit generated UI properties directly. `prepare_pilot.py` is a historical bootstrap with original-machine paths, not the recommended setup or translation workflow.

## Local packaging and checking

Create your own local item in the game's Workshop Manager first. Use its directory and actual `owner-user-id` from its config.xml:

```powershell
.\.venv\Scripts\python.exe prepare_workshop.py --item 'D:\path\to\your\workshop\item' --owner-id 'YOUR_OWNER_ID'
& 'D:\Software\Steam\steamapps\common\AOFTOTAL\jre\windows64\bin\java.exe' '-Djava.awt.headless=true' inspection/CheckPilot.java workshop-package
```

Packaging backs up the local item and stages `workshop-package/`; it does not install or upload. Test through Workshop Manager and Steam. Use your own ownership metadata. For local description updates, the PowerShell helper takes `-ItemConfig '...\config.xml' -OwnerId 'YOUR_OWNER_ID'`. It updates local files only.

Full layout review is pending, and `Could not load conversations [UXX_Please_review_us]` remains unresolved. Passing build checks does not establish complete in-game validation.

## Collaboration and versions

See [CONTRIBUTING.md](CONTRIBUTING.md). Each collaborator works on a separate branch and opens a pull request. Agree on translation batches to reduce conflicts. Record changes under Unreleased; at a milestone, update VERSION, move notes into a dated changelog section and tag the matching commit `vX.Y.Z`.

## Included materials

Game binaries, extracted English resources, the supplied game guide, bytecode dumps, fonts, backups, settings and generated Workshop packages are excluded. Recreate local resources with setup_local.py. The selected preview is a game screenshot; underlying game assets belong to their respective owners. No blanket license for third-party materials is granted by this repository. No open-source license for project contributions has been selected yet.
