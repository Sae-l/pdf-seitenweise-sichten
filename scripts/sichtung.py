#!/usr/bin/env python3
"""PDF-Text lokal speichern; im Chat genügt der knappe Seitenindex.

  sichtung.py extract <pdf-ordner> <neuer-ausgabeordner> [--alt <alter-sichtungsordner>] [--titel "<Überschrift>"]
  sichtung.py check   <ausgabeordner>
  sichtung.py render  <pdf-datei> <seite> <ausgabeordner> [--scale 2]

Ausgabe (gleiches Layout wie der bisherige Projekt-Helfer):
  Seitenindex.md, manifest.json, md/<pdf>.md mit "## PDF-Seite N", bilder/<pdf>-S###.png
Benötigt: pypdfium2. Originale werden nur gelesen.
"""
from pathlib import Path
import argparse, collections, hashlib, json, os, re, sys
from urllib.parse import quote

try:
    import pypdfium2 as pdfium
except ImportError:
    sys.exit("pypdfium2 fehlt: python -m pip install pypdfium2")

STATUS = dict(text_read=False, original_image_viewed=False, subject_review="offen")
SEITENZAHL = re.compile(r"^(Seite \d+( von \d+)?|\d+( / \d+)?|©.*)$")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def alte_pruefungen(ordner):
    """Prüfstatus aus früheren manifest.json-Dateien, Schlüssel (PDF-Name, Seite)."""
    alt = {}
    for manifest in Path(ordner).rglob("manifest.json"):
        daten = json.loads(manifest.read_text(encoding="utf-8"))
        for doc in daten if isinstance(daten, list) else []:
            for seite in doc.get("page_index", []):
                bild = manifest.parent / seite["image"] if seite.get("image") else None
                alt[(Path(doc["pdf"]).name, seite["page"])] = (doc.get("sha256"), {k: seite[k] for k in STATUS if k in seite}, bild)
    return alt


def extract(quelle, ziel, alt_ordner=None, ueberschrift=None):
    quelle, ziel = Path(quelle), Path(ziel)
    sources = sorted(quelle.glob("*.pdf")) if quelle.is_dir() else []
    if not sources:
        sys.exit(f"Keine PDFs im Quellordner: {quelle}")
    if (ziel / "Seitenindex.md").exists() or (ziel / "manifest.json").exists():
        sys.exit(f"Index oder Manifest in {ziel} existiert bereits. Neuen Ausgabeordner wählen und erst nach Vergleich übernehmen.")
    (ziel / "md").mkdir(parents=True, exist_ok=True)
    (ziel / "bilder").mkdir(exist_ok=True)
    alt = alte_pruefungen(alt_ordner) if alt_ordner else {}
    records, gesehen, uebernommen = [], {}, 0
    index = [f"# {ueberschrift or 'Seitenindex: ' + quelle.name}", "",
             "Maschinelle Textextraktion zum Suchen. Formeln, Tabellen und Zeichnungen am Original prüfen.", ""]
    for source in sources:
        hashwert = sha256(source)
        if hashwert in gesehen:
            index += [f"## {source.stem}", f"Byte-identisch mit {gesehen[hashwert]}; nicht erneut indiziert.", ""]
            records.append(dict(pdf=source.name, sha256=hashwert, duplicate_of=gesehen[hashwert]))
            continue
        gesehen[hashwert] = source.name
        document = pdfium.PdfDocument(source)
        texte = []
        for number in range(1, len(document) + 1):
            textpage = document[number - 1].get_textpage()
            texte.append(textpage.get_text_range().replace("\r\n", "\n").replace("\r", "\n"))
            textpage.close()
        # Zeilen auf mindestens der Hälfte der Seiten sind Kopf-/Fußzeilen und taugen nicht als Titel.
        zaehler = collections.Counter(z for t in texte for z in {l.strip() for l in t.splitlines() if l.strip()})
        wiederholt = {z for z, c in zaehler.items() if len(texte) >= 4 and c >= len(texte) / 2}
        relative_source = Path(os.path.relpath(source, ziel / "md")).as_posix()
        extracted = [f"# {source.stem}", "", f"Quelle: {relative_source}",
                     "Die Seitenzahlen unten sind PDF-Seiten, keine behaupteten Foliennummern.", ""]
        index += [f"## {source.stem} ({len(document)} PDF-Seiten)",
                  f"[Markdown]({quote('md/' + source.stem + '.md', safe='/')})", ""]
        pages, answer_start_page = [], None
        for number, raw in enumerate(texte, 1):
            lines = [l.strip() for l in raw.splitlines() if l.strip()]
            meaningful = [l for l in lines if l not in wiederholt and not SEITENZAHL.match(l)]
            headings = [l for l in meaningful if re.search(r"[A-Za-zÄÖÜäöüß]{4}", l)]
            preview = " / ".join(headings[:2] or meaningful[:3])[:100].replace("|", "/")
            thin = len(re.sub(r"\s", "", raw)) < 80
            damaged = bool(re.search(r"[�-]", raw))
            tasks = bool(re.search(r"\b(Übung\w*|Aufgabe\w*|Beispiel\w*)\b", raw, re.I))
            if "Endantworten:" in raw and answer_start_page is None:
                answer_start_page = number
            flags = [label for yes, label in [(thin, "wenig Text"), (damaged, "Zeichen prüfen"), (tasks, "Aufgabe/Beispiel")] if yes]
            if answer_start_page is not None:
                flags.append("Endantworten-Abschnitt")
            extracted += [f"## PDF-Seite {number}", "", "```text", raw.strip(), "```", ""]
            index.append(f"- S. {number}: {preview}" + (" [" + ", ".join(flags) + "]" if flags else ""))
            image, status = None, dict(STATUS)
            alt_hash, alt_status, alt_bild = alt.get((source.name, number), (None, None, None))
            if alt_status is not None and alt_hash == hashwert:
                status.update(alt_status)
                uebernommen += 1
                if alt_bild and alt_bild.is_file():  # bereits angesehenes Bild hat Vorrang vor neuem Rendern
                    image = f"bilder/{source.stem}-S{number:03}{alt_bild.suffix}"
                    (ziel / image).write_bytes(alt_bild.read_bytes())
            if image is None and (thin or damaged):
                image = f"bilder/{source.stem}-S{number:03}.png"
                page = document[number - 1]
                page.render(scale=1.5).to_pil().save(ziel / image)
                page.close()
            pages.append(dict(page=number, characters=len(raw), flags=flags, image=image, **status))
        target = ziel / "md" / f"{source.stem}.md"
        target.write_text("\n".join(extracted), encoding="utf-8")
        records.append(dict(pdf=source.name, sha256=hashwert, pages=len(document),
                            markdown=f"md/{source.stem}.md", answer_start_page=answer_start_page, page_index=pages))
        document.close()
        index.append("")
    (ziel / "Seitenindex.md").write_text("\n".join(index), encoding="utf-8")
    (ziel / "manifest.json").write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    seiten = sum(r.get("pages", 0) for r in records)
    print(f"{len(records)} PDFs, {seiten} Seiten, {sum(1 for r in records if 'duplicate_of' in r)} Duplikate, "
          f"{sum(p['image'] is not None for r in records for p in r.get('page_index', []))} Bildfälle, "
          f"{uebernommen} Prüfstände übernommen.")
    return check(ziel, quelle)


