# Age of Fear: Total — 简体中文汉化

Work in progress · Translation v0.1.0 · Game v11.0.5 · Locale `zh`

Simplified Chinese translations for the interface, gameplay text, events and campaign stories. Untranslated text falls back to English.

## Progress

| Resource | Translated | Coverage |
| --- | ---: | ---: |
| 界面与正文 | 4,215 / 4,215 | 100% |
| 通用事件 | 2,144 / 2,144 | 100% |
| 通用对话 | 1,019 / 1,019 | 100% |
| 亡灵战役：死灵法师的崛起 | 251 / 732 | 34.3% |
| 永生之旅：独立对话文件 | 275 / 275 | 100% |
| 海盗！：独立对话文件 | 239 / 239 | 100% |
| 元素使：独立对话文件 | 18 / 18 | 100% |
| 血与月：独立对话文件 | 130 / 130 | 100% |
| 维克多的实验：当前关卡正文 | 114 / 114 | 100% |
| 维克多的实验：独立对话文件 | 238 / 238 | 100% |
| 风暴山：当前关卡正文 | 536 / 536 | 100% |
| 风暴山：独立对话文件 | 118 / 118 | 100% |
| 生者与死者：当前关卡正文 | 293 / 293 | 100% |
| 生者与死者：独立对话文件 | 41 / 41 | 100% |
| 战争机器：当前关卡正文 | 323 / 323 | 100% |
| 战争机器：独立对话文件 | 52 / 52 | 100% |
| Other main-campaign stories (excluding expansions above) | Not started | — |

All completed expansion resources and the latest description were installed locally on 2026-11-21 after a full backup and hash verification. The mod now contains 17 runtime files and 10,044 entries including metadata. No Steam upload was performed; in-game review remains deferred.

Counts exclude metadata and measure entries, not words. One entry may contain a full story page. The two shared properties files are fully covered; separate campaign/expansion dialogue and script-generated English remain outside these totals.

The Quest for Immortality's conversation resource is fully translated: 14 AXX groups, nine battle-reaction groups and seven return-to-game groups, totaling 275 content entries. Six return greetings are defined in the core game; the Free World group's eight entries have no matching XML in the installed archives, so their runtime use remains unverified. This resource is installed locally; file coverage does not establish whole-expansion completion.

Pirates! now has all 18 dialogue groups translated (239/239 entries), including 14 story groups and four battle-reaction groups. Its runtime resource is installed locally; complete file coverage does not establish whole-expansion completion.

The Elementalist's five dialogue groups are fully translated (18/18 entries), including both battle reactions. The resource is installed locally.

The Blood and Moon's 21 independent dialogue groups are fully translated (130/130 entries), including both campaign variants and all battle reactions. This resource is installed locally; game testing remains deferred.

The Victor's Experiment adds 238 independent conversation entries and 114 current level entries. Its old expansion properties are outdated; current level text comes from the matching Vampire Hunter campaign resource and is checked against the expansion XML. These expansion entries are counted separately from main-campaign progress. The build is installed locally.

The Storm Mountain adds 536 current level entries and all 118 independent conversation entries (21 groups). Current campaign text is verified against the expansion XML; one ghost-cave reaction has a definition but no verified trigger reference. Main-campaign VXX reactions remain outside this file coverage. These resources are installed locally.

The Quick and The Dead adds 293 current level entries and all 41 independent dialogue entries (four groups). Both files are XML-checked, including the payment and recruitment choices. The rose-giving dialogue has no verified trigger reference. These resources are installed locally.

War Machine adds 323 current level entries and all 52 independent dialogue entries (six groups). Current campaign text, quest choices, material dependencies and rewards are checked against the expansion XML. These resources are installed locally; automated checks do not establish in-game behavior.

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
| `source/` | Local English references, original font download and guide; excluded from Git |
| `backups/` | Latest full rollback backup and active-work recovery snapshot; excluded from Git |
| `workshop-package/` | Disposable package generated when needed; excluded from Git |

Build and packaging scripts stay in the root folder. Use `setup_local.py` for setup and `prepare_workshop.py` when an installable package is needed. Edit `translation/`; `pilot-mod/` contains the runtime build and packaging inputs.

## Contributing

Follow the [glossary](docs/TERMINOLOGY.md), coordinate translation scope, and preserve keys, placeholders and HTML. Read [CONTRIBUTING.md](CONTRIBUTING.md) and [AGENTS.md](AGENTS.md) before editing. Changes are recorded in [CHANGELOG.md](CHANGELOG.md); detailed notes are indexed in [docs/README.md](docs/README.md).

Automated validation passes for the current campaign batch; in-game layout review is pending. Packaging does not install or upload the mod.

Game files and fonts are not included. Third-party materials retain their owners' rights; font redistribution requires its license. No license for project contributions has been selected yet.
