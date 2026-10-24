# PDF-Unterlagen gezielt sichten

**Die richtige Seite finden. Den relevanten Text lesen. Am Original prüfen.**

Ein Agent-Skill mit lokalem Python-Werkzeug für Vorlesungsfolien, Übungsblätter und Formelsammlungen. Ein kompakter Seitenindex führt zur Quelle, ohne den gesamten PDF-Volltext in den Gesprächskontext zu laden.

![Drei Schritte: im Seitenindex finden, einen Textabschnitt lesen und Formeln oder Abbildungen an der Originalseite prüfen.](docs/assets/ablauf.svg)

[Schnellstart](#schnellstart) · [Als Skill nutzen](#als-skill-nutzen) · [Prüfstand](#prüfstand) · [Änderungen](CHANGELOG.md) · [MIT-Lizenz](LICENSE)

**Version 1.5.0:** [Release und Skill-ZIP](https://github.com/Sae-l/pdf-seitenweise-sichten/releases/tag/v1.5.0) · [Release-Hinweise](docs/releases/v1.5.0.md)

**Neu in 1.5.0:** begrenzte Suche, seitenweises Lesen, getrennte Arbeitsfassungen und erweiterte Integritätsprüfung. Bestehende Installationen werden nicht automatisch aktualisiert. Anleitung: [Gezielte Nutzung](references/gezielte-nutzung.md), Messungen und Grenzen: [Umsetzungsnachweis](docs/umsetzung-pdf-werkzeug-2026-10-24.md).

Das Release baut auf der portablen Projektinstallation auf und ergänzt die gezielte PDF-Nutzung. Die [Umsetzungsnachweise](docs/umsetzung-pdf-werkzeug-2026-10-24.md) trennen lokale Prüfungen, Bildstichproben und offene Agent-Endabnahmen; der [Abnahmebericht zu v1.4.0](docs/plattformabnahme-v1.4.0.md) bleibt ein historischer Nachweis.

## Was du bekommst

| Nutzen | Umsetzung |
| --- | --- |
| Gezielter Kontext | Ein Seitenindex und Markdown mit eindeutig nummerierten PDF-Seiten statt ungezieltem Volltextimport. |
| Nachvollziehbare Aussagen | Dokument und PDF-Seite als Quelle; Formeln, Tabellen und Zeichnungen werden am Original geprüft. |
| Wiederverwendbare Arbeit | SHA-256 erkennt geänderte PDFs. `--alt` übernimmt Sichtungsnachweise nur bei identischem vorhandenem Hash. |
| Geschützte Ergebnisse | Originale werden nur gelesen. Vorhandene Indizes und Manifeste werden nicht überschrieben. |
| Lokale Verarbeitung | Das Python-Werkzeug extrahiert und rendert lokal, ohne einen Cloud-Dienst aufzurufen. |

**Zwei Bausteine:** [SKILL.md](SKILL.md) steuert die Arbeit eines Agenten. [scripts/sichtung.py](scripts/sichtung.py) erledigt Extraktion, Prüfung und Rendering und funktioniert auch ohne Agent. Welche Inhalte ein Agent an seinen Anbieter sendet, hängt von dessen Umgebung ab.

## Schnellstart

Voraussetzungen: Git und Python 3.12 oder neuer. Die CI ist für Python 3.12 auf Windows und Linux eingerichtet; den tatsächlichen Laufstatus zeigt [GitHub Actions](https://github.com/Sae-l/pdf-seitenweise-sichten/actions/workflows/checks.yml).

```sh
git clone https://github.com/Sae-l/pdf-seitenweise-sichten.git
cd pdf-seitenweise-sichten
python -m pip install -r scripts/requirements.txt
```

Unter macOS/Linux gegebenenfalls `python3` statt `python` verwenden. Ein vorhandenes virtuelles Python-Environment kann direkt genutzt werden.

Lege die PDFs eines Themenbereichs in einen Quellordner. Die folgenden Befehle laufen im geklonten Repository; passe die beiden Beispielpfade an:

```sh
# 1. Einen neuen Sichtungsordner erzeugen
python scripts/sichtung.py extract "../Unterlagen" "../Unterlagen_Sichtung"

# 2. Aktualität und Seitenfolge prüfen
python scripts/sichtung.py check "../Unterlagen_Sichtung"

# 3. Bei Bedarf nur PDF-Seite 7 rendern
python scripts/sichtung.py render "../Unterlagen/Mechanik.pdf" 7 "../Arbeitsbilder" --scale 3
```

Der Quellordner wird unmittelbar nach PDFs durchsucht, ohne Unterordner rekursiv zu verarbeiten. Verwende für die Ausgabe einen eigenen Ordner außerhalb der Quellen.

```text
Unterlagen_Sichtung/
├── Seitenindex.md       # Dokumente, Seitenvorschau und Warnhinweise
├── manifest.json        # PDF-Hashes und Sichtungsstatus je Seite
├── md/                  # Extrahierter Text mit „## PDF-Seite N“
└── bilder/              # Automatische Bilder bei wenig oder beschädigtem Text
```

Byte-identische PDFs werden nur einmal indiziert. `check` beendet sich mit einem Fehlerstatus, wenn PDFs neu, geändert oder entfernt sind, der Seitenindex, Prüfsummen oder Markdown-Dateien fehlen oder Seitenabschnitte nicht stimmen.

### Gezielt suchen, lesen und wiederverwenden

```sh
python scripts/sichtung.py search "../Unterlagen_Sichtung" "Kraft Beschleunigung"
python scripts/sichtung.py read "../Unterlagen_Sichtung" "Mechanik.pdf" 7
python scripts/sichtung.py save "../Unterlagen_Sichtung" "Mechanik.pdf" 7 "Kraft.md" --status original-geprüft
python scripts/sichtung.py read "../Unterlagen_Sichtung" "Mechanik.pdf" 7 --arbeitsfassung
```

Die Arbeitsdatei `Kraft.md` vorher anhand der Quelle erstellen; das Werkzeug erzeugt oder bestätigt ihren Inhalt nicht selbst. Auch Text, CSV, LaTeX, PNG und JPEG sind möglich. `save` speichert die Datei mit Quellen- und Inhaltshashes und schützt vorhandene Arbeitsfassungen. Es setzt keine Sichtungsmarken automatisch.

`search` gibt standardmäßig höchstens fünf kurze Treffer aus. `read` liefert eine Seite, bei mehr als 12 000 Zeichen mit ausdrücklicher Fortsetzungsposition. Beide prüfen den Bestand vorher. Lösungsbereiche bleiben standardmäßig ausgeblendet; `--mit-antworten` bezieht sie ausdrücklich ein. Die Erkennung ist heuristisch und ersetzt keinen sorgfältigen Umgang mit ungekennzeichneten Lösungen oder ganzen Seitenbildern. Scans und Bildinhalte sind ohne passenden Text nicht zuverlässig durchsuchbar.

Der erweiterte `check` prüft auch Manifest-/Index-Seitenlisten, tatsächliche PDF-Seitenzahlen, Bildpfade und Markdown-Linkziele. Neue Extraktionen schützen zusätzlich ihren Rohtext per SHA-256; ältere Bestände erhalten einen Hinweis auf den fehlenden Rohtextnachweis. Korrekturen gehören in die getrennte Arbeitsfassung. `render` verwendet unveränderte Bilder anhand eines JSON-Nachweises erneut und überschreibt abweichende bestehende Bilder nicht; dann einen neuen Bildordner wählen.

### Wenn sich die Unterlagen ändern

```sh
python scripts/sichtung.py extract "../Unterlagen" "../Unterlagen_Sichtung_neu" --alt "../Unterlagen_Sichtung"
```

Vergleiche die neue Ausgabe mit der bisherigen, bevor du sie übernimmst. Ohne alten Hash werden keine alten Prüfmarken oder Bilder übernommen. Die alte Ausgabe bleibt erhalten.

## Als Skill nutzen

### Empfohlen: portabel im Zielprojekt

```sh
python scripts/install_projekt.py "../Mein-Projekt"
```

Das vorhandene Zielprojekt erhält zwei eigenständige Skill-Kopien: `.agents/skills/pdf-seitenweise-sichten/` für Codex, Antigravity, VS Code/Copilot und GitHub Copilot sowie `.claude/skills/pdf-seitenweise-sichten/` für Claude Code. Beide enthalten Anweisungen, Skripte und Referenzen. Bestehende Ziele führen zum Abbruch; Updates erst vergleichen und sichern. Die Kopien aktualisieren sich nicht durch `git pull` im ursprünglichen Klon.

Für GitHub Copilot Cloud die erzeugten Skill-Dateien im Zielrepository committen und die Python-Abhängigkeiten in dessen Agent-Umgebung installieren. Globale Verknüpfungen und Laufwerkspfade deines Rechners sind in der Cloud nicht verfügbar. Dieses Repository bringt dafür einen schlanken `.github/skills/`-Einstieg und [Copilot-Setup-Schritte](.github/workflows/copilot-setup-steps.yml) mit. Das Setup anderer Projekte muss deren bestehende Abhängigkeiten berücksichtigen; es wird nicht automatisch überschrieben.

### Alternativ: ein lokaler Klon für mehrere Werkzeuge

Ein Klon kann mit den Skill-Verzeichnissen mehrerer lokaler Werkzeuge verknüpft werden:

| System | Im Repository ausführen |
| --- | --- |
| Windows | `powershell -File install.ps1` |
| macOS / Linux | `bash install.sh` |

Die Skripte verknüpfen nach `~/.claude/skills/`, `~/.agents/skills/`, `~/.gemini/config/skills/` (Antigravity App/IDE) und `~/.gemini/antigravity-cli/skills/` (Antigravity CLI). Bestehende passende Verknüpfungen sind wiederverwendbar. Echte Kopien und fremde Verknüpfungen bleiben unverändert und führen zu einem Fehlerstatus. Eine ältere Installation unter `~/.codex/skills/` separat prüfen, damit keine veraltete Kopie geladen wird. Die Python-Abhängigkeiten werden über den Schnellstart installiert.

Wenn Windows `.ps1` blockiert, nutze die portable Python-Projektinstallation. Ändere dafür keine Ausführungsrichtlinie. Welche Pfade und Funktionen dein Werkzeug unterstützt, ist in [Plattformen und Installation](Obsidian-Plan/31%20Plattformen%20und%20Installation.md) mit offiziellen Quellen und dem jeweiligen Prüfstand dokumentiert.

Beispielauftrag nach dem Laden des Skills:

```text
$pdf-seitenweise-sichten
Finde in ../Unterlagen die Aufgabe zum schiefen Wurf.
Nenne Dokument, PDF-Seite und Aufgabennummer. Prüfe die Formel
am Originalbild und verrate noch keine Endantwort.
```

In Codex den Skill über `$pdf-seitenweise-sichten` wählen. Claude Code, Antigravity und VS Code/Copilot unterstützen `/pdf-seitenweise-sichten`. In GitHub Copilot den Skill-Namen und den Auftrag ausdrücklich nennen. Die verfügbaren Werkzeuge und Berechtigungen der jeweiligen Agent-Umgebung bleiben Voraussetzung; ein geladener Skill allein bestätigt keine Bildsichtung.

`git pull` im Klon aktualisiert verknüpfte Installationen gemeinsam. Für einen festgelegten Stand einen geprüften Commit oder vorhandenen Tag verwenden.

## Prüfstand

| Bereich | Nachweis und Grenze |
| --- | --- |
| Automatische Tests | [Selbsttest](scripts/selbsttest.py): Extraktion, Duplikate, Rendering, Änderungsprüfung, Statusübernahme und Schutz vorhandener Ergebnisse. Die [CI](.github/workflows/checks.yml) ist für Windows und Linux eingerichtet. |
| Plattformbereitstellung | [Plattformtest](scripts/plattformtest.py): portable Pakete, Ausführung aus anderem Arbeitsordner, native Installer, Wiederholung und Konfliktschutz. In der CI dürfen diese Tests nicht übersprungen werden. Das ersetzt keine Endabnahme in den fünf Agent-Oberflächen. |
| Skill-Format | Formale Validierung des aktuellen Arbeitsstands bestanden; Details in [ARCHIVE.json](ARCHIVE.json). |
| Dokumentation | [Vault-Prüfung](Obsidian-Plan/Pruefung/vault_pruefen.py) prüft Verknüpfungen, Erreichbarkeit und Manifest. [SHA256SUMS](SHA256SUMS) dokumentiert die aufgeführten Repository-Dateien. |
| Reale Unterlagen | v1.3.0 wurde an CuD-Unterlagen und zwei weiteren PDF-Sätzen erprobt. Messgrundlage und Grenzen stehen in [Ist-Stand und Messung](Obsidian-Plan/20%20Ist-Stand%20und%20Messung.md). Diese Ergebnisse gelten nicht automatisch für spätere Änderungen. |
| Offene Nachweise | Synthetische Lesetests in Codex und Claude Code sind dokumentiert. Vollständige Endabnahmen aller fünf Agenten und erneute reale PDF-Messungen bleiben offen; siehe [Abnahmebericht](docs/plattformabnahme-v1.4.0.md). |

Die Zustände **indiziert**, **als Text gelesen**, **im Originalbild angesehen** und **fachlich geprüft** bleiben getrennt. Erzeugte Bilder gelten nicht automatisch als angesehen. Auch eine Bildsichtung beweist keine mathematische Richtigkeit.

### Prüfungen selbst ausführen

```sh
python -m pip install reportlab
python scripts/selbsttest.py
python scripts/plattformtest.py
python Obsidian-Plan/Pruefung/vault_pruefen.py
```

Die Tests erzeugen eigene kleine PDF-Dateien in einem temporären Verzeichnis; fremde Lehrunterlagen werden dafür nicht benötigt.

## Aufbau und Weiterentwicklung

| Einstieg | Inhalt |
| --- | --- |
| [SKILL.md](SKILL.md) | Verbindlicher Ablauf, Quellenangaben und Umgang mit Unsicherheit |
| [scripts/](scripts/) | CLI, Abhängigkeiten und Selbsttest |
| [Projektbeispiel](references/beispiel-formelsammlung.md) | Zuordnung von Quellen und Sichtungsordnern |
| [Plan und Nachweise](Obsidian-Plan/00%20Start.md) | Entscheidungen, Messungen und offene Schritte; auch direkt auf GitHub lesbar |
| [Repository-Konfiguration](docs/repository-konfiguration.md) | Schutzregeln, CI-Berechtigungen und Release-Prüfweg |
| [CHANGELOG.md](CHANGELOG.md) | Änderungen je Version |

Version 1.5.0 ergänzt gezielte Suche, Seitenzugriff und wiederverwendbare Arbeitsfassungen. Für eine festgelegte Installation `v1.5.0` auschecken. Die [Release-Action](.github/workflows/release.yml) prüft Selbsttest, Vault, Repository-Prüfsummen und Tag-Version, baut ein Skill-ZIP und legt einen Release-Entwurf an. Nach Download und Vergleich mit dem getaggten Quellstand wird dieser veröffentlicht.

Im Release liegen das Skill-ZIP und eine separate `SHA256SUMS` für dessen Download. Die gleichnamige Datei im Repository prüft dagegen die darin aufgeführten Quelldateien. Der ZIP-Inhalt ist für die Skill-Installation gedacht; Dokumentation und Installationsskripte stehen im vollständigen Repository. Eine ZIP-Datei bestätigt noch keine Kompatibilität mit jeder Agent-Oberfläche.

Fehler oder Verbesserungen? Eröffne ein [Issue](https://github.com/Sae-l/pdf-seitenweise-sichten/issues) mit Befehl, Betriebssystem, Python-Version und beobachtetem Ergebnis. Für PDF-Probleme möglichst eine kleine, selbst erstellte Beispieldatei verwenden. Änderungen am Verhalten bitte mit einem passenden Selbsttest und Changelog-Eintrag einreichen.

## Lizenz und Herkunft

[MIT](LICENSE) für den eigenen Code und die Dokumentation dieses Repositorys. Die Lizenz erteilt keine Rechte an fremden PDF-Unterlagen, deren Texten oder Abbildungen. Originalunterlagen und ihre Extraktionen verbleiben im jeweiligen Quellprojekt.

Entstanden am 12.10.2026 aus dem Formelsammlungsprojekt von [Sae-l](https://github.com/Sae-l). Der Schwerpunkt liegt auf belegbarer Quellensichtung; PDF-Erstellung und automatische fachliche Freigabe gehören nicht zum Umfang.
