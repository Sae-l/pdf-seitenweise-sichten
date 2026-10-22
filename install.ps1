# Verknüpft diesen Klon in die Skill-Ordner von Claude Code, VS Code/Copilot/Codex und Antigravity.
# Junctions brauchen keine Adminrechte. Zielbasis ist für getrennte Profile und Installationstests optional.
param([string]$Zielbasis = $HOME)
$ErrorActionPreference = 'Stop'
$Name = 'pdf-seitenweise-sichten'
$Src = $PSScriptRoot
$Konflikte = 0

foreach ($dir in "$Zielbasis\.claude\skills", "$Zielbasis\.agents\skills", "$Zielbasis\.gemini\config\skills", "$Zielbasis\.gemini\antigravity-cli\skills") {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    $target = Join-Path $dir $Name
    $item = Get-Item -LiteralPath $target -Force -ErrorAction SilentlyContinue
    if ($item) {
        if ($item.LinkType -and @($item.Target)[0] -eq $Src) {
            Write-Host "bereits verknüpft: $target"
        } else {
            Write-Warning "Konflikt: $target bleibt unverändert; vorhandene Kopie oder fremde Verknüpfung zuerst prüfen"
            $Konflikte++
        }
        continue
    }
    New-Item -ItemType Junction -Path $target -Target $Src | Out-Null
    Write-Host "verknüpft: $target -> $Src"
}

Write-Host "Benötigt Python-Paket: python -m pip install -r `"$Src\scripts\requirements.txt`""
if ($Konflikte) { exit 1 }
