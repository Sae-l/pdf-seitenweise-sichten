# Plan: tokensparsame, belegbare PDF-Nutzung

Stand: 24.10.2026. Planungsentwurf auf Grundlage des lokalen Reviews vom 23.10.2026. Noch keine Implementierung und keine neue Abnahme.

## Ziel und Entscheidung

PDFs einmal lokal erschließen und anschließend pro Frage nur relevante Textseiten, Bilder oder geprüfte Arbeitsfassungen an den Agenten geben. Texte, Formeln, Tabellen und Diagramme müssen mit Original und PDF-Seite verbunden bleiben.

Das bestehende Python-Werkzeug wird erweitert. Der Skill bleibt die kurze Arbeitsanweisung für Auswahl, tatsächliche Bildansicht, Quellenangaben und offene Unsicherheiten. Er ist weder Suchmaschine noch automatischer fachlicher Prüfer.

Erste Version: vorhandene lokale Dateien und Bibliotheken nutzen, keine zusätzliche Datenbank, keine Embeddings, keine Cloud-OCR und keine neue Oberfläche. Die geparkte Suche wird wegen des jetzt ausdrücklich gewünschten gezielten Zugriffs aufgegriffen; SQLite und weitere Suchsysteme bleiben bis zu einem gemessenen Bedarf zurückgestellt.

## Ablauf für eine Nutzerfrage

1. Quellenbestand und Ausgabe technisch prüfen; unveränderte Aufbereitung wiederverwenden.
2. Lokal suchen. Nur wenige Treffer mit Dokument, PDF-Seite, kurzem Ausschnitt und Warnungen zurückgeben. Auch in großen Beständen muss der Agent nicht zuerst sämtliche Seitenindizes lesen.
3. Ausgewählte Seitenabschnitte vollständig lesen. Fortsetzungen auf Nachbarseiten nur bei Bedarf hinzunehmen. Nummer der PDF-Seite und gedruckte Foliennummer getrennt behandeln.
4. Für Formeln, Tabellen, Diagramme und Fotos die relevante Originalseite öffnen. Ein Warnflag ist keine Voraussetzung dafür. Ein erzeugtes Bild ist noch keine Bildsichtung.
5. Benötigte Inhalte als kleine Arbeitsfassung speichern: normaler Text als Markdown, Formeln als LaTeX, Tabellen als Markdown oder CSV, Bilder mit Beschreibung. Nur benötigte Inhalte aufbereiten; Unsicherheiten ausweisen und Quellen je Abschnitt erhalten.
6. Bei späteren Fragen vorhandene Arbeitsfassungen anbieten, wenn Quellenhash und Herkunft noch passen. Fachliche Freigabe nicht aus technischer Aktualität ableiten.

## Phase 1: nachgewiesene Fehler beheben

### Technischen Check vervollständigen

- Fehlendes oder ungültiges Manifest verständlich zurückweisen.
- PDF-Seitenzahl, Markdown-Seitenfolge und Manifest-Seitenliste gegeneinander prüfen.
- Indexeinträge und Markdown-Linkziele kontrollieren, einen leeren Index zurückweisen.
- Eingetragene Bilder auf zulässigen Pfad und Existenz prüfen. Ein späterer Bild-Hash kann die Bindung eines tatsächlich geprüften Ausschnitts zusätzlich sichern.
- Erfolgsmeldung auf technische Integrität begrenzen.
- Rohtext und absichtlich korrigierte Arbeitsfassung unterscheiden. Die PDF-Prüfsumme bestätigt keine unveränderte Extraktion und keine richtige Formel.

### Vorschauen verbessern

- Wiederkehrende Erstseitenkopfzeilen anhand mehrerer Dokumente berücksichtigen; keine TH-Köln-Sonderliste einbauen. Wiederholung allein darf sinnvolle gemeinsame Kapitelüberschriften nicht entfernen.
- Ab erkanntem Lösungsbeginn keine Lösungstexte als Vorschau ausgeben. Auf gemischten Seiten nur den Aufgabenbereich für die Vorschau nutzen.
- Lösungsmarker bleiben eine Heuristik. Bei unklarer Trennung im Übemodus die Ausgabe zurückhalten und die Seite gezielt prüfen.

### Umgebung und Tests richtig behandeln

- Vorhandenen Python-Interpreter mit benötigten Bibliotheken bestimmen, keine automatische Installation auslösen.
- Beschreibbaren Tempordner für Tests verwenden.
- Sicherheitsrichtlinien erhalten. Gesperrte Junction-/Installertests als blockiert oder übersprungen ausweisen; keine Produktfreigabe daraus ableiten.

