# Änderungen

## 1.4.0 — 2026-10-23

- Zwei Audit-Fehler mit Regressionstests korrigiert: Übernommene Bilder erhalten PDF-/Seiten-spezifische Zielnamen und überschreiben keine Bilder anderer Dokumente mit gleichem alten Basisnamen. Die Bildbytes und Prüfmarken bleiben erhalten.
- `check` weist einen fehlenden `Seitenindex.md` mit Fehlerstatus ab.
- Plattformprüfung und synthetische Lesetests in Codex/Claude Code dokumentiert; vollständige Agent-Endabnahmen werden getrennt als offen ausgewiesen.

- Portable Projektinstallation mit vollständigen Skill-Kopien unter `.agents/skills/` und `.claude/skills/` für Codex, Claude Code, Antigravity, VS Code/Copilot und GitHub Copilot.
- Globalen Antigravity-CLI-Pfad ergänzt. Native Installer wiederholbar; bestehende Kopien und fremde Links bleiben unverändert und melden einen Konflikt.
- GitHub-Copilot-Einstieg und Setup-Workflow ergänzt; die verbindlichen Verfahrensanweisungen bleiben in der Root-`SKILL.md`.
- Ressourcenpfade relativ zur geladenen Skill-Datei dokumentiert; Cloud-Zugang, Python-Ausführung und Bildansicht werden als separate Voraussetzungen behandelt.
- Technische Plattformtests für portable Pakete und native Installer ergänzt, einschließlich Schutz gegen aus dem Projekt führende Verknüpfungen; lokale Windows-Richtlinien werden nicht umgangen. CI verlangt Ausführung aller Tests.
- Offizielle Plattformquellen und Obsidian-Erfolgskriterien aktualisiert. Native Agent-Endabnahmen bleiben offen.

## 1.3.1 — 2026-10-22

- Release-ZIP wird aus getrackten Dateien erzeugt, inklusive MIT-Lizenz und Versionsnachweis. Eine separate `SHA256SUMS` schützt den Download.
- Release-Action prüft Tests, Vault, Repository-Hashes und Tag-Version, verwendet Python 3.12 und erstellt zunächst einen überprüfbaren Entwurf.
- GitHub Actions auf geprüfte Commit-SHAs festgelegt; Schreibrechte auf den Release-Job begrenzt.

- Besucher-Einstieg mit Ablaufgrafik, ausführbarem Schnellstart, Prüfnachweisen und klaren Plattformgrenzen überarbeitet.
- MIT-Lizenz für eigenen Code und Dokumentation ergänzt; Lizenzdatei wird im Release-ZIP mitgeliefert.
- CI für Selbsttest, Vault, Python-Syntax und Prüfsummen auf Windows und Linux ergänzt.

- Sichtung auf die Nutzerfrage begrenzen, vorhandene Ergebnisse nach erfolgreichem Check wiederverwenden und bei ausreichenden Quellen beenden.
- `--alt` übernimmt Sichtungsnachweise und Bilder nur mit gleicher vorhandener SHA-256-Prüfsumme; alte Manifeste ohne Hash bleiben ungeprüft.
- `check` erkennt neue PDFs, fehlende Prüfsummen/Markdown-Dateien, leere Manifeste und doppelte oder falsch geordnete Seitenabschnitte.
- `extract` weist fehlende/leere Quellen ab und schützt auch ein vorhandenes Manifest vor Überschreiben.
- Regressionstests für diese Fälle; Pillow als benötigte Bildabhängigkeit deklariert. Bestehende CLI-Aufrufe und Ausgabeformate bleiben erhalten.
- README enthält einen vollständigen Schnellstart und die Trennung zwischen Werkzeug, Agent-Skill und fachlicher Prüfung. Bestehende lokale Installationen werden nicht verändert.

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
