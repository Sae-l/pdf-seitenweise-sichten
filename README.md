# PDF-Unterlagen gezielt sichten

**Die richtige Seite finden. Den relevanten Text lesen. Am Original prüfen.**

Ein Agent-Skill mit lokalem Python-Werkzeug für Vorlesungsfolien, Übungsblätter und Formelsammlungen. Ein kompakter Seitenindex führt zur Quelle, ohne den gesamten PDF-Volltext in den Gesprächskontext zu laden.

![Drei Schritte: im Seitenindex finden, einen Textabschnitt lesen und Formeln oder Abbildungen an der Originalseite prüfen.](docs/assets/ablauf.svg)

[Schnellstart](#schnellstart) · [Als Skill nutzen](#als-skill-nutzen) · [Prüfstand](#prüfstand) · [Änderungen](CHANGELOG.md) · [MIT-Lizenz](LICENSE)

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

Byte-identische PDFs werden nur einmal indiziert. `check` beendet sich mit einem Fehlerstatus, wenn PDFs neu, geändert oder entfernt sind, Prüfsummen oder Markdown-Dateien fehlen oder Seitenabschnitte nicht stimmen.

### Wenn sich die Unterlagen ändern

```sh
python scripts/sichtung.py extract "../Unterlagen" "../Unterlagen_Sichtung_neu" --alt "../Unterlagen_Sichtung"
```

Vergleiche die neue Ausgabe mit der bisherigen, bevor du sie übernimmst. Ohne alten Hash werden keine alten Prüfmarken oder Bilder übernommen. Die alte Ausgabe bleibt erhalten.

## Als Skill nutzen

Ein Klon kann mit den Skill-Verzeichnissen mehrerer lokaler Werkzeuge verknüpft werden:

| System | Im Repository ausführen |
| --- | --- |
| Windows | `powershell -File install.ps1` |
| macOS / Linux | `bash install.sh` |

Die Skripte verknüpfen nach `~/.claude/skills/`, `~/.agents/skills/` und `~/.gemini/config/skills/`. Echte vorhandene Kopien an diesen Zielpfaden werden übersprungen. Eine ältere Installation unter `~/.codex/skills/` separat prüfen, damit keine veraltete Kopie geladen wird. Die Python-Abhängigkeiten werden über den Schnellstart installiert.

Alternativ den Skill für ein Projekt in dessen `.agents/skills/pdf-seitenweise-sichten/` oder `.claude/skills/pdf-seitenweise-sichten/` ablegen. Welche Pfade und Funktionen dein Werkzeug unterstützt, ist in [Plattformen und Installation](Obsidian-Plan/31%20Plattformen%20und%20Installation.md) mit dem jeweiligen Prüfstand dokumentiert.

Beispielauftrag nach dem Laden des Skills:

```text
$pdf-seitenweise-sichten
Finde in ../Unterlagen die Aufgabe zum schiefen Wurf.
Nenne Dokument, PDF-Seite und Aufgabennummer. Prüfe die Formel
am Originalbild und verrate noch keine Endantwort.
```

`git pull` im Klon aktualisiert verknüpfte Installationen gemeinsam. Für einen festgelegten Stand einen geprüften Commit oder vorhandenen Tag verwenden.

## Prüfstand

| Bereich | Nachweis und Grenze |
| --- | --- |
| Automatische Tests | [Selbsttest](scripts/selbsttest.py): Extraktion, Duplikate, Rendering, Änderungsprüfung, Statusübernahme und Schutz vorhandener Ergebnisse. Die [CI](.github/workflows/checks.yml) ist für Windows und Linux eingerichtet. |
| Skill-Format | Formale Validierung des aktuellen Arbeitsstands bestanden; Details in [ARCHIVE.json](ARCHIVE.json). |
| Dokumentation | [Vault-Prüfung](Obsidian-Plan/Pruefung/vault_pruefen.py) prüft Verknüpfungen, Erreichbarkeit und Manifest. [SHA256SUMS](SHA256SUMS) dokumentiert die aufgeführten Repository-Dateien. |
| Reale Unterlagen | v1.3.0 wurde an CuD-Unterlagen und zwei weiteren PDF-Sätzen erprobt. Messgrundlage und Grenzen stehen in [Ist-Stand und Messung](Obsidian-Plan/20%20Ist-Stand%20und%20Messung.md). Diese Ergebnisse gelten nicht automatisch für spätere Änderungen. |
| Offene Nachweise | Für die anschließenden Korrekturen fehlen erneute reale PDF-Messungen sowie vollständige Tests in den unterstützten Agent-Oberflächen. Ein Effizienzgewinn ist dafür noch nicht gemessen. |

Die Zustände **indiziert**, **als Text gelesen**, **im Originalbild angesehen** und **fachlich geprüft** bleiben getrennt. Erzeugte Bilder gelten nicht automatisch als angesehen. Auch eine Bildsichtung beweist keine mathematische Richtigkeit.

### Prüfungen selbst ausführen

```sh
python -m pip install reportlab
python scripts/selbsttest.py
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
| [CHANGELOG.md](CHANGELOG.md) | Versionen und unveröffentlichte Änderungen |

Dieser Entwicklungsstand basiert auf v1.3.0; die anschließenden Änderungen stehen im Changelog unter „Unveröffentlicht“. Der zuletzt getaggte Stand ist v1.1.0. Ein fertiger Release-Anhang für v1.3.0 ist noch nicht vorhanden. Die [Release-Action](.github/workflows/release.yml) baut bei einem neuen Versions-Tag nach bestandenem Selbsttest ein ZIP; die Ausführung und das Ergebnis müssen anschließend geprüft werden.

Fehler oder Verbesserungen? Eröffne ein [Issue](https://github.com/Sae-l/pdf-seitenweise-sichten/issues) mit Befehl, Betriebssystem, Python-Version und beobachtetem Ergebnis. Für PDF-Probleme möglichst eine kleine, selbst erstellte Beispieldatei verwenden. Änderungen am Verhalten bitte mit einem passenden Selbsttest und Changelog-Eintrag einreichen.

## Lizenz und Herkunft

[MIT](LICENSE) für den eigenen Code und die Dokumentation dieses Repositorys. Die Lizenz erteilt keine Rechte an fremden PDF-Unterlagen, deren Texten oder Abbildungen. Originalunterlagen und ihre Extraktionen verbleiben im jeweiligen Quellprojekt.

Entstanden am 12.10.2026 aus dem Formelsammlungsprojekt von [Sae-l](https://github.com/Sae-l). Der Schwerpunkt liegt auf belegbarer Quellensichtung; PDF-Erstellung und automatische fachliche Freigabe gehören nicht zum Umfang.
