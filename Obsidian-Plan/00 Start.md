---
title: "00 Start"
description: "Einstieg in den Plan für pdf-seitenweise-sichten: Ziel, aktueller Stand, historische Pläne, Entscheidungen und Prüfwege."
type: moc
language: de
created: 2026-10-22
updated: 2026-10-29
status: aktiv
tags: ["pdf-sichtung", "moc"]
---

# pdf-seitenweise-sichten – Plan und Nachweise

> [!success] Aktueller Stand: v1.6.1
> Gezielte Suche, einzelne Seiten lesen, Originalbilder prüfen und Arbeitsfassungen mit Quellenbezug wiederverwenden. [Release](https://github.com/Sae-l/pdf-seitenweise-sichten/releases/tag/v1.6.1) · [Plugin](../README.md#mit-deinem-agenten-nutzen) · [Installation](../docs/installation.md) · [Messung und offene Grenzen](../docs/umsetzung-pdf-werkzeug-2026-10-24.md).

**Zweck:** ein projektunabhängiger Skill, der PDF-Referenzen beliebiger Projekte einmal lokal in Rohtext, Seitenbilder und einen Index zerlegt, damit die KI pro Frage nur die passenden Stellen lädt. Details: [[10 Ziel und Erfolgskriterien]].

Dieser Vault ist die einzige Quelle für Ziel, Plan und Entscheidungen. Der Einstieg für neue Nutzer steht in der [Projektübersicht](../README.md); `docs/plan-*` und `docs/umsetzung-*` sind historische Nachweise.

> [!info] Stand 22.10.2026
> v1.3.0 gebaut und am CuD-Satz gemessen: E1–E5 erfüllt (siehe [[20 Ist-Stand und Messung]]). Weiterentwicklung danach: Karte [PDF-Pipeline über v1.3.0 hinaus](https://github.com/Sae-l/pdf-seitenweise-sichten/issues/3).

## Lesereihenfolge

1. [[10 Ziel und Erfolgskriterien]] – Zweck, Anforderungen an Extraktion und Index, messbare Kriterien.
2. [[15 Glossar]] – verbindliche Begriffe.
3. [[20 Ist-Stand und Messung]] – gemessener Vergleich alt gegen v1.2.0 (historisch).
4. [[30 Plan v1.3.0]] – Schritte mit Fertig-wenn.
5. [[31 Plattformen und Installation]] – wo welches Werkzeug den Skill findet.
6. [[40 Entscheidungen]] – was entschieden wurde und warum.
7. [[50 Parkplatz]] – Ideen, die bewusst warten.
8. [[91 Quellen und Prüfwege]] – Quellen und Befehle, um alles neu zu prüfen.
9. [[92 Projektbeispiel Formelsammlung]] – wie ein Projekt Quellordner und Sichtungen zuordnet.

## Vault prüfen

```text
python Obsidian-Plan/Pruefung/vault_pruefen.py
```

Prüft Frontmatter, Wikilinks, Erreichbarkeit ab dieser Notiz und das Dateimanifest. Nach einer gewollten Änderung: `--write`.
