# Umsetzungsnachweis: gezielte PDF-Nutzung

Stand: 24.10.2026, lokaler Entwicklungsstand `1.5.0-dev`, unveröffentlicht. Grundlage: Review vom 23.10.2026 und Plan `docs/plan-pdf-werkzeug-2026-10-24.md`. Keine installierten Skill-Kopien verändert.

## Implementiert

- Vorhandenes Python-CLI erweitert, keine neuen Laufzeitabhängigkeiten.
- Integritätsprüfung für Manifest-/Markdown-/Index-Seitenlisten, tatsächliche PDF-Seitenzahl, Dokumentlinks, Bildreferenzen und interne Ausgabepfade. Fehlende/ungültige Manifeste werden verständlich zurückgewiesen.
- Neue Extraktionen besitzen Rohtext-Prüfsummen. Korrekturen werden getrennt gespeichert; alte Extraktionen ohne Rohtextnachweis bleiben mit einem ausdrücklichen Hinweis benutzbar.
- `search` durchsucht lokal auch gruppierte Sichtungen und gibt standardmäßig fünf kurze Treffer aus. Dateiname und Textanfang beeinflussen die Reihenfolge. Aufgabenangaben wie `MPG1_M2 Aufgabe 9` werden als Dateifilter und nummerierter Aufgabenbeginn behandelt. Keine semantische Suche.
- `read` liefert die ausgewählte Seite mit Quellenhash, Status und ausdrücklicher Fortsetzung. Erkannte Lösungen bleiben standardmäßig ausgeblendet. `save` und `read --arbeitsfassung` verbinden aufbereitete Inhalte mit Quelle, Seite und Inhaltshashes; vorhandene Dateien bleiben erhalten.
- Wiederkehrende Erstseitenkopfzeilen im oberen Seitenband werden dokumentübergreifend gefiltert. Erkannte Antworttexte erscheinen nicht in neuen Indexvorschauen.
- `render` dokumentiert Quellenhash, Seite, Maßstab und Bildhash und verwendet passende vorhandene Bilder erneut. Andere vorhandene Bilder werden nicht überschrieben.
- Skill-Anweisung und Nutzungsreferenz beschreiben Text-, Formel-, Tabellen-, Bild- und Scanbehandlung sowie die Grenzen von Statusangaben und Lösungserkennung.

## Automatische Prüfungen

| Prüfung | Beobachtetes Ergebnis |
| --- | --- |
| Erweiterter Selbsttest | bestanden; isolierte Fehlermutationen, Originalseitenzahl trotz konsistenter falscher Metadaten, Pfadausbruch, Lösungsschutz, Suche/Paginierung, Aufgabenangaben, Seitenfortsetzung, Arbeitsfassungen und veränderte Inhalte, Renderwiederverwendung, textlose Raster-/Vektorseiten |
| Plattformtest | sechs Tests, drei bestanden, drei wegen Windows-Richtlinien/Sandbox übersprungen; kein vollständiger Plattformnachweis |
| Portable Kopien | die beiden `.agents`-/`.claude`-Kopien werden im Plattformtest mit Extraktion, Check, Rendering, Suche, Lesen, Speichern und Wiederverwendung aus anderem Arbeitsverzeichnis geprüft |
| Vault | PASS, acht Notizen, 28 Wikilinks, zehn Manifestdateien; Vault unverändert |
| Python-Syntax und Repository-Prüfsummen | abschließend lokal geprüft; neue Referenz, Plan und dieser Bericht in die Prüfsummenliste aufgenommen |
| Skill-Format | einfache Frontmatter-Eigenschaften lokal geprüft; `quick_validate.py` hier nicht ausführbar, da dessen Abhängigkeit PyYAML im verwendeten Interpreter fehlt. Kein nachträglich behaupteter vollständiger Validatorlauf |

Die Sandbox sperrt im Standard-Tempordner erforderliche Schreiboperationen. Testläufe verwendeten deshalb `Test/Umsetzung-2026-10-24/tmp` innerhalb des Projekts. Die Windows-Ausführungsrichtlinie wurde nicht verändert. Junction-Tests werden nur bei konkret gemeldetem Zugriff-Verweigert übersprungen; andere Fehler bleiben Fehler. Die vorhandene CI weist weiterhin jeden übersprungenen Plattformtest zurück.

## Reale MPG1-Unterlagen

27 lokale PDFs mit 218 PDF-Seiten erneut in eigene Ausgabeordner extrahiert. Maßgeblich ist `Test/Umsetzung-2026-10-24/Sichtung-final/`; die erste Zwischenausgabe bleibt als Vergleich erhalten. Alle vier Gruppen bestehen den erweiterten `check`. Original-PDFs und die Sichtung unter `Test/pdf sichten Test/Sichtung/` wurden nicht überschrieben. Vorher-/Nachher-Hashvergleich bei der ersten Extraktion bestätigte beide Bestände unverändert; der abschließende Originalhashvergleich bestand ebenfalls.

Die zwölf ersten Übungsseiten haben jetzt Vorschauen wie „Übungsblatt M1 / Elementare Algebra“ statt Fakultäts-/Institutszeilen. Die Rohtexte sind weiterhin unverändert extrahiert und können fehlerhafte Formeln enthalten.

