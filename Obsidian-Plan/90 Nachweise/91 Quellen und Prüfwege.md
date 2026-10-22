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
| Portable Pakete und native Installer | `python scripts/plattformtest.py`; lokale übersprungene Tests sind als solche zu berichten, in CI verboten |
| Skill formal gültig | `quick_validate.py` aus dem skill-creator |
| Archivdateien unverändert | `sha256sum -c SHA256SUMS` |
| Vault vollständig und verlinkt | `python Obsidian-Plan/Pruefung/vault_pruefen.py` |

## Quellen (abgerufen 22.10.2026)

| Thema | Quelle | Kernaussage |
| --- | --- | --- |
| Codex | [Build skills](https://learn.chatgpt.com/docs/build-skills) | Projekt und Benutzer: `.agents/skills`; symbolische Skill-Verzeichnisse unterstützt |
| Claude Code | [Extend Claude with skills](https://code.claude.com/docs/en/skills) | Lokaler Benutzer/Projekt: `.claude/skills`; `/skill-name`; Cloud-Sitzungen gesondert behandeln |
| VS Code / Copilot | [Use Agent Skills in VS Code](https://code.visualstudio.com/docs/agent-customization/agent-skills) | Ordner `.github/`, `.claude/`, `.agents/skills`; `name` muss dem Ordner entsprechen |
| Antigravity | [Agent skills](https://antigravity.google/docs/skills) | Projekt `.agents/skills`; App/IDE global `.gemini/config/skills`; CLI global `.gemini/antigravity-cli/skills` |
| GitHub Copilot | [Adding agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) | Projekt-Skills unter `.github/skills`, `.claude/skills` oder `.agents/skills`; Ressourcen im Skill-Verzeichnis |
| GitHub-Agent-Umgebung | [Configure the development environment](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/customize-the-agent-environment) | `.github/workflows/copilot-setup-steps.yml` mit Job `copilot-setup-steps` installiert Abhängigkeiten vor Agent-Arbeit |
| ChatGPT | [Skills in ChatGPT](https://help.openai.com/en/articles/20001066) | nur Business, Enterprise, Healthcare, Edu; Upload über „Create“ |
| ECC Tools | [GitHub Marketplace](https://github.com/marketplace/ecc-tools) | private Repos nur mit Pro (19 $ pro Person und Monat) |
| Fremde PDF-Skills | [mineru-refine](https://skillselion.com/skills/LcpMarvel/mineru-refine/plugin), [all2md](https://all2md.readthedocs.io/en/stable/_sources/agent_skills.rst.txt) | mineru-refine nutzt externe APIs; all2md-Lokalität ungeklärt |
| Skill-Verzeichnis | [skills.sh](https://skills.sh/) | kein PDF-/OCR-Skill auf der Bestenliste sichtbar |

> [!note] Grenzen
> Plattformangaben ändern sich schnell. Vor Schritt 6 in [[30 Plan v1.3.0]] die Quellen erneut öffnen und das Abrufdatum hier anpassen.
