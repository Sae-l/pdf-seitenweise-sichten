---
title: "00 Start"
description: "Einstieg in den Plan für pdf-seitenweise-sichten: Ziel, aktueller Stand, historische Pläne, Entscheidungen und Prüfwege."
type: moc
language: de
created: 2026-10-22
updated: 2026-10-24
status: aktiv
tags: ["pdf-sichtung", "moc"]
---

# pdf-seitenweise-sichten – Plan und Nachweise

> [!success] Aktueller Stand: v1.5.0
> Gezielte Suche, einzelne Seiten lesen, Originalbilder prüfen und Arbeitsfassungen mit Quellenbezug wiederverwenden. [Release](https://github.com/Sae-l/pdf-seitenweise-sichten/releases/tag/v1.5.0) · [Installation](../docs/installation.md) · [Messung und offene Grenzen](../docs/umsetzung-pdf-werkzeug-2026-10-24.md).

Der Einstieg für neue Nutzer steht in der [Projektübersicht](../README.md). Dieser Vault bewahrt Entscheidungen, historische Messungen und noch offene Abnahmen. Die folgenden Versionspläne bleiben als historische Nachweise erhalten.

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
