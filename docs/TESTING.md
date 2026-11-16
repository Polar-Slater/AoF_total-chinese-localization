# Validation and game testing

Run commands from the project root after building translations. Prepare the font first; see [setup](SETUP.md).

## Automated checks

```powershell
.\.venv\Scripts\python.exe build_translation.py
& 'C:\path\to\AOFTOTAL\jre\windows64\bin\java.exe' '-Djava.awt.headless=true' inspection/CheckPilot.java pilot-mod source/aof/messages-en.properties source/aof-data/shared-en.properties source/aof-data/shared-conversations-en.properties source/aof-undead/undeadcampaign-en.properties source/aof-undead/undeadcampaign-conversations-en.properties
.\.venv\Scripts\python.exe inspection/check_shared_events.py --game 'C:\path\to\AOFTOTAL'
git diff --check
```

Use `workshop-package` instead of `pilot-mod` to check a staged package. The Java check verifies properties decoding and font coverage for translated text, supplied English fallback resources and engine symbols in four font styles.

## In-game review

After local installation, launch through Steam and select **Options → Screen → Language → Chinese (Simplified) - Test**. Check story pages, dialogue, choices and long tooltips for missing glyphs, clipping and awkward wording.

The version through shared batch 5 had a successful smoke test. Shared batches 6–17 and Undead batches 1–4 have automated validation but await in-game review. Translation may continue while game testing is deferred.

The shared collaborator recorded the following installation before this merge: at the user’s request, shared batches through 17 and the latest description are now synced to the local Workshop folder. This sync changed the two shared properties files and `config.xml`; a full mod backup and SHA-256 checks verified installation and preservation of every other file, including main messages, the existing 45-key Undead opening batch, fonts and preview. The installed package contains 6,472 runtime entries and 2,198 shared content keys. The description stored in XML is 4,911 UTF-8 bytes after newline normalization and trimming, and matched that revision of the description source under the same normalization. The merged development resources contain newer campaign text; this merge does not update the installed package. No Steam upload or new game test was performed. Earlier batch notes and validation reports retain their historical pre-installation state.

## Latest local installation

The subsequent authorized sync installed Undead batches 2–4 alongside shared batches through 17. It updated only the two campaign properties files and the description in config.xml. The installed mod now contains 6,633 runtime entries, including 206 campaign and 2,198 shared content entries. The description is 4,970 UTF-8 bytes after normalization and trimming. A full backup and SHA-256 comparisons verified the changed files against staging and preserved all other installed files. The staged Java check passed for all runtime entries, 1,491 English fallback entries and four font styles. No Steam upload or new in-game test was performed.

The description was subsequently shortened to remove spoilers (3,247 UTF-8 bytes). The supplied Google Fonts static Noto Sans SC Regular font and its OFL license/notice were installed after another full backup; the unused SimHei font was removed. Hash checks verified preservation of all unrelated installed files, and the Java/font checks above passed against the installed folder itself. These local updates have not been uploaded to Steam or reviewed in game.

## Known issues

- The original Shaman's Hut `on-select-42` menu targets hero 107, while its unequip command targets hero 17. Translation preserves the source placeholders; the script mismatch is recorded in shared batch 16 and remains unfixed.
- Large numbers still follow the engine's English-style grouping and spacing.
- Some minigame fragments come directly from scripts and remain English.
- Some shared locations call campaign dialogue that is not translated yet.
- The earlier `UXX_Please_review_us` loading warning remains undiagnosed.

Automated checks do not prove that every screen fits or every branch works in game. Record what was actually tested in the relevant [batch note](README.md).
