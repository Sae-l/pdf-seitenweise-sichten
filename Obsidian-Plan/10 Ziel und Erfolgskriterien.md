---
title: "10 Ziel und Erfolgskriterien"
description: "Ziel des Skills und messbare Kriterien, an denen v1.3.0 als fertig gilt."
type: konzept
language: de
created: 2026-10-22
updated: 2026-10-22
status: festgelegt
tags: ["pdf-sichtung", "ziel"]
---

# Ziel und Erfolgskriterien

**Ziel:** Große PDFs (50–200 Seiten, ca. 10 MB) mit Text, Mathematik, Bildern und Diagrammen **einmal lokal** erfassen und danach als Projektreferenz nutzen, ohne dass eine KI die Datei erneut ganz liest.

**Einsatzorte:** Claude Code, claude.ai, VS Code/Copilot, Codex, Antigravity, ChatGPT (nur Business/Enterprise/Edu), siehe [[31 Plattformen und Installation]].

## Erfolgskriterien (alle müssen gelten)

| Nr. | Kriterium | Prüfweg |
| --- | --- | --- |
| E1 | Index höchstens so groß wie beim alten Helfer: ≤ 116 Zeichen pro Seite am CuD-Referenzsatz | `messen.py`, siehe [[20 Ist-Stand und Messung]] |
| E2 | Kein Seitentitel besteht nur aus „Seite N“ | `messen.py`, Wert `titel_nur_seitennummer` = 0 |
| E3 | Byte-identische PDFs werden nur einmal indiziert | `messen.py` gegen Index vergleichen |
| E4 | Prüfstatus pro Seite (Text gelesen, Bild angesehen, fachlich geprüft) bleibt im Manifest erhalten | Manifest öffnen |
| E5 | `check` erkennt geänderte PDFs, Überschreibschutz greift | `scripts/selbsttest.py` |
| E6 | Ein Klon versorgt alle lokalen Werkzeuge | `install.ps1` bzw. `install.sh`, siehe [[31 Plattformen und Installation]] |

**Stoppregel:** Gelten E1–E6, ist v1.3.0 fertig. Weitere Stufen stehen im [[50 Parkplatz]] und werden erst nach einem echten Bedarf begonnen.
