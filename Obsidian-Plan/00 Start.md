---
title: "00 Start"
description: "Einstieg in den Plan für pdf-seitenweise-sichten: Ziel, gemessener Stand, Plan v1.3.0, Entscheidungen und Prüfwege."
type: moc
language: de
created: 2026-10-22
updated: 2026-10-22
status: aktiv
tags: ["pdf-sichtung", "moc"]
---

# pdf-seitenweise-sichten – Plan und Nachweise

> [!todo] Nächste Aktion
> v1.3.0 und die Korrekturen aus PR #10 sind auf `main`. Der Release-Stand v1.3.1 bündelt sie mit einer geprüften Paketierung. Den aktuellen Veröffentlichungsstatus zeigt [GitHub Releases](https://github.com/Sae-l/pdf-seitenweise-sichten/releases/tag/v1.3.1); lokale Installation bleibt Schritt 6 in [[30 Plan v1.3.0]].

> [!info] Stand 22.10.2026
> v1.3.0 gebaut und am CuD-Satz gemessen: E1–E5 erfüllt (siehe [[20 Ist-Stand und Messung]]). Weiterentwicklung danach: Karte [PDF-Pipeline über v1.3.0 hinaus](https://github.com/Sae-l/pdf-seitenweise-sichten/issues/3).

## Lesereihenfolge

1. [[10 Ziel und Erfolgskriterien]] – was „fertig“ bedeutet, messbar.
2. [[20 Ist-Stand und Messung]] – gemessener Vergleich alt gegen v1.2.0.
3. [[30 Plan v1.3.0]] – Schritte mit Fertig-wenn.
4. [[31 Plattformen und Installation]] – wo welches Werkzeug den Skill findet.
5. [[40 Entscheidungen]] – was entschieden wurde und warum.
6. [[50 Parkplatz]] – Ideen, die bewusst warten.
7. [[91 Quellen und Prüfwege]] – Quellen und Befehle, um alles neu zu prüfen.

## Vault prüfen

```text
python Obsidian-Plan/Pruefung/vault_pruefen.py
```

Prüft Frontmatter, Wikilinks, Erreichbarkeit ab dieser Notiz und das Dateimanifest. Nach einer gewollten Änderung: `--write`.
