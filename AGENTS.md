# Project instructions

## Scope and current work

Build a complete Simplified Chinese localization of Age of Fear: Total, using locale `zh`. Read README.md, docs/LOCALIZATION-PLAN.md, docs/TERMINOLOGY.md and the latest batch notes before editing. Historical batch notes describe earlier states; current instructions take precedence.

- Main messages: 4,215/4,215 content keys translated.
- War Machine: 323/323 current level entries and 52/52 independent dialogue entries (six groups), installed locally on 2026-11-21. Current LevelMachineWar keys come from the Ratmen campaign resource and match XML; five internal fields are excluded. Preserve ratmencampaign namespace without duplicate keys. The antidote task label follows two scripted items instead of the English label’s three; the material hand-in condition does not check tool-route completion (REP-005, runtime untested). See `docs/batches/MACHINE-EXPANSION-BATCH1.md`.
- The Quick and The Dead: 293/293 current level entries and 41/41 independent dialogue entries (four groups), installed locally on 2026-11-21. Current LevelQuickFemaleAssassin keys come from the Ratmen campaign resource and match expansion XML; six internal XML fields are explicitly excluded. Preserve ratmencampaign namespace without duplicate keys. QXX_Rizza_rose has no verified trigger link; the sapphire reward label follows three scripted items instead of the English label’s two. See `docs/batches/QUICK-EXPANSION-BATCH1.md`.
- The Storm Mountain: 536/536 current level entries and 118/118 independent dialogue entries (21 groups), installed locally on 2026-11-21. Current LevelNewSeaPeople keys come from the Vampire Hunter resource and are XML-checked; nine internal XML fields absent from that resource are explicitly excluded. N06_Angela_damage has XML but no verified trigger link. VXX campaign reactions remain separate. See `docs/batches/STORM-EXPANSION-BATCH1.md`; preserve the vampirehuntercampaign namespace without duplicate keys.
- The Victor's Experiment: 238/238 independent conversation keys (27 groups) and 114/114 current level keys translated, installed locally on 2026-11-21. The bundled 99-key level file is outdated; setup_local.py selects the current LevelZombieFranky entries from aof4-vampirehunter/vampirehuntercampaign-en.properties and verifies them against the expansion XML. Keep the vampirehuntercampaign marker and avoid duplicating these keys when main-campaign work reaches them. See `docs/batches/VICTOR-EXPANSION-BATCH1.md`.
- The Blood and Moon: all 21 independent dialogue groups translated (130/130 content keys; expansion dialogue batch 1, installed locally on 2026-11-21). Seven campaign-linked groups contain 76 keys; 14 battle-reaction groups contain 54 keys. All XML fields, seven campaign calls and 14 dialogue-name references in five battle boards checked. See `docs/batches/WEREWOLF-DIALOGUE-BATCH1.md`.
- The Elementalist: all five independent dialogue groups translated (18/18 content keys; expansion dialogue batch 1, installed locally on 2026-11-21), including two battle-reaction groups. XML, riddle outcomes and two dialogue-name references in one battle board checked. See `docs/batches/ELEMENTALIST-DIALOGUE-BATCH1.md`.
- Pirates!: all 18 dialogue groups translated (239/239 content keys; expansion dialogue batches 1–2, installed locally on 2026-11-21), including 14 PXX story groups and four battle-reaction groups. All dialogue XML and four battle-board name references are checked; runtime behavior remains untested. See `docs/batches/PIRATES-DIALOGUE-BATCH2.md`.
- The Quest for Immortality: all 275/275 content keys in `alchemistdlc-conversations` translated (30 groups; expansion dialogue batches 1–3, installed locally on 2026-11-21). This includes seven return-to-game groups (66 keys). Six are defined in aof.jar; AOFFREE has eight source-only keys with no matching XML found in the installed archives, and runtime use is unverified. Scope, archive origins and verification limits are declared in `translation/expansion-coverage.json`; keep this coverage separate from shared/campaign totals. See `docs/batches/ALCHEMIST-DIALOGUE-BATCH3.md`.
- 通用事件 and 通用对话: 3,163/3,163 content keys translated (through shared batch 31; installed locally). Shared conversations are complete at 1,019/1,019; shared events are complete at 2,144/2,144. Separate campaign/expansion dialogue and script-generated English remain outside these totals; follow the user assignment for subsequent work.
- Campaign work starts with Rise of The Necromancer. Undead batches 1–5 cover 251/732 content keys: opening through Level17, U00–U05 dialogue groups, linked UXX groups and the LevelSecret01b defeat-route opening. Continue with Level19, Level19b shop and Level20 / U06 dialogue, checking UXX_Vision_2a and Stonehenge dependencies. Level22/24, defeat-route Level30/33 and base-upgrade campaign dialogue remain separate follow-ups; shared base files belong to the shared-resource workstream. See docs/batches/UNDEAD-CAMPAIGN-BATCH5.md.
- Shared resources and campaign stories are separate workstreams. Follow the current user assignment and preserve the other workstream; do not infer ownership from which chat or branch is active.
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
- For expansion dialogue batches, run `inspection/check_expansion_dialogues.py --game <game-directory>` to verify declared dialogue fields, image-only indices, linked choices and outcomes against the original archive.
- Runtime resources under `pilot-mod/` must use ASCII Java-properties escapes. The engine loads properties through Java `Properties.load(InputStream)`.
- Run `inspection/CheckPilot.java` with the game's Java runtime, the build/package root and relevant English properties files. Check all four font styles, remaining English fallback and engine NBSP/bullet symbols.
- Font configuration uses static regular Noto Sans SC for body/story/effect text and the compact AoF Han UI derivative for button text. Run `prepare_ui_font.py` on the original regular font and `inspection/CheckInventoryLayout.java` to prevent inventory layout collapse. Use `prepare_font.py` for variable-font conversion. Keep local font binaries out of Git; redistribution requires appropriate license materials.
- Verify previous translations are preserved and run `git diff --check`. Update coverage reports, batch notes and CHANGELOG.md accurately.
- In-game testing is deferred while translation proceeds. Automated checks do not establish layout correctness. Do not require a new game test before continuing authorized translation.

