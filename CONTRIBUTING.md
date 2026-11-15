# Contributing

Read README.md and AI-HANDOFF.md before making changes. Coordinate file/batch assignments with the other translator, and follow the glossary in PHASE1-NOTES.md.

```powershell
git switch main
git pull --ff-only
git switch -c translation/your-batch
```

Edit UTF-8 files in translation/. Keep keys, placeholders and functional HTML intact. Register new UI batch files in build_translation.py. Run the build using your local Python environment and review the resulting diff. Include regenerated UI properties and validation report when they change. Check layout in game when possible; document checks you could not run.

```powershell
git diff --check
git diff
git add translation/ pilot-mod/ inspection/phase1-validation.json CHANGELOG.md
git commit -m "Translate the next interface batch"
git push -u origin translation/your-batch
```

Add any other intentionally changed scripts/docs explicitly. Open a pull request into main and summarize scope and validation. After merging, both collaborators update main with git pull --ff-only. Avoid force-pushing shared branches. If the same lines changed, resolve the translations together before merging.

Do not add game resources, font files, saves, account credentials, backups or personal environment files. Workshop publishing is a separate action from GitHub collaboration.

Use VERSION as the translation project version, independent of the game version. Record work under Unreleased in CHANGELOG.md; increment the version for agreed milestones. Patch versions cover fixes, minor versions cover translation batches/features, and 1.0.0 is reserved for the agreed complete release.
