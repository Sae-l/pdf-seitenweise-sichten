---
title: "40 Entscheidungen"
description: "Entscheidungsprotokoll zum Skill: was entschieden wurde, warum und wodurch die Entscheidung kippen würde."
type: entscheidung
language: de
created: 2026-10-22
updated: 2026-10-26
status: aktiv
tags: ["pdf-sichtung", "entscheidung"]
---

# Entscheidungen

| Datum | Entscheidung | Grund | Kippt, wenn |
| --- | --- | --- | --- |
| 22.10.2026 | Alter Projekt-Helfer wird Basis von v1.3.0, nicht `sichtung.py` aus v1.2.0 | Gemessen besser bei Indexgröße und Titeln ([[20 Ist-Stand und Messung]]); Duplikate und Prüfstatus werden neu ergänzt | – (umgesetzt, gemessen) |
| 22.10.2026 | Keine Kopf-/Fußzeilen-Entfernung | Anteil am CuD-Satz nur 0–10 % | Abgelöst am 24.10.2026, siehe unten |
| 22.10.2026 | Keine Suche/Datenbank in v1.3.0 | Bei 83 Seiten bleibt der Index klein; Stoppregel in [[10 Ziel und Erfolgskriterien]] | Suche abgelöst am 24.10.2026, siehe unten; Datenbank bleibt geparkt |
| 22.10.2026 | Kein fremder PDF-Skill | `npx skills find` ohne Treffer; mineru-refine sendet Dokumente an externe APIs; all2md ungeprüft ([[91 Quellen und Prüfwege]]) | Ein lokaler, gut belegter Skill taucht auf |
| 22.10.2026 | Verteilung über Verknüpfungen eines Klons und Release-ZIP | Eine Quelle, keine auseinanderlaufenden Kopien ([[31 Plattformen und Installation]]) | – |
| 22.10.2026 | Merge per Squash | Ein Commit pro Version, passend zur bisherigen Historie | – |
| 22.10.2026 | ECC Tools Pro nicht kaufen | 19 $ pro Monat, kein Studentenrabatt genannt, kein Mehrwert für dieses Repo | – (Repo ist seit 22.10.2026 öffentlich; Prüfung damit im kostenlosen Tarif möglich) |
| 22.10.2026 | Ausgabelayout des alten Helfers bleibt unverändert | Die CuD-Website und ihre Tests lesen `Referenz_Sichtung/<Gruppe>/bilder`, `md/` und `manifest.json` direkt | Begründung abgelöst am 26.10.2026, siehe unten |
| 22.10.2026 | Bereits angesehene Bilder haben bei `--alt` Vorrang vor neuem Rendern | Sie sind Prüfnachweis und teils von der Website verlinkt | – |
| 22.10.2026 | Einsatz in CuD vor der Karte über v1.3.0 hinaus | CuD-PDFs sind klein (max. 33 S.); Recherchen kosten Tokens und sind nicht dringend | – |
| 24.10.2026 | Lokale Wortsuche (`search`) und seitenweises Lesen (`read`) eingeführt | Gezielter Zugriff ausdrücklich gewünscht; Agent soll nicht alle Indizes lesen. Gemessen 92–95 % weniger Zeichen in der Auswahlphase | Ein festgelegter Suchtest zeigt eine Lücke, die nur ein anderes Suchverfahren schließt |
| 24.10.2026 | Wiederkehrende Kopfzeilen im oberen Band der ersten Seiten werden dokumentübergreifend gefiltert | Fakultäts-/Institutszeilen verdrängten sinnvolle Vorschauen bei Übungsblättern | Gemeinsame Kapitelüberschriften gehen verloren |
| 26.10.2026 | Der Skill ist projektunabhängig; Lehrunterlagen sind der erste Anwendungsfall | Ziel ist jede Projekt-PDF-Referenz günstig nutzbar zu machen ([[10 Ziel und Erfolgskriterien]]) | – |
| 26.10.2026 | Das Ausgabeformat ist ein stabiles, dokumentiertes Format für alle Nutzer | Andere Werkzeuge und Projekte lesen es direkt; nicht mehr an ein einzelnes Projekt gebunden | Eine Formatänderung bringt messbar mehr als der Umstellungsaufwand; dann mit Versionshinweis |
| 26.10.2026 | Index mit drei Ebenen: Gliederung, Seitenzeile, Suche; automatisch und lokal | Gliederung zeigt „was wo“ ohne Lesen aller Seitenzeilen; KI-Zusammenfassungen kosten Tokens und brauchen Prüfung | Messung zeigt, dass Gliederung und Suche Fundstellen nicht finden |
| 26.10.2026 | Seitenbilder vorab nur für Verdachtsseiten, sonst bei Bedarf | Bilder kosten Speicher, keine Tokens; alle Seiten vorab wäre bei großen PDFs unnötig | Agenten rendern regelmäßig dieselben Seiten nach |
| 26.10.2026 | Erfolgskriterien Z1–Z4 ergänzen E1–E6 | E1–E6 messen Indexgröße und Integrität, nicht Kosten und Richtigkeit pro Frage | – |
| 26.10.2026 | Projektbeispiel aus dem Skill-Paket in den Vault verschoben ([[92 Projektbeispiel Formelsammlung]]) | Projektpfade gehören nicht in einen allgemeinen Skill | – |
| 26.10.2026 | Ziel, Plan und Entscheidungen nur im Vault; `docs/plan-*` und `docs/umsetzung-*` sind historische Nachweise | Eine Quelle statt verstreuter Stände | – |
