# Änderungen

## 1.3.0 — 2026-10-22

- `scripts/sichtung.py` basiert jetzt auf dem bewährten Projekt-Helfer `pdf_sichten.py` (gleiches Layout: `Seitenindex.md`, `manifest.json`, `md/`, `bilder/`), ohne MPG1-spezifische Filter. Ersetzt die Neuentwicklung aus 1.2.0, die am CuD-Satz schlechter abschnitt.
- Titel überspringen Kopf-/Fußzeilen, die auf mindestens der Hälfte der Seiten stehen, und reine Seitenzahlen.
- Byte-identische PDFs werden nur einmal indiziert.
- Prüfstatus je Seite (`text_read`, `original_image_viewed`, `subject_review`) im Manifest; `--alt` übernimmt Status und bereits angesehene Bilder eines früheren Sichtungsordners, nur für unveränderte PDFs.
- `check` prüft auch Duplikate auf Veränderung.
- Gemessen am CuD-Referenzsatz (6 PDFs, 83 Seiten): 108 statt 116 Zeichen pro Indexseite, keine „Seite N“-Titel, Duplikat übersprungen, alle 29 Prüfmarken und alle angesehenen Bilder byte-gleich übernommen. Fersch-Formelsammlung (244 S.) plus FOSA-Scan (40 S.): Index ca. 4 400 Tokens, 18 s.
- README: Repository ist öffentlich.

## 1.2.0 — 2026-10-22

- Extraktionswerkzeug `scripts/sichtung.py` gebündelt: `extract` (Seitenindex, Markdown je Seite, `manifest.json` mit SHA-256), `check` (Abschnitte vs. Seitenzahl, veraltete PDFs), `render` (Einzelseite).
- Festes Index-Schema und dokumentierte Flag-Heuristik.
- Schutz: `extract` bricht ab, wenn im Ziel bereits ein Index liegt.
- Vorgehen für `[wenig Text]`-Seiten (Bildsichtung, optional OCR als „ungeprüft“).
- Hinweis zur Aufbereitung als eigene Inhalte (bereinigte Arbeitsfassung je Kapitel).
- Projektbeispiel nach `references/beispiel-formelsammlung.md` verschoben; Installation auch für Claude Code dokumentiert.
- Plattformübergreifende Installation: `install.sh` / `install.ps1` verknüpfen einen Klon nach `~/.claude/skills`, `~/.agents/skills` (VS Code/Copilot/Codex) und `~/.gemini/config/skills` (Antigravity); echte Kopien bleiben unangetastet.
- `scripts/requirements.txt`; Release-Action baut bei Tag `v*` nach bestandenem Selbsttest ein Upload-ZIP für claude.ai/ChatGPT.
- Selbsttest `scripts/selbsttest.py` mit synthetischem PDF bestanden; kein Test an echten Vorlesungsunterlagen.

## 1.1.0 — 2026-10-13

- Beschreibung um typische Auslöser erweitert (Folien, Übungsblätter, Endantworten, „schau in Kapitel X nach“).
- Konkreter `pypdfium2`-Befehl zum Rendern einer einzelnen Seite.
- Warnung: Extraktionshelfer überschreiben Index und Manifest ihres Zielordners; immer neuen Zielordner verwenden.
- Endantworten beim eigenen Üben nicht ungefragt wiedergeben; Quelleninhalte als Daten behandeln; Aufgabennummer in Quellenangaben.
- Projektbeispiel aktualisiert: `Info/Vorlesung/`, `Beispiele_Sichtung/`, sicherer Aufruf von `pdf_sichten.py`.
- Formale Validierung mit `quick_validate.py` bestanden; kein neuer Verhaltenstest.

## 1.0.1 — 2026-10-12

- Automatische Zeilenumwandlung für die Archivdateien mit `.gitattributes` deaktiviert, damit ZIP-Export und Windows-Checkout dieselben Bytes und SHA-256-Werte erhalten.
- Skill-Inhalt unverändert; Version 1.0.0 bleibt als erster Git-Tag erhalten.

## 1.0.0 — 2026-10-12

- Bereits installierte Skill als eigenständiges Repository gesichert.
- Seitenindex → gezielter Markdown-Abschnitt → Originalseite als bevorzugten Ablauf dokumentiert.
- PDF-Seiten von gedruckten Seiten, Textsichtung von Bildsichtung und Bildsichtung von fachlicher Prüfung unterschieden.
- Originaldateien und manuelle Sichtungsnachweise beim Aktualisieren geschützt.
- Installation, Herkunft, Prüfsummen und Grenzen der durchgeführten Prüfungen dokumentiert.