def check(ziel, quelle=None):
    """Abschnitte gegen Seitenzahl und PDF-Hashes gegen das Manifest prüfen; gibt Anzahl Probleme zurück."""
    ziel = Path(ziel)
    probleme = 0
    if not (ziel / "Seitenindex.md").is_file():
        print("FEHLER: Seitenindex.md fehlt"); probleme += 1
    records = json.loads((ziel / "manifest.json").read_text(encoding="utf-8"))
    if not records:
        print("FEHLER: Manifest enthält keine PDFs")
        return 1
    for d in records:
        if "duplicate_of" not in d:
            md = ziel / d["markdown"]
            if not md.is_file():
                print(f"FEHLER {md.name}: Markdown fehlt"); probleme += 1
                continue
            text = md.read_text(encoding="utf-8")
            abschnitte = [int(n) for n in re.findall(r"(?m)^## PDF-Seite (\d+)$", text)]
            if abschnitte != list(range(1, d["pages"] + 1)):
                print(f"FEHLER {md.name}: Seitenabschnitte fehlen, sind doppelt oder falsch geordnet"); probleme += 1
            if quelle is None:  # Quellordner aus der "Quelle:"-Zeile des ersten Markdowns ableiten
                source = re.search(r"(?m)^Quelle: (.+)$", text)
                if source:
                    quelle = (md.parent / source.group(1)).parent
    if quelle is None or not Path(quelle).is_dir():
        print("FEHLER: Quellordner fehlt oder ist nicht bestimmbar")
        return probleme + 1
    for name in sorted({p.name for p in Path(quelle).glob("*.pdf")} - {d["pdf"] for d in records}):
        print(f"VERALTET {name}: neue PDF, neu extrahieren"); probleme += 1
    for d in records:
        pdf = Path(quelle) / d["pdf"]
        if not pdf.exists():
            print(f"WARNUNG {d['pdf']}: Original nicht gefunden"); probleme += 1
        elif not d.get("sha256"):
            print(f"UNGEPRÜFT {d['pdf']}: SHA-256 fehlt, neu extrahieren"); probleme += 1
        elif sha256(pdf) != d["sha256"]:
            print(f"VERALTET {d['pdf']}: PDF geändert, neu extrahieren"); probleme += 1
    if not probleme:
        print("OK: Index aktuell, Abschnittszahlen stimmen")
    return probleme


def render(pdf, seite, ziel, scale):
    ziel = Path(ziel); ziel.mkdir(parents=True, exist_ok=True)
    doc = pdfium.PdfDocument(str(pdf))
    if not 1 <= seite <= len(doc):
        sys.exit(f"Seite {seite} außerhalb 1–{len(doc)}")
    out = ziel / f"{Path(pdf).stem}-S{seite:03}.png"
    doc[seite - 1].render(scale=scale).to_pil().save(out)
    print(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract"); e.add_argument("quelle"); e.add_argument("ziel")
    e.add_argument("--alt", help="früherer Sichtungsordner, dessen Prüfstatus übernommen wird")
    e.add_argument("--titel", help="Überschrift des Seitenindex")
    c = sub.add_parser("check"); c.add_argument("ziel")
    r = sub.add_parser("render"); r.add_argument("pdf"); r.add_argument("seite", type=int)
    r.add_argument("ziel"); r.add_argument("--scale", type=float, default=2)
    a = ap.parse_args()
    if a.cmd == "extract":
        sys.exit(1 if extract(a.quelle, a.ziel, a.alt, a.titel) else 0)
    if a.cmd == "check":
        sys.exit(1 if check(a.ziel) else 0)
    render(a.pdf, a.seite, a.ziel, a.scale)
