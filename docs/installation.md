# Installation und Updates

[Zur Startseite](../README.md) · [Nutzungsbeispiele](../references/gezielte-nutzung.md)

## Welcher Weg passt?

| Ziel | Empfohlener Einstieg |
| --- | --- |
| Das Werkzeug ohne Agenten nutzen | Repository klonen, Python-Abhängigkeiten bereitstellen, CLI verwenden |
| Den Skill in einem Projekt nutzen | Portable Projektkopien mit `install_projekt.py` erzeugen |
| Einen festen Stand ohne Git herunterladen | Skill-ZIP aus dem [Release v1.5.0](https://github.com/Sae-l/pdf-seitenweise-sichten/releases/tag/v1.5.0) entpacken |
| Einen Klon für mehrere lokale Agenten verwenden | Globale Verknüpfungen aus dem vollständigen Repository einrichten |
| GitHub Copilot Cloud verwenden | Skill-Dateien und geeignete Quellen im Zielrepository bereitstellen |

## Voraussetzungen

Python 3.12 oder neuer; für den Klon zusätzlich Git. Benötigte Pakete stehen in `scripts/requirements.txt`: `pypdfium2` und `Pillow`. Ein vorhandenes virtuelles Python-Environment kann genutzt werden. `reportlab` ist nur für Tests erforderlich.

```sh
git clone --branch v1.5.0 --depth 1 https://github.com/Sae-l/pdf-seitenweise-sichten.git
cd pdf-seitenweise-sichten
python -m pip install -r scripts/requirements.txt
```

Unter macOS/Linux gegebenenfalls `python3` verwenden. Die CLI-Aufrufe stehen im [Schnellstart](../README.md#schnellstart).

## Portable Projektinstallation

```sh
python scripts/install_projekt.py "../Mein-Projekt"
```

Das Zielprojekt muss bereits existieren. Der Installer erzeugt zwei vollständige Kopien:

- `.agents/skills/pdf-seitenweise-sichten/`
- `.claude/skills/pdf-seitenweise-sichten/`

Sie enthalten Anweisung, Skripte, Referenzen, Lizenz und Versionsnachweis. Bestehende Ziele führen zum Abbruch. Ein `git pull` im ursprünglichen Klon aktualisiert solche Kopien nicht.

Den Skill im jeweiligen Agenten aktivieren. Für Codex ist `$pdf-seitenweise-sichten` vorgesehen, für Claude Code `/pdf-seitenweise-sichten`. Weitere Pfade und Aktivierungswege sowie der getrennte Prüfstand stehen unter [Plattformen und Installation](../Obsidian-Plan/31%20Plattformen%20und%20Installation.md). Bereitstellung allein ist keine vollständige Agent-Abnahme.

## ZIP verwenden

Lade das Skill-ZIP und `SHA256SUMS` von derselben Release-Seite herunter und vergleiche den ZIP-Hash. Beispielsweise mit PowerShell:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath .\pdf-seitenweise-sichten-v1.5.0.zip
```

Nach dem Entpacken im enthaltenen Skill-Ordner die Python-Abhängigkeiten bereitstellen und bei Bedarf `scripts/install_projekt.py` ausführen. Das ZIP enthält `SKILL.md`, `LICENSE`, `ARCHIVE.json`, `scripts/` und `references/`. README, globale Installer und Plan-Vault gehören zum vollständigen Repository. Die vollständigen Plattformtests deshalb aus dem Repository ausführen.

## Globale Verknüpfungen

Aus dem vollständigen Repository:

| System | Befehl |
| --- | --- |
| Windows | `powershell -File install.ps1` |
| macOS / Linux | `bash install.sh` |

Die Skripte verknüpfen den Klon mit `.claude/skills/`, `.agents/skills/`, `.gemini/config/skills/` und `.gemini/antigravity-cli/skills/` im Benutzerprofil. Passende vorhandene Links sind wiederverwendbar. Echte Kopien oder fremde Verknüpfungen bleiben unverändert und führen zu einem Fehlerstatus.

Blockiert Windows `.ps1`, die portable Python-Projektinstallation verwenden. Dafür keine Ausführungsrichtlinie ändern. Ältere Kopien unter `.codex/skills/` separat vergleichen, damit nicht unbeabsichtigt ein alter Stand geladen wird.

Ein fest auf `v1.5.0` ausgecheckter Klon bleibt bei diesem Stand. Wer bewusst den Entwicklungszweig nutzt, kann verknüpfte Installationen über dessen Updates gemeinsam aktualisieren; vorher Änderungen und Prüfnachweise vergleichen.

## GitHub Copilot Cloud

Die erzeugten Skill-Dateien im Zielrepository committen und die Python-Abhängigkeiten in dessen Agent-Umgebung installieren. Quellen müssen dort vorhanden und freigegeben sein; lokale Laufwerkspfade und persönliche globale Links sind in der Cloud nicht verfügbar.

Dieses Repository enthält einen [GitHub-Einstieg](../.github/skills/pdf-seitenweise-sichten/SKILL.md) und [Copilot-Setup-Schritte](../.github/workflows/copilot-setup-steps.yml). Das Setup anderer Projekte gezielt ergänzen, nicht ersetzen. Ein Setup-Lauf bestätigt keinen vollständigen Agent-Auftrag oder Bildzugriff.

## Sicher aktualisieren

1. Vorhandene Version, eigene Ergänzungen und Sichtungsnachweise vergleichen und sichern.
2. Neuen Stand separat bereitstellen und prüfen. Bestehende Kopien werden nicht automatisch überschrieben.
3. Bei geänderten PDF-Quellen in einen neuen Sichtungsordner extrahieren:

```sh
python scripts/sichtung.py extract "../Unterlagen" "../Unterlagen_Sichtung_neu" --alt "../Unterlagen_Sichtung"
```

Alte Sichtung erhalten, Ergebnisse vergleichen und erst danach übernehmen. Status und Bilder werden nur bei gleicher vorhandener Quellenprüfsumme übernommen; Arbeitsfassungen werden nicht automatisch migriert.
