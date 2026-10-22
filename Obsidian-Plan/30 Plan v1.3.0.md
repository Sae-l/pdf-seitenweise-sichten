---
title: "30 Plan v1.3.0"
description: "Schritte von v1.2.0 zu v1.3.0: alten Helfer bündeln, Stärken zusammenführen, an CuD gegenprüfen, veröffentlichen."
type: plan
language: de
created: 2026-10-22
updated: 2026-10-22
status: offen
tags: ["pdf-sichtung", "plan"]
---

# Plan v1.3.0

Ziel und Kriterien: [[10 Ziel und Erfolgskriterien]]. Ausgangslage: [[20 Ist-Stand und Messung]].

## Jetzt nötig

- [ ] **1. Alten Helfer ins Repo bringen** (ca. 2 min, Saeed)
  - Was: `D:\Saeed\Projekts\Formelsammlung\pdf_sichten.py` hochladen oder pushen.
  - Warum: Er ist am CuD-Satz nachweislich besser (E1–E4).
  - Fertig wenn: Datei liegt unverändert im Repo, SHA-256 notiert.
- [ ] **2. Zusammenführen** (ca. 20 min, Claude)
  - Was: alter Helfer als `scripts/sichtung.py`; aus v1.2.0 übernehmen: `check`, Abbruch statt Überschreiben, `render`.
  - Warum: eine Pipeline statt zwei.
  - Fertig wenn: Selbsttest grün (E5).
- [ ] **3. `messen.py` und Selbsttest anpassen** (ca. 10 min, Claude)
  - Was: neuen Indexaufbau einlesen; Testfall für Duplikat und Titel ergänzen.
  - Fertig wenn: beide Skripte laufen ohne Fehler.
- [ ] **4. Gegenprüfung an CuD** (ca. 5 min, Claude)
  - Was: `messen.py` gegen CuD-Klon.
  - Fertig wenn: E1–E3 erfüllt; Ergebnis in [[20 Ist-Stand und Messung]] ergänzt.
- [ ] **5. Pull Request, Squash-Merge, Tag `v1.3.0`** (ca. 5 min, Saeed)
  - Fertig wenn: Release enthält ZIP; Action grün.
- [ ] **6. Lokal installieren und testen** (ca. 10 min, Saeed)
  - Was: `install.ps1`, dann ein Testauftrag je genutztem Werkzeug.
  - Fertig wenn: E6 erfüllt, Ergebnis in [[31 Plattformen und Installation]] vermerkt.

## Später empfohlen

- [ ] Pflegeaufwand senken: `SHA256SUMS` und `ARCHIVE.json` in der Release-Action erzeugen statt von Hand.
- [ ] Suche nur dann, wenn ein PDF über 100 Seiten den Index über ca. 5 000 Tokens treibt (siehe [[50 Parkplatz]]).

## Optional

- [ ] ECC-Tools-App für dieses Repo entfernen (Kommentare ohne Prüfung, siehe [[40 Entscheidungen]]).

> [!tip] Stoppregel
> Nach Schritt 6 mit E1–E6 erfüllt: fertig. Keine weiteren Stufen ohne konkreten Anlass.
