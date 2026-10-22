# pdf-seitenweise-sichten

Eine kleine Codex-Skill zur tokensparsamen Sichtung von PDF-Unterlagen. Sie arbeitet mit einem lokalen Seitenindex, gezielt gelesenen Markdown-Seitenabschnitten und den zugehörigen Originalseiten.

## Ablauf

1. Zuerst `Seitenindex.md` lesen und Dokument sowie PDF-Seite auswählen.
2. Im verlinkten Markdown nur `## PDF-Seite N` bis zur nächsten Seitenüberschrift lesen.
3. Formeln, Tabellen und Zeichnungen anhand der Originalseite oder ihres gerenderten Bildes prüfen.

Die verbindlichen Anweisungen stehen in [SKILL.md](SKILL.md). Ab 1.2.0 liegt das Extraktionswerkzeug [scripts/sichtung.py](scripts/sichtung.py) bei (Index erzeugen, Aktualität prüfen, Seite rendern; benötigt `pypdfium2`). Selbsttest: `python scripts/selbsttest.py` (zusätzlich `reportlab`). PDF-Erstellung gehört nicht zum Umfang.

## Plan und Nachweise

Der weitere Plan (v1.3.0), gemessene Vergleiche, Entscheidungen und Prüfbefehle liegen als Obsidian-Vault in [Obsidian-Plan/00 Start.md](Obsidian-Plan/00%20Start.md). Prüfen: `python Obsidian-Plan/Pruefung/vault_pruefen.py`.

## Installation und Nutzung

**Empfohlen: einmal klonen, überall verknüpfen.** Ein Klon versorgt alle lokalen Werkzeuge; `git pull` im Klon aktualisiert alle gleichzeitig.

```text
git clone https://github.com/Sae-l/pdf-seitenweise-sichten
cd pdf-seitenweise-sichten
./install.sh                                      # macOS/Linux
powershell -ExecutionPolicy Bypass -File install.ps1   # Windows (Junctions, keine Adminrechte)
python -m pip install -r scripts/requirements.txt
```

| Werkzeug | Verknüpfter Ordner |
| --- | --- |
| Claude Code | `~/.claude/skills/` |
| VS Code / GitHub Copilot, Codex | `~/.agents/skills/` |
| Antigravity | `~/.gemini/config/skills/` |
| claude.ai, ChatGPT (Business/Enterprise/Edu) | ZIP aus dem GitHub-Release hochladen |

Eine bereits vorhandene echte Kopie (z. B. eine ältere Installation unter `~/.codex/skills/` oder in einem der Ordner oben) wird nicht angetastet; das Skript meldet sie, damit sie vorher gesichert und entfernt werden kann.

Pro Projekt (auch für den Copilot-Cloud-Agent auf GitHub) den Skill-Ordner nach `.agents/skills/` bzw. `.claude/skills/` des Projekts kopieren.

**Release:** Ein Tag `v*` startet `.github/workflows/release.yml`: Selbsttest, dann ZIP mit `SKILL.md`, `scripts/` und `references/` als Release-Anhang.

Alternativ mit dem offiziellen `skill-installer` und dessen `scripts/install-skill-from-github.py`:

```text
--repo Sae-l/pdf-seitenweise-sichten --ref v1.2.0 --path . --name pdf-seitenweise-sichten
```

Für das private Repository sind passende GitHub-Zugangsdaten erforderlich. Nach der Installation ist die Skill im nächsten Codex-Turn verfügbar. Beispielaufruf:

```text
$pdf-seitenweise-sichten Sichte die Unterlagen im angegebenen PDF-Ordner.
```

## Herkunft und Stand

Erstellt am 12.10.2026 aus dem ausdrücklich gewünschten Workflow im Projekt Formelsammlung. Version 1.1.0 glich die Skill an den Projektstand an, 1.2.0 bündelt das Extraktionswerkzeug (siehe Changelog); ältere Stände bleiben über Git-Tags erhalten. [CHANGELOG.md](CHANGELOG.md) beschreibt diesen Stand; [ARCHIVE.json](ARCHIVE.json) enthält die SHA-256-Prüfsumme der Skill und den dokumentierten Prüfstand.

Die formale Skill-Validierung wurde ausgeführt. Der Ablauf wurde an P2, PDF-Seite 9, und an acht ausgewählten Seiten aus fünf Beispielsammlungen angewendet. Bei einer FOSA-Seite war der extrahierte Text leer; die Originalbildsichtung war deshalb erforderlich.

Nicht durchgeführt: unabhängiger umfassender Verhaltenstest oder vollständige fachliche Prüfung der gesichteten Formeln. Ein vorhandenes Bild oder fehlende Extraktionswarnungen beweisen keine korrekte Formel. Die Skill unterscheidet indiziert, als Text gelesen, im Original angesehen und fachlich geprüft.

## Archiv und Wiederherstellung

Der Git-Tag `v1.1.0` bezeichnet den zuletzt archivierten Stand; `v1.2.0` wird nach dem Merge gesetzt. Die SHA-256-Werte in [SHA256SUMS](SHA256SUMS) beziehen sich auf die archivierten Dateien. Lokale ZIP- und Git-Bundle-Sicherungen werden getrennt vom Repository aufbewahrt; das Bundle enthält die Git-Historie und den Tag.

Wiederherstellung aus einem Bundle:

```text
git clone pdf-seitenweise-sichten-v1.1.0.bundle pdf-seitenweise-sichten
git -C pdf-seitenweise-sichten checkout v1.1.0
```

Dieses Repository archiviert die Skill und ihre Begleitdokumentation. Die PDF-Unterlagen, deren Volltexte und Bilder bleiben im jeweiligen Quellprojekt.
