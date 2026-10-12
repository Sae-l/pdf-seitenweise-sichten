---
name: pdf-seitenweise-sichten
description: PDF-Unterlagen tokensparsam über Seitenindex.md und seitenweise Markdown-Extraktionen sichten; Formeln, Tabellen und Zeichnungen an gezielt ausgewählten Originalseiten prüfen. Für Quellensichtung, nicht für PDF-Erstellung.
---

# PDF-Unterlagen seitenweise sichten

Verwende vorhandene lokale Extraktionen und Bilder. Lade nicht den gesamten PDF-Volltext in den Gesprächskontext.

1. Lies zuerst `Seitenindex.md` im zugehörigen Sichtungsordner. Bei großen Indizes lies den Überblick und suche nach dem gewünschten Thema. Beachte Dokumentname und PDF-Seitennummer.
2. Öffne das verlinkte Markdown und lies nur den Abschnitt von `## PDF-Seite N` bis zur nächsten Seitenüberschrift bzw. zum Dateiende. Eine Textsuche dient zur Auswahl, nicht als Ersatz für diesen Abschnitt. PDF-Seite und gedruckte Seiten-/Foliennummer können abweichen.
3. Ziehe für Formeln, Tabellen und Zeichnungen genau die zugehörige Originalseite oder ihr gerendertes Bild heran. Prüfe insbesondere Exponenten, Indizes, Vorzeichen, Bruchstriche, Produktzeichen, Einheiten und Vektorpfeile. Bei Widersprüchen hat das Original Vorrang; korrigiere nur die Arbeitsfassung.

Fehlende automatische Warnungen beweisen keine korrekte Formel. Ein erzeugtes Bild gilt erst nach tatsächlicher Ansicht als gesichtet. Eine Bildsichtung allein bestätigt noch nicht die mathematische Richtigkeit.

## Wenn ein Zugang fehlt

- Suche zunächst einen vorhandenen `Seitenindex.md`, auch in benachbarten Sichtungsordnern. Nutze den vorhandenen Projekt-Helfer, falls vorhanden, statt eine zweite Extraktionspipeline anzulegen.
- Fehlt die Extraktion, speichere lokal einen knappen Seitenindex und Markdown mit `## PDF-Seite N`. Erhalte Originaldateien unverändert und trenne die Ausgabe vom Quellordner. Rendere nur die für die aktuelle Frage nötigen Seiten zusätzlich.
- Prüfe die Anzahl der Seitenabschnitte gegen die PDF-Seitenzahl und die Linkziele. Bestehende manuelle Sichtungsnachweise beim Aktualisieren erhalten. Sind Formelzeichen im Bild unlesbar, rendere die einzelne Seite größer und lasse die Aussage bis zur Klärung offen.

## Quellen und Ergebnis

Nenne Dokument und PDF-Seite für inhaltliche Aussagen. Unterscheide zwischen indiziert, als Text gelesen, im Originalbild angesehen und fachlich geprüft. Markiere offene Prüfungen ausdrücklich. Halte Endantworten und Lösungen beim aktiven Üben getrennt, sofern das Lernziel dies verlangt.

In diesem Projekt liegen die Zugänge für `Info` in `Info_Sichtung/Seitenindex.md`, für `Info/Übungen` in `Uebungen_Sichtung/Seitenindex.md`. Diese Zuordnung ist ein Projektbeispiel, kein fest vorgeschriebener Pfad.
