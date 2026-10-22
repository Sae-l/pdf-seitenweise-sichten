#!/usr/bin/env python3
"""Seitenindex.md + Markdown je PDF-Seite erzeugen, Index-Aktualität prüfen, einzelne Seiten rendern.

  sichtung.py extract <pdf-datei-oder-ordner> <neuer-ausgabeordner>
  sichtung.py check   <ausgabeordner>
  sichtung.py render  <pdf-datei> <seite> <ausgabeordner> [--scale 2]

Benötigt: pypdfium2 (pip install pypdfium2). Originale werden nur gelesen.
"""
import argparse, hashlib, json, re, sys
from pathlib import Path

try:
    import pypdfium2 as pdfium
except ImportError:
    sys.exit("pypdfium2 fehlt: pip install pypdfium2")

WENIG_TEXT = 20  # Zeichen; darunter vermutlich Scan oder reine Abbildung (Titelfolien liegen meist darüber)
# Zeichen, bei denen die Textextraktion Formeln häufig verfälscht
FORMEL_ZEICHEN = re.compile(r"[∑∫√∂∇≈≤≥±×·⋅→⃗²³⁻¹₀-₉αβγδεηθλμνπρστφωΩΔ]|\^|_\{")


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def pdfs(quelle):
    q = Path(quelle)
    return sorted(q.rglob("*.pdf")) if q.is_dir() else [q]


def titel(text):
    for zeile in text.splitlines():
        z = zeile.strip()
        if len(z) >= 3:
            return z[:70].replace("|", "/")
    return ""


def flags(text):
    f = []
    if len(text.strip()) < WENIG_TEXT:
        f.append("[wenig Text]")
    if FORMEL_ZEICHEN.search(text):
        f.append("[Zeichen prüfen]")
    if re.search(r"(?im)^\s*(endergebnis|lösung|ergebnisse?|antworten?)\b", text):
        f.append("[Endantworten-Abschnitt]")
    return " ".join(f)


def extract(quelle, ziel):
    ziel = Path(ziel)
    if (ziel / "Seitenindex.md").exists():
        sys.exit(f"{ziel}/Seitenindex.md existiert bereits. Neuen Ausgabeordner wählen; "
                 "Ergebnisse erst nach Vergleich übernehmen.")
    ziel.mkdir(parents=True, exist_ok=True)
    zeilen = ["# Seitenindex", "",
              "| Dokument | PDF-S. | Titel (erste Zeile) | Zeichen | Flags |",
              "| --- | ---: | --- | ---: | --- |"]
    manifest = {"version": 1, "dokumente": []}
    for pdf in pdfs(quelle):
        doc = pdfium.PdfDocument(str(pdf))
        md_name = pdf.stem + ".md"
        teile = [f"# {pdf.name}", ""]
        for n in range(1, len(doc) + 1):
            text = doc[n - 1].get_textpage().get_text_range().replace("\r", "")
            teile += [f"## PDF-Seite {n}", "", text.strip(), ""]
            zeilen.append(f"| [{pdf.name}]({md_name}#pdf-seite-{n}) | {n} | {titel(text)} "
                          f"| {len(text.strip())} | {flags(text)} |")
        (ziel / md_name).write_text("\n".join(teile), encoding="utf-8")
        manifest["dokumente"].append({"pdf": str(pdf.resolve()), "markdown": md_name,
                                      "seiten": len(doc), "sha256": sha256(pdf)})
        doc.close()
    (ziel / "Seitenindex.md").write_text("\n".join(zeilen) + "\n", encoding="utf-8")
    (ziel / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2),
                                        encoding="utf-8")
    fehler = check(ziel)
    print(f"{len(manifest['dokumente'])} PDF(s) → {ziel}" + ("" if not fehler else " (mit Fehlern)"))
    return fehler


def check(ziel):
    """Seitenzahl, Abschnittszahl und Hash gegen das Manifest prüfen; gibt Anzahl Probleme zurück."""
    ziel = Path(ziel)
    manifest = json.loads((ziel / "manifest.json").read_text(encoding="utf-8"))
    probleme = 0
    for d in manifest["dokumente"]:
        pdf, md = Path(d["pdf"]), ziel / d["markdown"]
        abschnitte = len(re.findall(r"(?m)^## PDF-Seite \d+$", md.read_text(encoding="utf-8")))
        if abschnitte != d["seiten"]:
            print(f"FEHLER {md.name}: {abschnitte} Abschnitte, {d['seiten']} Seiten"); probleme += 1
        if not pdf.exists():
            print(f"WARNUNG {pdf}: Original nicht gefunden"); probleme += 1
        elif sha256(pdf) != d["sha256"]:
            print(f"VERALTET {pdf.name}: PDF geändert, neu extrahieren"); probleme += 1
    if not probleme:
        print("OK: Index aktuell, Abschnittszahlen stimmen")
    return probleme


def render(pdf, seite, ziel, scale):
    ziel = Path(ziel); ziel.mkdir(parents=True, exist_ok=True)
    doc = pdfium.PdfDocument(str(pdf))
    if not 1 <= seite <= len(doc):
        sys.exit(f"Seite {seite} außerhalb 1–{len(doc)}")
    out = ziel / f"{Path(pdf).stem}-S{seite}.png"
    doc[seite - 1].render(scale=scale).to_pil().save(out)
    print(out)


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("extract"); e.add_argument("quelle"); e.add_argument("ziel")
    c = sub.add_parser("check"); c.add_argument("ziel")
    r = sub.add_parser("render"); r.add_argument("pdf"); r.add_argument("seite", type=int)
    r.add_argument("ziel"); r.add_argument("--scale", type=float, default=2)
    a = ap.parse_args()
    if a.cmd == "extract":
        sys.exit(1 if extract(a.quelle, a.ziel) else 0)
    if a.cmd == "check":
        sys.exit(1 if check(a.ziel) else 0)
    render(a.pdf, a.seite, a.ziel, a.scale)
