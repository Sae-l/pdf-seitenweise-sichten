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

- Der alte Helfer rendert Seiten mit wenig oder beschädigtem Text vorab und kennt die Flags `[Aufgabe/Beispiel]` sowie `answer_start_page`. Seine guten Titel stammen aus **MPG1-spezifischen Filterregeln** (`Fakultät für`, `Kapitel [MP]\d` …).
- v1.2.0 bringt dafür neu: `check` mit SHA-256-Vergleich, Abbruch statt Überschreiben, Selbsttest, Installationsskripte und Release-ZIP.

> [!warning] Korrektur vom 22.10.2026 (nach Lesen des Helfer-Quelltexts)
> Der alte Helfer erkennt **keine** Duplikate und schreibt **keinen** Prüfstatus. Beides wurde in CuD von Hand nachgetragen (Sichtungsbericht und Felder `text_read`, `original_image_viewed`, `subject_review`). Auch 9 der 16 Bilder in CuD sind von Hand gerendert. Die erste Fassung dieser Notiz schrieb das fälschlich dem Helfer zu.

> [!warning] Korrektur einer früheren Schätzung
> Im Gespräch wurde zuerst „ca. 35 % mehr“ genannt. Der Wert stammte nur aus dem Vorlesungs-Index. Über alle 83 Seiten gemessen sind es 21 %.

## Ergebnis v1.3.0 (22.10.2026)

`messen.py` vergleicht jetzt den alten Index mit `scripts/sichtung.py` einschließlich `--alt`-Übernahme:

| Messgröße | Alter Helfer | v1.3.0 | Kriterium |
| --- | ---: | ---: | --- |
| Indizierte Seiten | 83 | 80 (Duplikat übersprungen) | E3 erfüllt |
| Zeichen pro Seite im Index | 116 | 108 | E1 erfüllt |
| Titel nur „Seite N“ | 0 | 0, ohne MPG1-Sonderregeln | E2 erfüllt |
| Prüfmarken im Manifest | 29 | 29 übernommen | E4 erfüllt |

Zusätzlich manuell geprüft: alle angesehenen CuD-Bilder byte-gleich übernommen; nur das Bild des Duplikats entfällt. Großer Satz (Fersch 244 S. + FOSA-Scan 40 S.): Index ca. 4 400 Tokens, 18 s auf der Testumgebung.
