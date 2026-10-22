---
title: "40 Entscheidungen"
description: "Entscheidungsprotokoll zum Skill: was entschieden wurde, warum und wodurch die Entscheidung kippen würde."
type: entscheidung
language: de
created: 2026-10-22
updated: 2026-10-22
status: aktiv
tags: ["pdf-sichtung", "entscheidung"]
---

# Entscheidungen

| Datum | Entscheidung | Grund | Kippt, wenn |
| --- | --- | --- | --- |
| 22.10.2026 | Alter Projekt-Helfer wird Basis von v1.3.0, nicht `sichtung.py` aus v1.2.0 | Gemessen besser bei Indexgröße und Titeln ([[20 Ist-Stand und Messung]]); Duplikate und Prüfstatus werden neu ergänzt | – (umgesetzt, gemessen) |
| 22.10.2026 | Keine Kopf-/Fußzeilen-Entfernung | Anteil am CuD-Satz nur 0–10 % | Ein PDF zeigt über 25 % Wiederholung |
| 22.10.2026 | Keine Suche/Datenbank in v1.3.0 | Bei 83 Seiten bleibt der Index klein; Stoppregel in [[10 Ziel und Erfolgskriterien]] | Index eines PDFs über ca. 5 000 Tokens |
| 22.10.2026 | Kein fremder PDF-Skill | `npx skills find` ohne Treffer; mineru-refine sendet Dokumente an externe APIs; all2md ungeprüft ([[91 Quellen und Prüfwege]]) | Ein lokaler, gut belegter Skill taucht auf |
| 22.10.2026 | Verteilung über Verknüpfungen eines Klons und Release-ZIP | Eine Quelle, keine auseinanderlaufenden Kopien ([[31 Plattformen und Installation]]) | – |
| 22.10.2026 | Merge per Squash | Ein Commit pro Version, passend zur bisherigen Historie | – |
| 22.10.2026 | ECC Tools Pro nicht kaufen | 19 $ pro Monat, kein Studentenrabatt genannt, kein Mehrwert für dieses Repo | – (Repo ist seit 22.10.2026 öffentlich; Prüfung damit im kostenlosen Tarif möglich) |
| 22.10.2026 | Ausgabelayout des alten Helfers bleibt unverändert | Die CuD-Website und ihre Tests lesen `Referenz_Sichtung/<Gruppe>/bilder`, `md/` und `manifest.json` direkt | CuD stellt auf ein anderes Format um |
| 22.10.2026 | Bereits angesehene Bilder haben bei `--alt` Vorrang vor neuem Rendern | Sie sind Prüfnachweis und teils von der Website verlinkt | – |
| 22.10.2026 | Einsatz in CuD vor der Karte über v1.3.0 hinaus | CuD-PDFs sind klein (max. 33 S.); Recherchen kosten Tokens und sind nicht dringend | – |
