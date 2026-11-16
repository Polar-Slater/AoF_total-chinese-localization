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

The version through shared batch 5 had a successful smoke test. Shared batches 6–7 and Undead batches 1–4 have automated validation but await in-game review. Translation may continue while game testing is deferred.

## Known issues

- Large numbers still follow the engine's English-style grouping and spacing.
- Some minigame fragments come directly from scripts and remain English.
- Some shared locations call campaign dialogue that is not translated yet.
- The earlier `UXX_Please_review_us` loading warning remains undiagnosed.

Automated checks do not prove that every screen fits or every branch works in game. Record what was actually tested in the relevant [batch note](README.md).