### Gemessene Suchausgaben

Verglichen werden die Zeichen der vollständigen JSON-Suchausgabe einschließlich Metadaten mit dem vollständigen Index derselben Gruppe. Die erwarteten Quelldateien und PDF-Seiten wurden vor der Prüfung festgelegt. Das ist ein Vergleich der Auswahlphase, keine gesamte Auftrags- oder Modelltokenmessung.

| Suchauftrag | Erwartete Quelle | Indexzeichen | Suchausgabezeichen | Weniger Zeichen |
| --- | --- | ---: | ---: | ---: |
| Potenzen Wurzeln | M1 Elementare Algebra, PDF-S. 5 | 14 432 | 663 | 95,4 % |
| geneigten Straße | MPG1_M2, PDF-S. 4 | 7 891 | 635 | 92,0 % |
| Kräftepolygon | MPG1_M4, PDF-S. 2 | 7 891 | 635 | 92,0 % |
| Potenzgesetze | M1 Elementare Algebra, PDF-S. 5 | 14 432 | 662 | 95,4 % |
| MPG1_M2 Aufgabe 9 | MPG1_M2, PDF-S. 4 | 7 891 | 635 | 92,0 % |

Alle fünf erwarteten Treffer waren enthalten; jeweils ein Treffer wurde ausgegeben. Diese kleinen ausgewählten Fälle belegen keine allgemeine Suchqualität oder Einsparungsquote. Nachfolgendes Seitenlesen, die Skill-Anweisung und Bildkosten sind nicht enthalten. Tatsächliche Modelltoken wurden nicht gemessen.

### Tatsächliche Bild- und Textstichprobe

Text und Bilder wurden für M1 Elementare Algebra, PDF-S. 5 (gedruckte Folie 4), sowie MPG1_M2, PDF-S. 4, tatsächlich geöffnet. Bei M1 sind Exponenten im Rohtext entstellt, obwohl kein Zeichenwarnflag vorliegt. Das Originalbild erlaubt den Abgleich der ausgewählten Potenzgesetze. Bei MPG1_M2 macht das Bild die Bruch-/Wurzelstruktur und das Diagramm der Ballbewegung lesbar.

Nur diese zwei Seiten wurden im neuen Manifest als textgelesen/bildgesehen markiert. `subject_review` bleibt offen. Die M1-Regeln wurden als begrenzte Markdown-/LaTeX-Arbeitsfassung mit `original-geprüft` gespeichert und mit `read --arbeitsfassung` erfolgreich erneut gelesen. Dieser Status bezeichnet den Originalabgleich der enthaltenen Regeln, keine vollständige Transkription oder unabhängige mathematische Prüfung.

Lokale Nachweisdateien: `Test/Umsetzung-2026-10-24/selbsttest.json`, `plattformtest.json`, `extraktion.json`, `suchmessung-final.json`, `wiederverwendung-final.json`. Sie enthalten lokale Pfade; Testunterlagen und Extraktionen sind nicht Teil einer Veröffentlichung. Automatische CLI-Tests sind von vollständigen Agent-Verhaltenstests zu unterscheiden; die Checkliste dafür steht in `references/gezielte-nutzung.md`.

## Bewusste Grenzen

Keine neue Datenbank, Embeddings, Oberfläche, automatische Formelkorrektur oder flächendeckende OCR. OCR kann bei Bedarf als vorhandenes lokales Werkzeug genutzt werden; sie ist hier nicht integriert. Ein PDF ohne Text bleibt thematisch über Textsuche unvollständig erschlossen. Die heuristische Lösungserkennung ist kein vollständiger Schutz vor unmarkierten Antworten, auch nicht in Bildern oder frei erstellten Arbeitsfassungen.

Eine Arbeitsdatei pro Dokument/Seite; verlinkte Begleitdateien werden nicht automatisch mitkopiert. Bildausschnitte können als eigene Arbeitsdatei gespeichert werden, werden aber nicht automatisch erzeugt oder geometrisch vermessen. Solche Ausschnitte benötigen ihren Kontext und Lagebezug im Beschreibungstext.

Kein neuer CuD-Vergleichslauf, keine Linux-Ausführung, keine GitHub-CI-/Releaseprüfung und keine vollständige Endabnahme aller fünf Agent-Oberflächen. Kein Commit, Release oder Update lokaler Installationen in diesem Arbeitsschritt.

## Nachtrag zur Release-Vorbereitung v1.5.0

Der vollständige `quick_validate.py`-Lauf besteht für Root-Skill und GitHub-Einstieg mit isoliert bereitgestelltem PyYAML 6.0.3. Diese reine Prüfabhängigkeit wird weder Laufzeitvoraussetzung noch Teil des Skill-Pakets. Die frühere Validatorgrenze im Entwicklungsnachweis ist damit für den Release-Kandidaten geschlossen. Lokale Windows-Skips und offene fachliche/Agent-Endabnahmen bleiben unverändert. Der neue manuelle Start der vorhandenen Release-Action ersetzt hier die ungültige lokale CLI-Anmeldung; bestehende Sicherheitsregeln und Jobrechte bleiben erhalten.
