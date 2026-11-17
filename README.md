# Age of Fear: Total — 简体中文汉化

Work in progress · Translation v0.1.0 · Game v11.0.5 · Locale `zh`

Simplified Chinese translations for the interface, gameplay text, events and campaign stories. Untranslated text falls back to English.

## Progress

| Resource | Translated | Coverage |
| --- | ---: | ---: |
| 界面与正文 | 4,215 / 4,215 | 100% |
| 通用事件 | 2,144 / 2,144 | 100% |
| 通用对话 | 1,019 / 1,019 | 100% |
| 亡灵战役：死灵法师的崛起 | 206 / 732 | 28.1% |
| Other campaigns | Not started | — |

Counts exclude metadata and measure entries, not words. One entry may contain a full story page. The two shared properties files are fully covered; separate campaign/expansion dialogue and script-generated English remain outside these totals.

通用事件 / 通用对话 and campaign stories are separate workstreams. Each collaborator edits their assigned resources and preserves the other section. See the [work plan](docs/LOCALIZATION-PLAN.md).

## Get started

Requires Windows, Python 3.10+ and a local copy of the game. Run from the project folder, replacing the example game path:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe setup_local.py --game 'C:\path\to\AOFTOTAL'
.\.venv\Scripts\python.exe build_translation.py
```

Edit Chinese text in `translation/`, then rebuild. See [setup and packaging](docs/SETUP.md) for fonts and local packages, and [testing](docs/TESTING.md) for validation.

## Project layout

| Location | Contents |
| --- | --- |
| `translation/` | Editable Chinese text and coverage declarations |
| `pilot-mod/` | Generated game resources; do not edit directly |
| `workshop-assets/` | Workshop description and preview |
| `inspection/` | Validation tools and reports |
| `docs/` | Setup, testing, work plan and glossary |
| `docs/batches/` | Translation batch history |
| `source/`, `backups/`, `workshop-package/`, `pilot-home/` | Local references, backups, packages and test state; excluded from Git |

Build and packaging scripts stay in the root folder. `prepare_pilot.py` and `launch-chinese-test.bat` are legacy tools; use the setup guide for current work.

## Contributing

Follow the [glossary](docs/TERMINOLOGY.md), coordinate translation scope, and preserve keys, placeholders and HTML. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) before editing. Changes are recorded in [CHANGELOG.md](CHANGELOG.md); detailed notes are indexed in [docs/README.md](docs/README.md).

Automated validation passes for the current campaign batch; in-game layout review is pending. Packaging does not install or upload the mod.

Game files and fonts are not included. Third-party materials retain their owners' rights; font redistribution requires its license. No license for project contributions has been selected yet.