## Packaging and collaboration

- Follow CONTRIBUTING.md. Do not overwrite unrelated local edits or another collaborator's translations.
- `prepare_workshop.py` requires the local item path and its actual owner ID. Preserve ownership checks; never hardcode personal account details.
- Back up before an authorized local installation and verify changed files against staging. Packaging does not install or upload automatically.
- Keep Workshop descriptions below the project's 7,999 UTF-8 byte limit and preserve bilingual campaign names and the selected preview.
- Keep the public Workshop description concise and spoiler-free: show broad categories and progress counts only. Do not list story locations, encounters, rewards, recruitable characters or plot outcomes; keep detailed scope in internal batch notes.
- Publishing, uploading and pushing require corresponding user authorization. The local Workshop mod now includes shared batch 31 (3,163 shared keys), Undead batch 5 (251/732), and all completed resources for the eight expansions (2,377 content entries in 12 added runtime files). All 17 installed runtime files match the repository: 10,044 entries including metadata. The latest concise description uses campaign tables and is installed (3,773 UTF-8 bytes). A fresh full backup and whole-folder hash verification preserve existing fonts, licenses, preview and non-description metadata. See `inspection/expansions-installation-validation.json` and `docs/TESTING.md`; historical batch reports retain their pre-installation state. No Steam upload or GitHub push was performed; in-game review remains deferred.

## Privacy and local state

- Do not include personal names, account handles, owner IDs, personal Workshop item IDs, email addresses or user-specific absolute paths in tracked files or documentation. Use generic placeholders and explicit command arguments.
- Keep local source archives, extraction manifests, game binaries, fonts, backups, deployment packages, credentials and personal runtime state out of Git. Do not copy local identities into examples or generated reports.
- Keep the workspace lean: original downloads go under source/reference/; retain the latest rollback backup and active uncommitted-work snapshots, and prune obsolete helpers and superseded backups after verification. Generate workshop-package/ when needed. Preserve translation sources, runtime/font/license inputs and archive-separated English references.
- Use an available local Python interpreter; a Windows Store alias may be unusable. Do not record the interpreter's personal absolute path in project documentation.

## Known limits

- Number words still use the engine's English-style spacing and thousand grouping; do not hide this with incorrect magnitude translations.
- The earlier `UXX_Please_review_us` conversation warning remains undiagnosed. Do not invent or remove story text to conceal it.
- Shared minigames include script-generated English fragments, and some shared locations call separate campaign dialogue. Do not claim these are translated solely because the shared files are covered.
- Keep the language selector label `Chinese (Simplified) - Test` in ASCII so it renders before switching to the Chinese font.
- Third-party translations were not incorporated; do not claim ownership or redistribution rights for third-party text, fonts or game artwork.
