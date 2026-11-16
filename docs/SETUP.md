# Setup and packaging

Run commands from the project root. Replace example paths and IDs with your own local values; keep those values out of tracked files.

## Prepare the project

Follow the [README](../README.md) to install Python dependencies, extract English references and build translations. `setup_local.py` reads your game installation and writes ignored files under `source/`.

To prepare the configured Noto Sans SC font:

```powershell
.\.venv\Scripts\python.exe prepare_font.py 'C:\path\to\NotoSansSC-VF.ttf'
```

This produces a static regular-weight font for Java. Fonts are optional for text-only editing, but required for font checks and packaging. Font binaries stay local; include the appropriate license materials before distributing them.

The Google Fonts Noto Sans SC ZIP also includes `static/NotoSansSC-Regular.ttf`. This static weight-400 font can be copied unchanged to `pilot-mod/com/aof/resource/text/font/noto-sans-sc.ttf`, without conversion. The current local package uses this option. Its matching `OFL.txt` and a provenance notice are included under `pilot-mod/licenses/NotoSansSC/` and copied into the Workshop package. Preserve these files when distributing the font. Keep the downloaded ZIP out of Git and remove obsolete test fonts from staging before packaging.

## Build translations

```powershell
.\.venv\Scripts\python.exe build_translation.py
```

Edit `translation/`, not generated files in `pilot-mod/`. Register main/shared batch files in the build script. Declare complete groups in `translation/shared-coverage.json` or `translation/campaign-coverage.json` as appropriate. The build checks keys, placeholders, markup and coverage, then generates Java-compatible properties files.

## Prepare a local Workshop package

Create a local item in Workshop Manager first. Use its directory and the actual `owner-user-id` from its `config.xml`:

```powershell
.\.venv\Scripts\python.exe prepare_workshop.py --item 'C:\path\to\workshop\item' --owner-id 'YOUR_OWNER_ID'
```

The script builds `workshop-package/` and backs up the existing item. It does not install or upload. Validate the package using the [testing guide](TESTING.md), then back up and verify files when installing locally.

## Update a local description

Edit `workshop-assets/description.txt`, then preview the change:

```powershell
.\update-workshop-description.ps1 -ItemConfig 'C:\path\to\workshop\item\config.xml' -OwnerId 'YOUR_OWNER_ID' -WhatIf
```

Remove `-WhatIf` to apply it. The helper checks ownership and the 7,999 UTF-8 byte limit, backs up existing configs, and updates local installed/staged metadata. It does not upload to Steam.

## Local files

`source/`, `backups/`, `workshop-package/`, `pilot-home/` and fonts are excluded from Git. The optional game modding guide belongs in `source/reference/`. Keep account IDs and personal paths out of project documentation and reports.

`prepare_pilot.py` is a historical bootstrap, not the current build workflow. Do not run it over ongoing translation work.
