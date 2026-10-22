---
title: "91 Quellen und Prüfwege"
description: "Externe Quellen mit Abrufdatum und die Befehle, mit denen jede Aussage des Vaults erneut geprüft werden kann."
type: nachweis
language: de
created: 2026-10-22
updated: 2026-10-22
status: aktiv
tags: ["pdf-sichtung", "quellen"]
---

# Quellen und Prüfwege

## Prüfbefehle

| Aussage | Befehl |
| --- | --- |
| Messwerte in [[20 Ist-Stand und Messung]] | `python Obsidian-Plan/Pruefung/messen.py <CuD-klon>` |
| Extraktion, `check`, Überschreibschutz, `render` | `python scripts/selbsttest.py` (braucht `reportlab`) |
| Skill formal gültig | `quick_validate.py` aus dem skill-creator |
| Archivdateien unverändert | `sha256sum -c SHA256SUMS` |
| Vault vollständig und verlinkt | `python Obsidian-Plan/Pruefung/vault_pruefen.py` |

## Quellen (abgerufen 22.10.2026)

| Thema | Quelle | Kernaussage |
| --- | --- | --- |
| VS Code / Copilot | [Use Agent Skills in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills) | Ordner `.github/`, `.claude/`, `.agents/skills`; `name` muss dem Ordner entsprechen |
| Antigravity | [Authoring Google Antigravity Skills](https://codelabs.developers.google.com/getting-started-with-antigravity-skills?hl=en) | global `~/.gemini/config/skills/`, Projekt `.agents/skills/`; Skripte in `scripts/` |
| ChatGPT | [Skills in ChatGPT](https://help.openai.com/en/articles/20001066) | nur Business, Enterprise, Healthcare, Edu; Upload über „Create“ |
| ECC Tools | [GitHub Marketplace](https://github.com/marketplace/ecc-tools) | private Repos nur mit Pro (19 $ pro Person und Monat) |
| Fremde PDF-Skills | [mineru-refine](https://skillselion.com/skills/LcpMarvel/mineru-refine/plugin), [all2md](https://all2md.readthedocs.io/en/stable/_sources/agent_skills.rst.txt) | mineru-refine nutzt externe APIs; all2md-Lokalität ungeklärt |
| Skill-Verzeichnis | [skills.sh](https://skills.sh/) | kein PDF-/OCR-Skill auf der Bestenliste sichtbar |

> [!note] Grenzen
> Plattformangaben ändern sich schnell. Vor Schritt 6 in [[30 Plan v1.3.0]] die Quellen erneut öffnen und das Abrufdatum hier anpassen.