Abnahme: Jede Prüflücke mit einer eigenen, isolierten Mutation testen. Der unveränderte Bestand muss bestehen. Bestehende Selbst- und Plattformtests weiterverwenden. Originalsichtung und PDFs nicht überschreiben.

## Phase 2: gezielten Textzugriff ergänzen

Geplante CLI-Erweiterungen, noch keine verfügbaren Befehle:

```text
sichtung.py search <sichtungsordner> <suchtext>
sichtung.py read <sichtungsordner> <dokument> <pdf-seite>
```

`search` durchsucht die lokal gespeicherten Seitenabschnitte und liefert standardmäßig höchstens fünf Treffer mit je ungefähr 160 Zeichen Vorschau sowie Gesamtzahl und Hinweis auf weitere Treffer. Der erste Ansatz verwendet einfache, Unicode-taugliche Wortsuche mit stabiler Sortierung. Für Folgefragen werden Suchbegriffe oder Dokumentauswahl präzisiert. Keine Garantie für Synonyme oder semantische Suche.

`read` liefert genau den angeforderten Seitenabschnitt samt Quellenangabe und Status. Keine stille Kürzung. Bei außergewöhnlich langen Seiten wird eine ausdrückliche Fortsetzung benötigt und die Unvollständigkeit angezeigt; Suche bleibt nur Auswahlhilfe.

Lösungsschutz gilt auch für Suchtreffer und Leseausgaben im Übemodus. Die interne lokale Suche darf Lösungstext kennen; sie darf ihn dann nicht als Treffertext an den Nutzer weiterreichen. Aufgaben auf gemischten Seiten nicht unnötig verstecken. Für einen verlässlichen Schutz reichen Dokumentflags allein nicht: Trennstellen im Text berücksichtigen und unklare Fälle offenhalten. Bild- und Exportausgaben müssen denselben Schutz beachten.

Abnahme: Trefferquelle und Seitenzahl stimmen; keine Nachbarseite versehentlich ausgegeben; Trefferbegrenzung ist sichtbar; Lösungstext erscheint im Übemodus nicht; lange Seiten verlieren keinen Inhalt unbemerkt.

## Phase 3: Bilder, Scans und Layout gezielt nutzen

Bestehendes `render` weiterverwenden. Aus dem Original gerenderte Seiten funktionieren auch bei Vektorzeichnungen und gemischtem Layout; eingebettete Rasterbilder allein bilden solche Seiten nicht vollständig ab.

- Zuerst nur die benötigte Seite rendern und ansehen.
- Falls Details unlesbar sind: Auflösung gezielt erhöhen. Einen Ausschnitt erst nach Orientierung auf der ganzen Seite erzeugen; Seite und Ausschnittsposition dokumentieren.
- Vorhandene passende Bilder wiederverwenden. Quelle, PDF-Seite, Renderparameter und gegebenenfalls Ausschnitt an die verwendete Bilddatei binden.
- Beschreibungen von Bildern und Diagrammen nur bei tatsächlicher Nutzung erstellen und später wiederverwenden. Keine automatisch erzeugten Beschreibungen aller Seiten.
- Bei Scans: Ohne OCR ist die lokale Textsuche unvollständig. Das sichtbar ausweisen. Erst relevante Seiten visuell auswählen; OCR für benötigte Seiten einsetzen, falls ein geeignetes lokales Werkzeug vorhanden ist. Ein Scan-Thema ohne Texttreffer ist kein nachgewiesener Fehlbestand.
- Ganze Bildseiten mit Lösungen im Übemodus nicht ungefiltert als Nutzerartefakt ausgeben; erforderlichenfalls nur den geprüften Aufgabenbereich verwenden.

Abnahme: synthetische Testseiten mit Rasterbild, Vektordiagramm und Scan. Kein falscher Leerbefund bei fehlendem Text, keine behauptete Ansicht ohne Bildzugang. Diagrammachsen, Einheiten, Legenden und Formeldetails bleiben erkennbar.

## Phase 4: geprüfte Inhalte wiederverwendbar machen

Die vorhandenen Rohdateien bleiben Suchgrundlage. Eine getrennte Arbeitsfassung enthält nur die tatsächlich benötigten Inhalte, beispielsweise:

```text
Arbeitsfassung/
  Potenzgesetze.md
  Messwerte.csv
  bilder/Diagramm-S012.png
```

