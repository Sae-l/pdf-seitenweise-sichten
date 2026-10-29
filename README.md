# PDF-Unterlagen gezielt sichten

**Die passende Seite finden. Text und Bilder prüfen. Inhalte mit Quellen weiterverwenden.**

Ein lokales Python-Werkzeug und Agent-Skill für Vorlesungsfolien, Übungsblätter und Formelsammlungen. Für alle, die aus umfangreichen PDFs gezielt Wissen erschließen möchten, ohne jedes Mal das ganze Dokument in den KI-Kontext zu laden.

![Vom kompakten Seitenindex zum relevanten Text und zur Prüfung an der Originalseite.](docs/assets/ablauf.svg)

<p align="center">
  <a href="https://github.com/Sae-l/pdf-seitenweise-sichten/releases/tag/v1.6.1"><strong>v1.6.1 herunterladen</strong></a> ·
  <a href="#schnellstart">Schnellstart</a> ·
  <a href="references/gezielte-nutzung.md">Nutzungsbeispiele</a> ·
  <a href="#prüfstand">Prüfnachweise</a>
</p>

<p align="center">
  <a href="https://github.com/Sae-l/pdf-seitenweise-sichten/actions/workflows/checks.yml"><img src="https://github.com/Sae-l/pdf-seitenweise-sichten/actions/workflows/checks.yml/badge.svg?branch=main" alt="Aktueller Status der Windows- und Linux-CI" /></a>
</p>

## Weniger suchen. Gezielter arbeiten.

| Dein Vorhaben | Was das Werkzeug liefert |
| --- | --- |
| Eine Erklärung oder Aufgabe finden | Wenige kurze Treffer mit Dokument und PDF-Seite; auch für Angaben wie „Aufgabe 9“. |
| Text, Formeln und Diagramme verstehen | Einzelne Textseiten und bei Bedarf das gerenderte Originalbild. |
| Inhalte weiterverwenden | Getrennte Arbeitsfassungen als Markdown, LaTeX, CSV oder Bilddatei mit Quellenbezug. |
| Später mit denselben Unterlagen arbeiten | Prüfung auf geänderte Quellen und Wiederverwendung unveränderter Ergebnisse. |

**Zwei Bausteine, ein Ablauf:** Das [Python-Werkzeug](scripts/sichtung.py) erledigt Suche, Extraktion und Integritätsprüfung. Der [Skill](SKILL.md) führt einen Agenten durch Auswahl, Originalabgleich und Quellenangaben. Das Werkzeug funktioniert auch ohne KI.

## Schnellstart

Du brauchst **Python 3.12 oder neuer** und Git. Unter macOS/Linux gegebenenfalls `python3` verwenden.

```sh
git clone --branch v1.6.1 --depth 1 https://github.com/Sae-l/pdf-seitenweise-sichten.git
cd pdf-seitenweise-sichten
python -m pip install -r scripts/requirements.txt
```

Lege eigene PDFs in einen Ordner, beispielsweise `../Unterlagen`. Danach:

```sh
# Einmal lokal erschließen; einen neuen Ausgabeordner verwenden.
python scripts/sichtung.py extract "../Unterlagen" "../Unterlagen_Sichtung"

# Gezielt suchen, statt das gesamte Dokument zu laden.
python scripts/sichtung.py search "../Unterlagen_Sichtung" "Kraft Beschleunigung"
```

Die Treffer nennen Datei und PDF-Seite. Mit diesen Werten lesen:

```sh
# Beispiel: Dateiname und Seite durch einen tatsächlichen Treffer ersetzen.
python scripts/sichtung.py read "../Unterlagen_Sichtung" "Mechanik.pdf" 7
```

Die Originale bleiben erhalten. PDFs werden direkt im angegebenen Quellordner gesucht; Unterordner werden nicht automatisch mitextrahiert. [Installation, ZIP-Nutzung und Updates →](docs/installation.md)

## Mit deinem Agenten nutzen

Als Plugin aus diesem Repository (Python mit `pypdfium2` und `Pillow` muss lokal vorhanden sein):

```text
/plugin install pdf-seitenweise-sichten --marketplace Sae-l/pdf-seitenweise-sichten
```

