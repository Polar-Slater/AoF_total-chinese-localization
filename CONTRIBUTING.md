# Contributing

Read README.md and AGENTS.md before making changes. Coordinate file/batch assignments with the other translator, and follow the glossary in docs/TERMINOLOGY.md.

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

## Combining parallel work

Shared resources and campaign stories are separate workstreams. Keep assignments neutral in tracked instructions: use resource names rather than "this chat", "our work" or "the friend". Follow the user's assignment for the current task.

When merging, preserve the latest changes for each section: shared translations/progress from the shared workstream, and campaign translations/progress from the campaign workstream. Retain both sets of changelog entries and batch notes. Do not accept an entire file solely because its commit is newer; its other sections may be stale. If both contributors changed the same translation key, review its meaning before choosing a value.

Rebuild runtime files and coverage reports with build_translation.py after combining editable sources and coverage declarations. Run the documented validation checks, verify that both sets of translations survive, and update combined progress totals. Keep installation history separate from current repository coverage. This workflow reduces conflicts but does not make shared documentation conflict-free.

Use VERSION as the translation project version, independent of the game version. Record work under Unreleased in CHANGELOG.md; increment the version for agreed milestones. Patch versions cover fixes, minor versions cover translation batches/features, and 1.0.0 is reserved for the agreed complete release.
