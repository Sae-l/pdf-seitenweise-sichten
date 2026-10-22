---
title: "50 Parkplatz"
description: "Ideen, die bewusst warten, mit dem Anlass, der sie wieder aufruft."
type: parkplatz
language: de
created: 2026-10-22
updated: 2026-10-22
status: geparkt
tags: ["pdf-sichtung", "parkplatz"]
---

# Parkplatz

Wir lösen noch [[30 Plan v1.3.0]]. Alles hier ist geparkt, bis der genannte Anlass eintritt.

| Idee | Nutzen | Aufwand | Anlass zum Starten |
| --- | --- | --- | --- |
| Volltextsuche (SQLite FTS5) und Kapitelgliederung aus PDF-Lesezeichen | Pro Frage einige hundert statt einige tausend Tokens | ca. 40 Zeilen | Index eines PDFs über ca. 5 000 Tokens |
| Bildexport und Flag `[Diagramm]` über Vektorpfade | Diagrammseiten gezielt finden | ca. 20 Zeilen | Diagramme werden im Projekt regelmäßig gesucht |
| Formeln als LaTeX für markierte Seiten (Docling oder Marker, lokal) | Formeln ohne Seitenbild nutzbar | groß, langsam auf CPU | Viele Formelseiten werden wiederholt gebraucht; vorher an 10 Seiten testen |
| Einmalige Bildbeschreibung je Diagrammseite | Diagramm ohne Bild verstehen | einmalig Tokens oder lokales Modell | Nach Stufe Bildexport |
| Am Bild geprüfte Formel als LaTeX im Seitenabschnitt speichern | Bildprüfung nur einmal | klein | Gleiche Formelseite wird mehrfach geprüft |
| `all2md` oder `qmd` als Suchschicht testen | fertige Suche | Installation | Wenn die eigene Suche nicht reicht |
| Veröffentlichung auf skills.sh | `npx skills add` möglich | klein | Repo wird öffentlich |
