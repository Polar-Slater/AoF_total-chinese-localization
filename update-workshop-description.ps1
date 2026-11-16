[CmdletBinding(SupportsShouldProcess = $true)]
param(
    [Parameter(Mandatory = $true)][string]$ItemConfig,
    [Parameter(Mandatory = $true)][string]$OwnerId
)
$ErrorActionPreference = 'Stop'
$descriptionFile = Join-Path $PSScriptRoot 'workshop-assets\description.txt'
$descriptionText = [System.IO.File]::ReadAllText($descriptionFile, [System.Text.Encoding]::UTF8).Trim()
$descriptionBytes = [System.Text.Encoding]::UTF8.GetByteCount($descriptionText)
# Steam's 8000-byte buffer: reserve one byte for the terminating NUL.
if ($descriptionText.Length -lt 5 -or $descriptionBytes -gt 7999) {
    throw "Description must contain at least 5 characters and at most 7999 UTF-8 bytes; got $descriptionBytes bytes."
}
[xml]$configDocument = [System.IO.File]::ReadAllText($itemConfig)
if ($null -eq $configDocument.SelectSingleNode('/workshop-item/description')) {
    throw 'Workshop config is missing its description element. No changes made.'
}
if ($configDocument.'workshop-item'.'owner-user-id' -ne $OwnerId) {
    throw 'Unexpected Workshop owner ID. No changes made.'
}
$backupFolder = Join-Path $PSScriptRoot 'backups'
$packageConfig = Join-Path $PSScriptRoot 'workshop-package\config.xml'
if (-not $PSCmdlet.ShouldProcess("$ItemConfig and $packageConfig", "Update local description ($descriptionBytes UTF-8 bytes)")) {
    return
}
# Prepare output directories before changing the installed item.
New-Item -ItemType Directory -Force -Path (Split-Path -Parent $packageConfig) | Out-Null
New-Item -ItemType Directory -Force -Path $backupFolder | Out-Null
$backupId = (Get-Date -Format 'yyyyMMdd-HHmmssfff') + '-' + [guid]::NewGuid().ToString('N')
$installedBackup = Join-Path $backupFolder ('description-config-' + $backupId + '.xml')
$packageBackup = Join-Path $backupFolder ('description-package-' + $backupId + '.xml')
$packageExisted = Test-Path -LiteralPath $packageConfig
Copy-Item -LiteralPath $itemConfig -Destination $installedBackup
if ($packageExisted) {
    Copy-Item -LiteralPath $packageConfig -Destination $packageBackup
}
$configDocument.'workshop-item'.description = $descriptionText
try {
    $configDocument.Save($itemConfig)
    $configDocument.Save($packageConfig)
} catch {
    # Restore the installed metadata if either output cannot be saved.
    Copy-Item -LiteralPath $installedBackup -Destination $itemConfig -Force
    if ($packageExisted) {
        Copy-Item -LiteralPath $packageBackup -Destination $packageConfig -Force
    } elseif (Test-Path -LiteralPath $packageConfig -PathType Leaf) {
        Remove-Item -LiteralPath $packageConfig
    }
    throw
}
Write-Host "Description updated locally ($descriptionBytes UTF-8 bytes). Nothing was uploaded to Steam."
