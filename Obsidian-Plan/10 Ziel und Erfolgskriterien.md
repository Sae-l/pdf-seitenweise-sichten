---
title: "10 Ziel und Erfolgskriterien"
description: "Zweck des projektunabhängigen Skills, Anforderungen an Extraktion und Index sowie messbare Erfolgskriterien."
type: konzept
language: de
created: 2026-10-22
updated: 2026-10-26
status: festgelegt
tags: ["pdf-sichtung", "ziel"]
---

# Ziel und Erfolgskriterien

## Zweck

**pdf-seitenweise-sichten** ist ein projektunabhängiger Agent-Skill mit lokalem Python-Werkzeug. Er erschließt die PDF-Referenzen eines beliebigen Projekts **einmal lokal**: Rohtext pro Seite als Markdown, Originalseiten als Bilder und ein Index, der zeigt, was wo steht. Danach lädt die KI pro Frage nur die passenden Treffer, Seiten und Bilder statt ganzer PDFs. Inhalte bleiben mit Dokument und PDF-Seite belegbar; Formeln, Tabellen und Diagramme werden am Original geprüft.

Begriffe: [[15 Glossar]].

## Einsatzbereich

- **Dokumente:** allgemeine Fach-PDFs mit Text, Formeln, Tabellen, Diagrammen und Scans, beispielsweise Lehrunterlagen, Formelsammlungen, Normen, Datenblätter, Fachartikel und Handbücher. Lehrunterlagen sind der erste erprobte Anwendungsfall, nicht die Grenze.
- **Umgebungen:** Codex, Claude Code, Antigravity, VS Code mit Copilot und GitHub Copilot Cloud, siehe [[31 Plattformen und Installation]].
- **Grenzen:** lokal, ohne Kosten, keine Dokumente an fremde Dienste. Die Agent-Umgebung entscheidet, welche ausgewählten Ausgaben sie an ihren Anbieter übermittelt.

## Anforderungen

### Extraktion

- Rohtext jeder PDF-Seite wird unverändert als Markdown gespeichert, getrennt nach Dokument und PDF-Seite.
- Seitenbilder entstehen vorab nur für Verdachtsseiten (Formel, Tabelle, Diagramm, Scan oder wenig Text). Alle anderen Seiten werden bei Bedarf gerendert. Bilder kosten Speicherplatz, keine Tokens.
- Originale bleiben unverändert. Byte-identische PDFs werden nur einmal erschlossen. Geänderte Quellen werden erkannt.

### Index

Der Index wird automatisch und lokal erzeugt, ohne KI. Er hat drei Ebenen:

1. **Gliederung pro Dokument:** Kapitel mit Seitenbereichen, aus PDF-Lesezeichen oder ersatzweise aus erkannten Überschriften.
2. **Seitenzeile:** kurze Vorschau und Inhaltsart der Seite (Formel, Tabelle, Diagramm, Aufgabe, Scan, wenig Text).
3. **Suche:** wenige Treffer über den gesamten Seitentext, jeweils mit Dokument und PDF-Seite.

Von der KI geschriebene Seitenzusammenfassungen sind eine spätere Option, kein Teil des Index.

### Nutzung durch den Agenten

- Zuerst suchen oder die Gliederung lesen, dann einzelne Seiten lesen, dann bei Bedarf das Originalbild ansehen.
- Lösungsbereiche bleiben im Übemodus verborgen. Ausgeblendete Seiten werden gemeldet.
- Fehlt eine Fundstelle, meldet der Agent das, statt etwas zu erfinden.

### Ausgabeformat

`Seitenindex.md`, `manifest.json`, `md/<pdf>.md` mit `## PDF-Seite N` und `bilder/` bilden ein stabiles, dokumentiertes Format für alle Nutzer. Änderungen daran sind Formatänderungen mit Versionshinweis.

## Erfolgskriterien

### Skill allgemein (Ziel)

| Nr. | Kriterium | Prüfweg |
| --- | --- | --- |
| Z1 | Im Median unter 3 000 Tokens pro Frage, einschließlich `SKILL.md`, Werkzeugausgaben und Bildern | Testfragen am gemischten Testsatz, rechnerisch und je ein echter Lauf |
| Z2 | Keine falsche Formel in einer Antwort | Abgleich jeder ausgegebenen Formel mit dem Original |
| Z3 | Richtige Fundstelle (Dokument und PDF-Seite) bei mindestens 9 von 10 Fragen | Vorher festgelegte erwartete Fundstellen |
| Z4 | Ohne Fundstelle meldet der Agent „nicht gefunden“ samt Suchgrenze | Mindestens eine Testfrage ohne Fundstelle |

**Gemischter Testsatz:** eine Formelsammlung, Vorlesungsfolien, ein reiner Scan und ein PDF ohne Lehrbezug, beispielsweise ein Datenblatt. Testfragen und Messung: Karte [PDF-Pipeline über v1.3.0 hinaus](https://github.com/Sae-l/pdf-seitenweise-sichten/issues/3). Z1–Z4 sind noch nicht gemessen.

### Abnahme v1.3.0 (historisch)

| Nr. | Kriterium | Prüfweg |
| --- | --- | --- |
| E1 | Index höchstens so groß wie beim alten Helfer: ≤ 116 Zeichen pro Seite am CuD-Referenzsatz | `messen.py`, siehe [[20 Ist-Stand und Messung]] |
| E2 | Kein Seitentitel besteht nur aus „Seite N“ | `messen.py`, Wert `titel_nur_seitennummer` = 0 |
| E3 | Byte-identische PDFs werden nur einmal indiziert | `messen.py` gegen Index vergleichen |
| E4 | Prüfstatus pro Seite bleibt nur bei gleicher vorhandener PDF-Prüfsumme erhalten; bei fehlendem oder geändertem Hash bleibt die neue Seite ungeprüft | `scripts/selbsttest.py` und Manifestvergleich |
| E5 | `check` erkennt geänderte PDFs, Überschreibschutz greift | `scripts/selbsttest.py` |
| E6 | Portable Bereitstellung und ein belegter Testauftrag in jeder der fünf Zielumgebungen funktionieren | `scripts/plattformtest.py` plus getrennte Agent-Endabnahmen, siehe [[31 Plattformen und Installation]] |

E1–E5 sind am Stand v1.3.0 erfüllt. E6 ist offen ([[30 Plan v1.3.0]], Schritt 6). E1–E6 bleiben als Regressionsschutz gültig.

## Nicht Teil des Projekts

- Erstellen oder Bearbeiten von PDFs.
- Cloud-OCR und andere Dienste, an die Dokumente gesendet würden.
- Projektspezifische Anwendungen, die das Ausgabeformat lesen, beispielsweise eine Website.
- Automatische fachliche Freigabe: Werkzeug und Hashes bestätigen Aktualität, nicht Richtigkeit.
