# pdf-seitenweise-sichten

Eine kleine Codex-Skill zur tokensparsamen Sichtung von PDF-Unterlagen. Sie arbeitet mit einem lokalen Seitenindex, gezielt gelesenen Markdown-Seitenabschnitten und den zugehörigen Originalseiten.

## Ablauf

1. Zuerst `Seitenindex.md` lesen und Dokument sowie PDF-Seite auswählen.
2. Im verlinkten Markdown nur `## PDF-Seite N` bis zur nächsten Seitenüberschrift lesen.
3. Formeln, Tabellen und Zeichnungen anhand der Originalseite oder ihres gerenderten Bildes prüfen.

Die verbindlichen Anweisungen stehen in [SKILL.md](SKILL.md). Die Skill umfasst keine Extraktionssoftware; sie verwendet vorhandene lokale Helfer oder PDF-Werkzeuge. PDF-Erstellung gehört nicht zu ihrem Umfang.

## Installation und Nutzung

Den Repository-Ordner nach `~/.codex/skills/pdf-seitenweise-sichten` kopieren. Existiert dort bereits eine Installation, diese zuerst mit dem gewünschten Versionsstand vergleichen und sichern.

Alternativ mit dem offiziellen `skill-installer` und dessen `scripts/install-skill-from-github.py`:

```text
--repo Sae-l/pdf-seitenweise-sichten --ref v1.1.0 --path . --name pdf-seitenweise-sichten
```

Für das private Repository sind passende GitHub-Zugangsdaten erforderlich. Nach der Installation ist die Skill im nächsten Codex-Turn verfügbar. Beispielaufruf:

```text
$pdf-seitenweise-sichten Sichte die Unterlagen im angegebenen PDF-Ordner.
```

## Herkunft und Stand

Erstellt am 12.10.2026 aus dem ausdrücklich gewünschten Workflow im Projekt Formelsammlung. Version 1.1.0 gleicht die Skill an den aktuellen Projektstand an (siehe Changelog); 1.0.x bleibt über Git-Tags erhalten. [CHANGELOG.md](CHANGELOG.md) beschreibt diesen Stand; [ARCHIVE.json](ARCHIVE.json) enthält die SHA-256-Prüfsumme der Skill und den dokumentierten Prüfstand.

Die formale Skill-Validierung wurde ausgeführt. Der Ablauf wurde an P2, PDF-Seite 9, und an acht ausgewählten Seiten aus fünf Beispielsammlungen angewendet. Bei einer FOSA-Seite war der extrahierte Text leer; die Originalbildsichtung war deshalb erforderlich.

Nicht durchgeführt: unabhängiger umfassender Verhaltenstest oder vollständige fachliche Prüfung der gesichteten Formeln. Ein vorhandenes Bild oder fehlende Extraktionswarnungen beweisen keine korrekte Formel. Die Skill unterscheidet indiziert, als Text gelesen, im Original angesehen und fachlich geprüft.

## Archiv und Wiederherstellung

Der Git-Tag `v1.1.0` bezeichnet den geprüften Archivstand. Die SHA-256-Werte in [SHA256SUMS](SHA256SUMS) beziehen sich auf die archivierten Dateien. Lokale ZIP- und Git-Bundle-Sicherungen werden getrennt vom Repository aufbewahrt; das Bundle enthält die Git-Historie und den Tag.

Wiederherstellung aus einem Bundle:

```text
git clone pdf-seitenweise-sichten-v1.1.0.bundle pdf-seitenweise-sichten
git -C pdf-seitenweise-sichten checkout v1.1.0
```

Dieses Repository archiviert die Skill und ihre Begleitdokumentation. Die PDF-Unterlagen, deren Volltexte und Bilder bleiben im jeweiligen Quellprojekt.
