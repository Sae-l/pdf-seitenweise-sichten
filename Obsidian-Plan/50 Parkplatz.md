---
title: "50 Parkplatz"
description: "Ideen, die bewusst warten, mit dem Anlass, der sie wieder aufruft."
type: parkplatz
language: de
created: 2026-10-22
updated: 2026-10-24
status: geparkt
tags: ["pdf-sichtung", "parkplatz"]
---

# Parkplatz

v1.5.0 enthält bereits lokale Suche, Seitenlesen, Bildrendering und Arbeitsfassungen mit Quellenbezug. [Aktueller Umsetzungsnachweis](../docs/umsetzung-pdf-werkzeug-2026-10-24.md). [[30 Plan v1.3.0]] bleibt der historische Plan.

Die folgenden Erweiterungen brauchen zuerst einen nachgewiesenen Bedarf. Aufwand und Tokenersparnis sind dafür noch nicht gemessen.

| Idee | Nutzen | Anlass zum Starten |
| --- | --- | --- |
| SQLite FTS5 und PDF-Lesezeichen | Größere Bestände schneller durchsuchen und gliedern | Bestehende Suche an einem realen Bestand messbar zu langsam oder ungenau |
| Automatische Diagrammerkennung und Bildexport | Bildseiten gezielter finden | Diagramme werden regelmäßig gesucht; bisherige manuelle Seitenauswahl reicht nicht |
| Lokale OCR und Formelerkennung | Scans und Bildformeln erschließen | Wiederkehrender Bedarf; zuerst an zehn repräsentativen Seiten prüfen |
| Gespeicherte Bildbeschreibungen | Bereits geprüfte Diagramme wiederverwenden | Qualität, Quellenbezug und Aktualisierung an Beispielen nachgewiesen |
| Zusätzliche Suchschichten wie qmd | Andere Suchverfahren vergleichen | Ein festgelegter Suchtest zeigt eine konkrete Lücke |
| Distribution über weitere Skill-Verzeichnisse | Installation erleichtern | Paketformat und Updateverhalten im Zielsystem geprüft |

Eine am Original geprüfte Formel kann bereits heute über `save` als LaTeX-Arbeitsfassung gesichert und später geprüft wieder gelesen werden. Automatische fachliche Richtigkeit folgt daraus nicht.