Jeder Abschnitt erhält mindestens: Quelldatei, PDF-S., PDF-SHA-256, Art der Bearbeitung und Prüfstatus. Bei Bildbezug zusätzlich Bilddatei und Ausschnittsbezug. Keine neue universelle Wissensdatenbank entwerfen; zunächst Markdown mit Quellenzeile verwenden.

| Inhalt | Nutzbares Ergebnis | Erforderliche Prüfung |
| --- | --- | --- |
| Fließtext | bereinigter Markdown-Abschnitt | ausgewählten Text lesen; bei Layoutzweifeln Original ansehen |
| Formel | LaTeX und Bedeutung benötigter Größen | Exponenten, Indizes, Zeichen und Einheiten am Original vergleichen |
| Tabelle | Markdown oder CSV | Spalten, Zeilen, Einheiten und Zahlen am Original vergleichen |
| Diagramm/Bild | Seitenbild oder Ausschnitt plus Beschreibung | tatsächliche Ansicht; Achsen, Legende und Kontext berücksichtigen |
| Scan | OCR-Text mit Quellenbezug | OCR als ungeprüft markieren, verwendete Aussagen am Bild kontrollieren |

Vorhandene Statusfelder weiterverwenden. Nur wirklich gelesene oder angesehene Seiten markieren; `subject_review` bleibt ohne fachliche Prüfung offen. Eine Aufbereitung kann teilweise geprüft sein. Bei Änderungen an der Quelle werden alte Inhalte als veraltet markiert und nicht still überschrieben oder als aktuell ausgegeben.

## Phase 5: Nutzen und Tokenkosten messen

Mit denselben fünf Aufträgen den bisherigen Ablauf und den neuen vergleichen: Thema finden, Aufgabe belegen, Formel ohne Warnflag prüfen, Diagramm erklären, Aufgabe ohne Endantwort bearbeiten. Zusätzlich Scan ohne OCR und fehlenden Bildzugang testen. Erwartete Quellen und Prüfschritte vorher festlegen.

Messen:

- richtige Datei und PDF-Seite, belegte Aussagen, offene Unsicherheiten;
- tatsächlich an den Agenten zurückgegebener Text und tatsächlich geöffnete Bilder;
- Werkzeugaufrufe, Laufzeit und Nutzen der Wiederverwendung;
- tatsächliche Text-/Bildtokens, sofern die Agent-Umgebung sie ausweist. Zeichen nur als getrennten Näherungswert berichten; aus Bilddateigröße keine Tokenzahl ableiten.

Ziel: zunächst mindestens halb so viel zurückgegebenen Text wie beim bisherigen vollständigen Indexlesen für die festgelegten Suchaufträge, ohne schlechtere Quellenrichtigkeit oder ausgelassene nötige Bildprüfung. Das ist ein zu prüfendes Ziel, kein heutiges Ergebnis. Bildkosten getrennt ausweisen. Wiederholungsaufträge müssen vorhandene unveränderte Aufbereitung nutzen können.

Technische Abnahme mit synthetischen PDFs; ergänzend lokale MPG1-Stichproben und vorhandenen CuD-Vergleich verwenden, soweit die Quellen verfügbar sind. Keine fremden Lehrunterlagen in öffentliche Testfixtures übernehmen. Agent-Endabnahmen je Zielumgebung bleiben separat.

## Betroffene Dateien und Reihenfolge

1. `scripts/sichtung.py`, `scripts/selbsttest.py`: Prüflücken und Vorschauen beheben.
2. Dieselben Dateien: begrenzte Suche und seitenweises Lesen ergänzen; bestehende CLI erhalten.
3. `SKILL.md`: kurzen Such-/Lese-/Bild-/Aufbereitungsablauf beschreiben; ausführliche Beispiele nach `references/` auslagern. Rendering nur um nachgewiesen benötigte Details erweitern.
4. Kleines Verhaltenstest-Protokoll mit selbst erstellten PDFs hinzufügen. Vorhandene Mess- und Plattformprüfungen nutzen.
5. `README.md`, `CHANGELOG.md`, `SHA256SUMS`, bei Skilländerung `ARCHIVE.json` anpassen. Vault und sein Manifest nur bei dortigen Änderungen aktualisieren; portable Kopien prüfen.

Kein Release und keine Installation Bestandteil dieses Planungsauftrags. Bereits vorhandene Extraktionen bleiben erhalten. Erst nach bestandener Fehlerkorrektur wird die gezielte Nutzung erweitert.
