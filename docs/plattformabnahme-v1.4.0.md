# Plattformprüfung v1.4.0

> **Historischer Nachweis.** Aktueller Stand und Installation: [README](../README.md).

Prüfdatum: 23.10.2026. Die technische Paketprüfung und die Abnahme des Agent-Verhaltens sind getrennte Nachweise. **Eine vollständige Endabnahme aller fünf Agenten liegt noch nicht vor.**

## Fehlerkorrekturen

Beide Regressionstests schlugen vor der jeweiligen Korrektur fehl und bestanden danach:

- Gelöschter `Seitenindex.md`: `check` liefert einen Fehlerstatus und nennt die fehlende Datei.
- Zwei unterschiedliche PDFs mit alten Bildern namens `page.png`: Nach `extract --alt` verweisen die Manifest-Einträge auf unterschiedliche Zieldateien. Beide gültigen PNGs bleiben bytegleich, ebenso die übernommenen Sichtungsmarken. Dateiendungen bleiben erhalten.

Der vollständige Selbsttest prüft zusätzlich die bisherigen Fehlerfälle, Statusübernahme bei gleichem Hash, Zurückweisung fehlender/geänderter Hashes, Extraktion und Rendering.

## Technische Plattformprüfung

`scripts/plattformtest.py` umfasst sechs Tests: zwei portable Pakete mit bytegleichen Dateien und Ausführung von Hilfe/Extraktion/Prüfung/Rendering aus fremdem Arbeitsverzeichnis, Konfliktschutz, fehlendes Zielprojekt, Schutz gegen Verknüpfungen nach außerhalb sowie Wiederholbarkeit und Bestandsschutz der nativen Installer.

Lokal unter Windows bestanden vier Tests; zwei native PowerShell-Tests wurden durch die bestehende Ausführungsrichtlinie gesperrt und ausdrücklich übersprungen. Die Richtlinie wurde nicht geändert. Die Windows-/Linux-CI verlangt alle sechs Tests ohne Überspringen. Maßgeblich sind die [Actions-Läufe am Release-Tag](https://github.com/Sae-l/pdf-seitenweise-sichten/actions?query=branch%3Av1.4.0); ein früherer grüner Lauf bestätigt keinen späteren Commit.

## Beobachtete Agent-Lesetests

Eigene synthetische `Mechanik.pdf`, zwei Seiten: Aufgabe 1 mit `F = m * a` auf PDF-Seite 1; separater Endantworten-Abschnitt auf Seite 2. Auftrag: Aufgabe finden, Dokument/PDF-Seite/Aufgabe nennen, Formel am Originalbild ansehen, Endantwort zurückhalten. Die Ausführung schreibt ausschließlich in einen isolierten Testordner.

| Umgebung | Beobachtung | Abnahmestand |
| --- | --- | --- |
| Codex Desktop, aktuelle Sitzung | Root-Skill gelesen; portable Kopien erzeugt; Extraktion, `check` und Rendering erfolgreich; Index und ausgewählter Textabschnitt gelesen; Originalbild mit Bildwerkzeug tatsächlich geöffnet. Aufgabe und Formel stimmen mit PDF-Seite 1 überein. | Manueller synthetischer Ablauf bestanden; automatische Skill-Aktivierung in einer frischen Sitzung nicht geprüft. |
| Claude Code 2.1.300 | Projekt-Skill im nativen Skill-Verzeichnis erkannt und über `/pdf-seitenweise-sichten` aufgerufen. Werkzeugprotokoll belegt Lesen des Index, des ausgewählten Markdown-Abschnitts und des PNGs. Antwort nennt Mechanik.pdf, PDF-Seite 1, Aufgabe 1 und die Formel; keine Endantwort. Keine verweigerten Werkzeugaufrufe. | Lesetest bestanden. Nur `Read`/`Skill` erlaubt; Python-Ausführung und Manifest-Aktualisierung durch diesen Agenten wurden nicht abgenommen. |
| Antigravity | Kein ausführbarer Antigravity-Befehl in der verfügbaren Umgebung gefunden. | Native Endabnahme offen. |
| VS Code 1.143.0 / Copilot | VS Code verfügbar; der vorhandene Copilot-CLI-Starter meldet eine fehlende CLI. Kein nativer Copilot-Chat-Auftrag ausgeführt. | Native Endabnahme offen; der CLI-Befund sagt nichts über die VS-Code-Erweiterung aus. |
| GitHub Copilot Cloud | Repository-Einstieg und Setup-Workflow vorhanden. Kein echter Cloud-Agent-Auftrag mit den Testquellen ausgeführt. | Native Endabnahme offen; Setup-CI ersetzt keinen Agent-Auftrag. |

Der Index enthält auch eine Vorschau des Endantworten-Abschnitts. Ein Lesetest mit zurückgehaltener Antwort ist deshalb kein Nachweis, dass der Agent die Lösung nicht im Kontext hatte. Bildsichtung bestätigt die dargestellte Formel, keine umfassende fachliche Prüfung.

## Noch abzunehmen

Für jede Zielumgebung bleibt ein vollständiger Auftrag mit nativer Aktivierung, Python-Ausführung, Bildsichtung, neuen/geänderten PDFs und Statusübernahme erforderlich. Die negativen Fälle sind technisch im Selbsttest abgedeckt, aber damit nicht als Agent-Verhalten aller Plattformen bewiesen. Erneute Messungen an realen Lehrunterlagen und ein Effizienzvergleich wurden für v1.4.0 nicht durchgeführt.