Das ist der Befehl für Claude Code. Für Codex lautet er `codex plugin marketplace add Sae-l/pdf-seitenweise-sichten`, danach `codex plugin add pdf-seitenweise-sichten@sae-l-skills`. Cursor und VS Code/Copilot lesen den Skill aus der Projektkopie unten. Ein Agent kann die Einrichtung selbst übernehmen: [Anleitung für Agenten](AGENTS.md#installation-für-nutzer). Der Ordner [`plugins/`](plugins/pdf-seitenweise-sichten) ist die daraus erzeugte Plugin-Kopie von `SKILL.md`, `scripts/` und `references/`; geändert wird nur an der Quelle.

Alternativ installierst du den Skill aus dem geklonten Repository in ein **bereits vorhandenes Zielprojekt**:

```sh
python scripts/install_projekt.py "../Mein-Projekt"
```

Der Installer erzeugt vollständige Kopien unter `.agents/skills/` und `.claude/skills/`. Bestehende Kopien werden geschützt. Bereitstellung ist für Codex, Claude Code, Antigravity und Copilot beschrieben; vollständige Agent-Endabnahmen bleiben getrennt von den technischen Tests.

Beispielauftrag nach dem Aktivieren des Skills:

```text
Finde die Aufgabe zum schiefen Wurf in meinen Unterlagen.
Nenne Dokument, PDF-Seite und Aufgabennummer.
Prüfe Formeln am Originalbild und verrate keine Endantwort.
```

Aktivierung, globale Verknüpfungen und Cloud-Voraussetzungen stehen in der [Installationsanleitung](docs/installation.md).

## Von der Quelle zur Arbeitsfassung

**Suchen → Seite lesen → Original ansehen → benötigte Inhalte speichern.**

`search` liefert standardmäßig höchstens fünf kurze Treffer. `read` liest die gewählte Seite mit sichtbarer Fortsetzung bei langen Texten. Für Formeln, Tabellen und Diagramme folgt die tatsächliche Bildansicht. Anschließend kann `save` eine selbst erstellte Arbeitsfassung mit Quellen- und Inhaltshashes sichern.

| Befehl | Aufgabe |
| --- | --- |
| `extract` | PDFs lokal erschließen und einen Seitenindex anlegen |
| `search` / `read` | Passende Inhalte finden und einzelne Seiten lesen |
| `render` | Eine Originalseite als Bild bereitstellen |
| `save` | Eine aufbereitete Datei mit Quelle und Prüfstatus speichern |
| `check` | Quellen, Seitenlisten, Links und Bildreferenzen technisch prüfen |

Die [Nutzungsbeispiele](references/gezielte-nutzung.md) zeigen den vollständigen Ablauf einschließlich Wiederverwendung und Lösungsschutz.

## Prüfstand

- **Automatisierte Technik:** Selbsttest, portable Installation, Plugin-Paket, Vault, Syntax und Prüfsummen werden auf Windows und Linux geprüft. [GitHub Actions](https://github.com/Sae-l/pdf-seitenweise-sichten/actions/workflows/checks.yml)
- **Reale Unterlagen:** 27 MPG1-PDFs mit 218 Seiten neu extrahiert und geprüft; fünf festgelegte Suchfälle, zwei tatsächlich betrachtete Originalseiten und eine wiederverwendete Formel-Arbeitsfassung. [Messung und Grenzen](docs/umsetzung-pdf-werkzeug-2026-10-24.md)
- **Paketintegrität:** Das Release enthält das Skill-ZIP und dessen SHA-256-Datei. Die [Repository-Prüfsummen](SHA256SUMS) betreffen dagegen die aufgeführten Quelldateien.

Bei den fünf Suchfällen wurden **92–95 % weniger Zeichen** ausgegeben als beim vollständigen jeweiligen Gruppenindex. Das misst die Auswahlphase, keine allgemeine Tokenersparnis und keine vollständige Bearbeitung einschließlich Bildern.

**Prüfstatus bleibt präzise:** Indiziert, als Text gelesen, im Originalbild angesehen und fachlich geprüft sind getrennte Zustände. Ein Hashvergleich oder erzeugtes Bild bestätigt keine mathematische Richtigkeit.

## Was du wissen solltest

Das Python-Werkzeug verarbeitet lokal. Welche Inhalte ein KI-Agent an seinen Anbieter übermittelt, hängt von dessen Umgebung ab. Scans und Bildinhalte sind ohne passenden Text nicht zuverlässig durchsuchbar; OCR ist nicht integriert. Erkannte Lösungsbereiche werden standardmäßig ausgeblendet, unmarkierte Antworten und ganze Seitenbilder benötigen weiterhin sorgfältige Prüfung. Die vollständige Abnahme aller Agent-Oberflächen und eine umfassende fachliche Prüfung sind offen.

## Weiterführend

| Einstieg | Inhalt |
| --- | --- |
| [Installation und Updates](docs/installation.md) | Passender Weg für Projekt, ZIP, globale Verknüpfungen und Cloud |
| [Nutzungsbeispiele](references/gezielte-nutzung.md) | Suche, Seitenlesen, Bilder und Arbeitsfassungen |
| [Skill-Anweisung](SKILL.md) | Verbindlicher Ablauf für Agenten |
| [Änderungen](CHANGELOG.md) · [Release-Hinweise](docs/releases/v1.6.1.md) | Neuerungen und Versionsgrenzen |
| [Plan und Nachweise](Obsidian-Plan/00%20Start.md) | Entscheidungen, frühere Messungen und offene Schritte |
| [Mitwirken](CONTRIBUTING.md) | Fehler melden und Änderungen nachvollziehbar prüfen |

[MIT-Lizenz](LICENSE) für eigenen Code und Dokumentation. Rechte an fremden PDF-Unterlagen bleiben bei deren Rechteinhabern. Entwickelt von [Sae-l](https://github.com/Sae-l), entstanden im Formelsammlungsprojekt.
