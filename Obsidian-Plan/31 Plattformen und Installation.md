---
title: "31 Plattformen und Installation"
description: "Bereitstellung für Codex, Claude Code, Antigravity, VS Code/Copilot und GitHub Copilot mit offiziellen Quellen und getrennten Prüfstufen."
type: referenz
language: de
created: 2026-10-22
updated: 2026-10-24
status: teilweise-geprüft
tags: ["pdf-sichtung", "installation"]
---

# Plattformen und Installation

Grundsatz: **ein Skill-Inhalt, passende Bereitstellung je Umgebung**. Codex, Claude Code, Antigravity, VS Code mit Copilot und GitHub Copilot sind die fünf Zielumgebungen. Eine ausführbare Python-Installation und Zugriff auf die benötigten Quellen sind Voraussetzung. Die normalen GitHub-Webseiten selbst führen keinen Skill aus.

| Werkzeug | Global | Pro Projekt | Aufruf |
| --- | --- | --- | --- |
| Codex | `~/.agents/skills/` | `.agents/skills/` | `$pdf-seitenweise-sichten` |
| Claude Code | `~/.claude/skills/` | `.claude/skills/` | `/pdf-seitenweise-sichten` |
| Antigravity App/IDE | `~/.gemini/config/skills/` | `.agents/skills/` | `/pdf-seitenweise-sichten` |
| Antigravity CLI | `~/.gemini/antigravity-cli/skills/` | `.agents/skills/` | Skill explizit auswählen/nennen |
| VS Code mit Copilot | `~/.agents/skills/` (auch weitere dokumentierte Pfade) | `.agents/skills/`, `.github/skills/`, `.claude/skills/` | `/pdf-seitenweise-sichten` |
| GitHub Copilot Cloud | Kein Zugriff auf lokale globale Ordner | `.agents/skills/`, `.github/skills/`, `.claude/skills/` im Zielrepository | Skill-Namen und Auftrag nennen |

Quellen am 22.10.2026 erneut abgerufen: [[91 Quellen und Prüfwege]]. Die Pfade bezeichnen jeweils den Elternordner des Unterordners `pdf-seitenweise-sichten/` mit `SKILL.md`.

## Installation

Portable Projektinstallation aus dem geklonten Repository oder entpackten Skill-Paket:

```text
python scripts/install_projekt.py <vorhandener-projektordner>
```

Erzeugt vollständige Kopien in `.agents/skills/pdf-seitenweise-sichten/` und `.claude/skills/pdf-seitenweise-sichten/`. Bestehende Ziele werden nicht überschrieben. Kopien vor einem Update vergleichen und sichern. Für GitHub die Kopien im Zielrepository committen; dort keine lokalen Junctions verwenden.

Die bisherigen `install.ps1`/`install.sh` verknüpfen stattdessen einen lokalen Klon in die vier globalen Ordner aus der Tabelle. Passende Links können wiederholt verwendet werden; echte Kopien und fremde Links bleiben erhalten und erzeugen einen Fehlerstatus. Für isolierte Profile/Tests akzeptieren die Installer `-Zielbasis <ordner>` bzw. `bash install.sh <ordner>`. Die Python-Abhängigkeiten separat installieren.

Dieses Repository enthält einen GitHub-Einstieg unter `.github/skills/pdf-seitenweise-sichten/SKILL.md` und einen `copilot-setup-steps.yml`-Workflow für Python und PDF-Abhängigkeiten. Der Einstieg verweist auf die verbindliche Root-`SKILL.md`; die Anweisungen werden nicht doppelt gepflegt. In anderen Zielrepositories deren bestehendes Copilot-Setup ergänzen, nicht ersetzen.

## Prüfstufen

| Stufe | Nachweis | Aussage |
| --- | --- | --- |
| Format/Pfade | Offizielle Quellen und Skill-Validierung | Dateien liegen im vorgesehenen Format; keine Garantie automatischer Aktivierung |
| Portable Ausführung | `python scripts/plattformtest.py` | Beide Projektpakete extrahieren, prüfen und rendern aus einem anderen Arbeitsverzeichnis; Unicode/Leerzeichen und Konfliktschutz geprüft |
| Native Installer | Derselbe Plattformtest auf Windows/Linux | Junctions/Symlinks, Wiederholbarkeit und Schutz vorhandener Kopien; CI darf keine Tests überspringen |
| Copilot-Setup | Workflow `Copilot Setup Steps` | Python-Abhängigkeiten und technische Tests ausführbar; keine Bestätigung eines echten Copilot-Auftrags |
| Agent-Endabnahme | Ein belegter Testauftrag je Zielumgebung | Synthetische Lesetests in Codex und Claude Code durchgeführt; vollständige Endabnahme aller Zielumgebungen offen. [Abnahmebericht v1.4.0](../docs/plattformabnahme-v1.4.0.md) |

Für v1.5.0 sind im [CI-Lauf des Release-Commits](https://github.com/Sae-l/pdf-seitenweise-sichten/actions/runs/40051849224) Windows und Linux erfolgreich; jeweils alle sechs Plattformtests ohne übersprungene Tests. Das bestätigt technische Bereitstellung, keine vollständige Agent-Endabnahme.

Im lokalen Windows-Lauf wurden drei native Tests wegen Ausführungsrichtlinie bzw. Junction-Berechtigung übersprungen; die drei portablen Tests bestanden. Sicherheitsrichtlinien wurden nicht umgangen. Details: [Umsetzungsnachweis](../docs/umsetzung-pdf-werkzeug-2026-10-24.md). Die [Installationsanleitung](../docs/installation.md) führt neue Nutzer durch Projektkopie, ZIP und Updates.

## Bekannte Grenzen

- Bestehende persönliche Skills gleichen Namens können eine Projektkopie überlagern oder doppelt erscheinen. Alte Kopien unter `~/.codex/skills/` prüfen und erst nach Sicherung bereinigen.
- Cloud-Agenten haben keinen Zugriff auf lokale Laufwerke. Quellen müssen in ihrer Umgebung vorhanden sein; PDF-Sichtung in einer eingeschränkten Code-Review-Oberfläche ist nicht automatisch möglich.
- Ohne Werkzeug zum tatsächlichen Anzeigen eines Bildes bleibt die Originalbildprüfung offen. Ein gerendertes Bild reicht nicht als Nachweis.
- Claude-Code-Cloudsitzungen lesen keine lokalen persönlichen Skill-Ordner; Account-Skills und Repository-Skills unterscheiden sich je Sitzungstyp. Die obige Claude-Code-Zeile bezeichnet den lokalen Agenten.
- ChatGPT-/claude.ai-Uploads sind kein Teil der fünf hier verlangten Endabnahmen; das Release-ZIP allein bestätigt deren Unterstützung nicht.

## Gemeinsamer Endabnahmetest

In jeder Zielumgebung denselben kleinen, selbst erstellten PDF-Satz verwenden. Den Skill ausdrücklich auswählen und eine Aufgabe mit Dokument, PDF-Seite und Aufgabennummer finden lassen. Einmal eine Formel am Originalbild prüfen, einmal eine neue PDF hinzufügen und `check` scheitern lassen. Bei unveränderter PDF Status übernehmen, bei verändertem oder fehlendem Hash nicht. Endantworten sollen auf Wunsch zurückgehalten werden.

Pro Lauf Werkzeugversion, Skill-Commit, Quellen-Hashes, Auftrag und beobachtete Ergebnisse festhalten. Erst danach die betreffende Agent-Endabnahme als bestanden markieren. Plan: [[30 Plan v1.3.0]].
