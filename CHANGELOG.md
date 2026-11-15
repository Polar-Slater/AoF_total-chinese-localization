# Changelog

Project versions describe translation milestones, not game versions.

## [Unreleased]

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
