# Änderungen

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
