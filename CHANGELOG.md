# Changelog

Project versions describe translation milestones, not game versions.

## [Unreleased]

- No changes yet.

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
