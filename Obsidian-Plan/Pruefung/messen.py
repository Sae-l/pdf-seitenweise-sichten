"""Reproduziert die Messungen aus der Notiz „20 Ist-Stand und Messung“.

  python messen.py <pfad-zum-CuD-klon>

Vergleicht den alten Index in CuD/Referenz_Sichtung mit einer frischen
Extraktion durch scripts/sichtung.py. Schreibt nur in ein Temp-Verzeichnis.
"""
import collections, hashlib, json, re, subprocess, sys, tempfile
from pathlib import Path

SKILL = Path(__file__).resolve().parents[2]


def seiten_aus_index(text):
    # alter Index: "- S. N: …"; neuer Index: Tabellenzeilen "| [doc](…) | N | …"
    return len(re.findall(r"(?m)^- S\. \d+:", text)) or len(re.findall(r"(?m)^\| \[", text))


def main(cud):
    cud = Path(cud)
    alt_dateien = [p for p in (cud / "Referenz_Sichtung").rglob("Seitenindex.md") if p.parent.name != "Referenz_Sichtung"]
    alt_zeichen = sum(len(p.read_text(encoding="utf-8")) for p in alt_dateien)
    alt_seiten = sum(seiten_aus_index(p.read_text(encoding="utf-8")) for p in alt_dateien)
    alt_titel = re.findall(r"(?m)^- S\. \d+: (.*?)(?: \[|$)", "\n".join(p.read_text(encoding="utf-8") for p in alt_dateien))

    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run([sys.executable, str(SKILL / "scripts/sichtung.py"), "extract", str(cud / "Referenz"), tmp],
                       check=True, capture_output=True)
        neu = (Path(tmp) / "Seitenindex.md").read_text(encoding="utf-8")
        neu_titel = [z.split(" | ")[2] for z in neu.splitlines() if z.startswith("| [")]
        wiederholt = {}
        for md in Path(tmp).glob("*.md"):
            if md.name == "Seitenindex.md":
                continue
            seiten = re.split(r"(?m)^## PDF-Seite \d+$", md.read_text(encoding="utf-8"))[1:]
            zaehl = collections.Counter(l.strip() for s in seiten for l in set(s.splitlines()) if l.strip())
            gesamt = sum(len(s) for s in seiten) or 1
            rep = sum(len(l) * c for l, c in zaehl.items() if c >= max(3, len(seiten) / 2))
            wiederholt[md.stem] = round(100 * rep / gesamt)

    hashes = collections.Counter(hashlib.sha256(p.read_bytes()).hexdigest() for p in (cud / "Referenz").rglob("*.pdf"))
    leer = lambda ts: sum(bool(re.fullmatch(r"Seite \d+", t.strip())) for t in ts)
    ergebnis = {
        "alt": {"seiten": alt_seiten, "zeichen_pro_seite": round(alt_zeichen / alt_seiten),
                "titel_nur_seitennummer": leer(alt_titel)},
        "neu_v1_2_0": {"seiten": len(neu_titel), "zeichen_pro_seite": round(len(neu) / len(neu_titel)),
                       "titel_nur_seitennummer": leer(neu_titel)},
        "kopf_fusszeilen_anteil_prozent": wiederholt,
        "byte_identische_pdf_duplikate": sum(c - 1 for c in hashes.values()),
    }
    print(json.dumps(ergebnis, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
