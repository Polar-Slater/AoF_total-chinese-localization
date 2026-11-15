param(
    [Parameter(Mandatory = $true)][string]$ItemConfig,
    [Parameter(Mandatory = $true)][string]$OwnerId
)
$ErrorActionPreference = 'Stop'
$descriptionFile = Join-Path $PSScriptRoot 'workshop-assets\description.txt'
$descriptionText = [System.IO.File]::ReadAllText($descriptionFile, [System.Text.Encoding]::UTF8).Trim()
if ($descriptionText.Length -lt 5 -or $descriptionText.Length -gt 8000) {
    throw 'Description must contain 5-8000 characters.'
}
[xml]$configDocument = [System.IO.File]::ReadAllText($itemConfig)
if ($configDocument.'workshop-item'.'owner-user-id' -ne $OwnerId) {
    throw 'Unexpected Workshop owner ID. No changes made.'
}
$backupFolder = Join-Path $PSScriptRoot 'backups'
New-Item -ItemType Directory -Force -Path $backupFolder | Out-Null
Copy-Item -LiteralPath $itemConfig -Destination (Join-Path $backupFolder ('description-config-' + (Get-Date -Format 'yyyyMMdd-HHmmssfff') + '.xml'))
$configDocument.'workshop-item'.description = $descriptionText
$configDocument.Save($itemConfig)
$packageConfig = Join-Path $PSScriptRoot 'workshop-package\config.xml'
$configDocument.Save($packageConfig)
Write-Host 'Description updated locally. Nothing was uploaded to Steam.'
