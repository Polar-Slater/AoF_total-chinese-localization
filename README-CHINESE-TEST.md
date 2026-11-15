# Simplified Chinese pilot

**Current status:** Phase 1 expands the pilot with 481 translated menu/settings/control entries. See [PHASE1-NOTES.md](PHASE1-NOTES.md) for scope, checks and testing. The original pilot notes below describe the initial compatibility test.

## Workshop Manager (preferred)

The pilot is installed in Workshop item `3840511924`, titled `Age of Fear Total - Simplified Chinese (Test)`. Restart Workshop Manager to refresh the title, then use its Run Validation button. Launch the game normally through Steam and select **Chinese (Simplified) - Test**. The ASCII language label is deliberate: the English selector font cannot render the original Chinese label before switching languages.

The other author's `Chinese` entry is separate (`cn` versus our `zh`). This package does not incorporate that author's translation. It remains a small compatibility pilot, not a full translation. Nothing was uploaded to Steam. The original item was backed up under `backups/workshop-3840511924-before-install` and the installed files were compared byte-for-byte to `workshop-package`.

The package includes a valid 800 x 450 preview, metadata retaining your owner ID, three translation files and the local test font. Do not publish this local-font test package; a release needs a redistributable font.

## Try the test

1. Close the game and keep Steam running.
2. Double-click `launch-chinese-test.bat` in this project folder.
3. In the game's language selection, choose `Chinese (Simplified) - Test`. If necessary, open Configuration to find the language setting.
4. Check the menu buttons for Chinese text, missing-character boxes, and clipping.
5. Find the Undead campaign: its title should read `死灵法师的崛起`, with a Chinese description. Sample early Krill/Goblin dialogue is also translated.
6. Report what displays correctly and any problems. Most text is intentionally still English.

The launcher uses the installed game's original classpath and Java flags, with a JVM `game.home` override pointing at this project's `pilot-home`. Test settings and saves are separate from the normal game profile. Start through Steam as usual to return to your normal profile. The installation and existing profile were not edited.

## Contents and validation

- `source/`: 62 English resource files extracted without modification, separated by source archive to preserve duplicate filenames. `manifest.json` records origins and SHA-256 hashes. These source copies must be reconciled against runtime resource precedence before full translation.
- `translation/`: editable UTF-8 pilot files.
- `pilot-mod/`: 3 runtime properties files using ASCII Unicode escapes, plus a local copy of the PC's SimHei font.
- `pilot-home/config.properties`: lookup-folder settings.
- `inspection/`: loader bytecode inspection and a Java decoding/glyph check.
- `prepare_pilot.py`: reproduces extraction and pilot from its embedded translations; running it overwrites the pilot and editable files.

Verified in this installed build: the localization loader calls `Properties.load(InputStream)`; font loading calls `Font.createFont` on a resource stream. Its system-language detection uses `Locale.getLanguage()`, so this pilot uses `zh`. This does not separately identify Simplified and Traditional Chinese.

The bundled Java runtime decoded all 51 pilot entries and confirmed font coverage for every character. Translation keys were checked against the corresponding English source. In-game loading, fallback and layout still need testing.

The SimHei copy is for this local test. A distributed Workshop release should use a font with redistribution permission and include its license.
