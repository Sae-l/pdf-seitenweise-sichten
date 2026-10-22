---
title: "31 Plattformen und Installation"
description: "Wo Claude Code, VS Code/Copilot, Codex, Antigravity, claude.ai und ChatGPT Skills laden und wie ein Klon alle versorgt."
type: referenz
language: de
created: 2026-10-22
updated: 2026-10-22
status: teilweise-geprüft
tags: ["pdf-sichtung", "installation"]
---

# Plattformen und Installation

Grundsatz: **ein Klon, überall verknüpft**. `git pull` im Klon aktualisiert alle lokalen Werkzeuge. Für Weboberflächen erzeugt ein Tag `v*` ein ZIP (Release-Action).

| Werkzeug | Global | Pro Projekt | Getestet am 22.10.2026 |
| --- | --- | --- | --- |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` | Verknüpfung per `install.sh` (Linux) |
| VS Code / GitHub Copilot | `~/.copilot/skills/`, `~/.claude/skills/`, `~/.agents/skills/` | `.github/skills/`, `.claude/skills/`, `.agents/skills/` | nein |
| Codex | `~/.agents/skills/` | `.agents/skills/` | nein |
| Antigravity | `~/.gemini/config/skills/` | `.agents/skills/` | nein |
| claude.ai | ZIP hochladen | – | nein |
| ChatGPT | ZIP hochladen, nur Business/Enterprise/Healthcare/Edu | – | nein |

Quellen: [[91 Quellen und Prüfwege]].

## Bekannte Grenzen

- `install.ps1` ist ungetestet (kein Windows in der Testumgebung).
- VS Code lädt einen Skill still nicht, wenn `name` nicht dem Ordnernamen entspricht; beide heißen `pdf-seitenweise-sichten`.
- Eine alte echte Kopie unter `~/.codex/skills/` kann zu doppeltem Laden führen; vorher entfernen.
- Ob ChatGPT Skripte eines Skills ausführt, ist laut Hilfeseite offen.

Testergebnisse aus Schritt 6 von [[30 Plan v1.3.0]] hier in der letzten Spalte eintragen.
