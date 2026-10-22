# Verknüpft diesen Klon in die Skill-Ordner von Claude Code, VS Code/Copilot/Codex und Antigravity.
# Junctions brauchen keine Adminrechte. Aktualisieren: im Klon `git pull`.
$ErrorActionPreference = 'Stop'
$Name = 'pdf-seitenweise-sichten'
$Src = $PSScriptRoot

foreach ($dir in "$HOME\.claude\skills", "$HOME\.agents\skills", "$HOME\.gemini\config\skills") {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    $target = Join-Path $dir $Name
    if (Test-Path -LiteralPath $target) {
        $item = Get-Item -LiteralPath $target -Force
        if (-not $item.LinkType) {
            Write-Warning "übersprungen: $target ist eine echte Kopie, keine Verknüpfung - erst sichern und entfernen"
            continue
        }
        $item.Delete()  # entfernt nur die Verknüpfung, nicht den Inhalt des Klons
    }
    New-Item -ItemType Junction -Path $target -Target $Src | Out-Null
    Write-Host "verknüpft: $target -> $Src"
}

Write-Host "Benötigt Python-Paket: python -m pip install -r `"$Src\scripts\requirements.txt`""
