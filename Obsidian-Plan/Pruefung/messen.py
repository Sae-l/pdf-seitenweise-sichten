"""Reproduziert die Messungen aus der Notiz „20 Ist-Stand und Messung“.

  python messen.py <pfad-zum-CuD-klon>

Vergleicht den alten Index in CuD/Referenz_Sichtung (alter Projekt-Helfer) mit
einer frischen Extraktion durch scripts/sichtung.py, je Unterordner von
CuD/Referenz, inklusive Übernahme des Prüfstatus. Schreibt nur in ein Temp-Verzeichnis.
"""
import json, re, subprocess, sys, tempfile
from pathlib import Path

SKILL = Path(__file__).resolve().parents[2]


def kennzahlen(ordner):
    # nur Gruppenindizes (Manifest als Liste); der Sammelindex mit Dict-Manifest würde doppelt zählen
    indizes = [p for p in Path(ordner).rglob("Seitenindex.md") if (p.parent / "manifest.json").exists()
               and isinstance(json.loads((p.parent / "manifest.json").read_text(encoding="utf-8")), list)]
    text = "".join(p.read_text(encoding="utf-8") for p in indizes)
    titel = re.findall(r"(?m)^- S\. \d+: (.*?)(?: \[|$)", text)
    status = 0
    for p in indizes:
        for doc in json.loads((p.parent / "manifest.json").read_text(encoding="utf-8")):
            status += sum(s.get("text_read", False) + s.get("original_image_viewed", False) for s in doc.get("page_index", []))
    return {"indizierte_seiten": len(titel), "zeichen_pro_seite": round(len(text) / len(titel)),
            "titel_nur_seitennummer": sum(bool(re.fullmatch(r"Seite \d+", t.strip())) for t in titel),
            "pruefmarken": status}


def main(cud):
    cud = Path(cud)
    with tempfile.TemporaryDirectory() as tmp:
        for quelle in sorted(p for p in (cud / "Referenz").iterdir() if p.is_dir() and any(p.glob("*.pdf"))):
            # Ordnernamen wie im alten Index: "Pflicht Übungen" -> "Pflicht_Uebungen"
            name = quelle.name.replace(" ", "_").replace("Ü", "Ue").replace("ü", "ue")
            subprocess.run([sys.executable, str(SKILL / "scripts/sichtung.py"), "extract", str(quelle),
                            str(Path(tmp) / name), "--alt", str(cud / "Referenz_Sichtung" / name)],
                           check=True, capture_output=True)
        print(json.dumps({"alt": kennzahlen(cud / "Referenz_Sichtung"), "sichtung_py": kennzahlen(tmp)},
                         ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
