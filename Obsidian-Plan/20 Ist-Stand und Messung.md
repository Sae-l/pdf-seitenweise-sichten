---
title: "20 Ist-Stand und Messung"
description: "Gemessener Vergleich zwischen dem alten Projekt-Helfer und scripts/sichtung.py aus v1.2.0 am CuD-Referenzsatz."
type: nachweis
language: de
created: 2026-10-22
updated: 2026-10-22
status: gemessen
tags: ["pdf-sichtung", "messung"]
---

# Ist-Stand und Messung

**Messgrundlage:** [Sae-l/CuD](https://github.com/Sae-l/CuD), Commit `9237bc2`, Ordner `Referenz` (6 PDFs, 83 Seiten). Alter Index: `Referenz_Sichtung`, erzeugt mit `D:/Saeed/Projekts/Formelsammlung/pdf_sichten.py`. Neu: `scripts/sichtung.py` aus v1.2.0 (`d49cc59`).

**Reproduzieren:**

```text
python Obsidian-Plan/Pruefung/messen.py <pfad-zum-CuD-klon>
```

## Ergebnis vom 22.10.2026

| Messgröße | Alter Helfer | v1.2.0 | Bewertung |
| --- | ---: | ---: | --- |
| Zeichen pro Seite im Index | 116 | 140 | v1.2.0 **+21 %** schlechter |
| Titel nur „Seite N“ | 0 von 83 | 24 von 83 | v1.2.0 schlechter |
| Byte-identische PDF-Duplikate | erkannt | 1 doppelt indiziert | v1.2.0 schlechter |
| Kopf-/Fußzeilenanteil am Text | – | 0–10 % je PDF | kein Handlungsbedarf |

## Was nur durch Lesen festgestellt wurde (nicht von `messen.py` geprüft)

- Der alte Helfer führt im Manifest pro Seite `text_read`, `original_image_viewed` und `subject_review`, rendert markierte Seiten vorab (14 Bilder, 3,6 MB) und kennt die Flags `[Aufgabe/Beispiel]` sowie `answer_start_page`.
- v1.2.0 bringt dafür neu: `check` mit SHA-256-Vergleich, Abbruch statt Überschreiben, Selbsttest, Installationsskripte und Release-ZIP.

## Folgerung

v1.2.0 hat eine zweite Extraktions-Pipeline geschaffen, obwohl der Skill selbst davor warnt. Richtig ist: den alten Helfer als Basis bündeln und die neuen Teile ergänzen, siehe [[30 Plan v1.3.0]] und [[40 Entscheidungen]].

> [!warning] Korrektur einer früheren Schätzung
> Im Gespräch wurde zuerst „ca. 35 % mehr“ genannt. Der Wert stammte nur aus dem Vorlesungs-Index. Über alle 83 Seiten gemessen sind es 21 %.
