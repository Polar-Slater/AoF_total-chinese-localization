# Project instructions

## Scope and current work

Build a complete Simplified Chinese localization of Age of Fear: Total, using locale `zh`. Read README.md, docs/LOCALIZATION-PLAN.md, docs/TERMINOLOGY.md and the latest batch notes before editing. Historical batch notes describe earlier states; current instructions take precedence.

- Main messages: 4,215/4,215 content keys translated.
- 通用事件 and 通用对话: 2,198/3,163 content keys translated. The current chat works on these resources; the user’s friend handles campaign translation. Keep their translation files separate.
- Campaign work belongs to the other collaborator, starting with Rise of The Necromancer. Undead batch 1 covers 45/732 content keys: Level00 through Level03a and four U00/U01 dialogue groups. Continue with the Bone River/Mistmill sequence and U02 dialogue, checking Level04 shop dependencies. See docs/batches/UNDEAD-CAMPAIGN-BATCH1.md.
- Counts measure resource entries, not words or whole-game completion. A long story page can occupy one key.

## Translation rules

- Edit UTF-8 files under `translation/`; never edit generated runtime properties directly.
- Follow docs/TERMINOLOGY.md. Use natural, faithful Chinese, preserving character voice and context. Retain existing translations unless a correction is justified.
- Write place names as `中文名 (English)`, retaining the original English spelling and case.
- Use 通用事件 for shared events, 通用对话 for shared conversations, and 正文 for main text. Keep technical resource names and keys unchanged.
- Preserve keys, placeholders and their multiplicities, functional HTML and `=BR=` markers. Missing keys intentionally fall back to English; do not copy English into Chinese resources and count it as translated.
- Translate complete declared level or conversation groups. Check linked choices and outcomes against original game resources. Separate campaign-resource dependencies and script-generated English from shared-resource coverage.

## Build and validation

- Extract local English references with `setup_local.py --game <game-directory>`. Keep archive directories separate; do not flatten duplicate resource filenames without checking precedence.
- Run `build_translation.py` after editing. Main/shared batches are registered there; campaign scope is declared in `translation/campaign-coverage.json` and shared scope in `translation/shared-coverage.json`.
- Runtime resources under `pilot-mod/` must use ASCII Java-properties escapes. The engine loads properties through Java `Properties.load(InputStream)`.
- Run `inspection/CheckPilot.java` with the game's Java runtime, the build/package root and relevant English properties files. Check all four font styles, remaining English fallback and engine NBSP/bullet symbols.
- Font configuration uses static regular Noto Sans SC. Use `prepare_font.py` for variable-font conversion. Keep local font binaries out of Git; redistribution requires appropriate license materials.
- Verify previous translations are preserved and run `git diff --check`. Update coverage reports, batch notes and CHANGELOG.md accurately.
- In-game testing is deferred while translation proceeds. Automated checks do not establish layout correctness. Do not require a new game test before continuing authorized translation.

## Packaging and collaboration

- Follow CONTRIBUTING.md. Do not overwrite unrelated local edits or another collaborator's translations.
- `prepare_workshop.py` requires the local item path and its actual owner ID. Preserve ownership checks; never hardcode personal account details.
- Back up before an authorized local installation and verify changed files against staging. Packaging does not install or upload automatically.
- Keep Workshop descriptions below the project's 7,999 UTF-8 byte limit and preserve bilingual campaign names and the selected preview.
- Publishing, uploading and pushing require corresponding user authorization. Shared batches through 17 and the existing Undead opening batch are now installed locally with backups and hash verification. They have not been uploaded to Steam by this chat; in-game review remains pending.

## Privacy and local state

- Do not include personal names, account handles, owner IDs, personal Workshop item IDs, email addresses or user-specific absolute paths in tracked files or documentation. Use generic placeholders and explicit command arguments.
- Keep local source archives, extraction manifests, game binaries, fonts, backups, deployment packages, credentials and personal runtime state out of Git. Do not copy local identities into examples or generated reports.
- Use an available local Python interpreter; a Windows Store alias may be unusable. Do not record the interpreter's personal absolute path in project documentation.

## Known limits

- Number words still use the engine's English-style spacing and thousand grouping; do not hide this with incorrect magnitude translations.
- The earlier `UXX_Please_review_us` conversation warning remains undiagnosed. Do not invent or remove story text to conceal it.
- Shared minigames include script-generated English fragments, and some shared locations call separate campaign dialogue. Do not claim these are translated solely because the shared files are covered.
- Keep the language selector label `Chinese (Simplified) - Test` in ASCII so it renders before switching to the Chinese font.
- Third-party translations were not incorporated; do not claim ownership or redistribution rights for third-party text, fonts or game artwork.
