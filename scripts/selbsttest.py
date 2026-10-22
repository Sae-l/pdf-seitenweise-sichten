#!/usr/bin/env python3
"""Selbsttest für sichtung.py: python scripts/selbsttest.py (benötigt zusätzlich reportlab)."""
import json, shutil, subprocess, sys, tempfile
from pathlib import Path

from reportlab.pdfgen import canvas

SKRIPT = Path(__file__).with_name("sichtung.py")


def lauf(*args):
    return subprocess.run([sys.executable, str(SKRIPT), *map(str, args)], capture_output=True, text=True)


with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    quelle = tmp / "quelle"
    quelle.mkdir()
    assert lauf("extract", quelle, tmp / "leer").returncode != 0
    assert not (tmp / "leer").exists(), "leere Quelle erzeugt einen scheinbar gültigen Index"
    assert lauf("extract", tmp / "fehlt", tmp / "leer").returncode != 0
    pdf = quelle / "Test.pdf"
    c = canvas.Canvas(str(pdf))
    for kopf, zeilen in [("Kapitel 1 Einführung in die Mechanik", ["Grundbegriffe der Kinematik"]),
                         ("Formeln", ["F = m · a, Einheit kg·m/s²", "Aufgabe 1: Kraft berechnen"]),
                         ("Endantworten:", ["12 N"]), (None, [])]:
        c.drawString(72, 800, "Mechanik Skript WS")  # Kopfzeile auf jeder Seite
        c.drawString(72, 40, "Seite 1")
        if kopf:
            c.drawString(72, 750, kopf)
            for i, z in enumerate(zeilen):
                c.drawString(72, 730 - 20 * i, z)
        c.showPage()
    c.save()
    shutil.copy(pdf, quelle / "Kopie.pdf")  # byte-identisches Duplikat

    r = lauf("extract", quelle, tmp / "out")
    assert r.returncode == 0, r.stdout + r.stderr
    index = (tmp / "out" / "Seitenindex.md").read_text(encoding="utf-8")
    zeilen = [z for z in index.splitlines() if z.startswith("- S.")]
    assert len(zeilen) == 4, index                                    # Duplikat nicht doppelt indiziert
    assert "Byte-identisch mit Kopie.pdf" in index or "Byte-identisch mit Test.pdf" in index
    assert "Mechanik Skript WS" not in index and "Seite 1" not in "".join(zeilen), index  # Kopfzeile kein Titel
    assert zeilen[0].startswith("- S. 1: Kapitel 1 Einführung")
    assert "Aufgabe/Beispiel" in zeilen[1] and "Aufgabe/Beispiel" not in zeilen[0]
    assert "Endantworten-Abschnitt" in zeilen[2] and "Endantworten-Abschnitt" not in zeilen[1]
    assert "wenig Text" in zeilen[3]  # Testseiten sind alle kurz; leere Seite muss es sicher sein
    manifest = json.loads((tmp / "out" / "manifest.json").read_text(encoding="utf-8"))
    seiten = next(d for d in manifest if "page_index" in d)["page_index"]
    assert seiten[0]["text_read"] is False and seiten[0]["subject_review"] == "offen"
    assert seiten[3]["image"] and (tmp / "out" / seiten[3]["image"]).exists()

    assert lauf("extract", quelle, tmp / "out").returncode != 0, "bestehender Index wurde nicht geschützt"
    assert lauf("check", tmp / "out").returncode == 0

    shutil.copy(pdf, quelle / "Neu.pdf")
    r = lauf("check", tmp / "out")
    assert r.returncode != 0 and "Neu.pdf" in r.stdout, r.stdout
    (quelle / "Neu.pdf").unlink()

    md = tmp / "out" / next(d for d in manifest if "markdown" in d)["markdown"]
    original = md.read_text(encoding="utf-8")
    md.write_text(original.replace("## PDF-Seite 2", "## PDF-Seite 1"), encoding="utf-8")
    assert lauf("check", tmp / "out").returncode != 0, "doppelte Seitennummer übersehen"
    md.unlink()
    assert lauf("check", tmp / "out").returncode != 0, "fehlendes Markdown übersehen"
    md.write_text(original, encoding="utf-8")

    geschützt = tmp / "geschuetzt"
    geschützt.mkdir()
    (geschützt / "manifest.json").write_text("[]", encoding="utf-8")
    assert lauf("extract", quelle, geschützt).returncode != 0
    assert (geschützt / "manifest.json").read_text(encoding="utf-8") == "[]"
    assert lauf("check", geschützt).returncode != 0

    # Prüfstatus und handgerenderte Bilder werden mit --alt übernommen
    seiten[1].update(text_read=True, original_image_viewed=True, image="bilder/hand-S002.png")
    (tmp / "out" / "bilder" / "hand-S002.png").write_bytes(b"png")
    (tmp / "out" / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
    r = lauf("extract", quelle, tmp / "neu", "--alt", tmp / "out")
    assert r.returncode == 0 and "Prüfstände übernommen" in r.stdout, r.stdout + r.stderr
    neu = next(d for d in json.loads((tmp / "neu" / "manifest.json").read_text(encoding="utf-8")) if "page_index" in d)
    assert neu["page_index"][1]["text_read"] is True and neu["page_index"][1]["original_image_viewed"] is True
    assert (tmp / "neu" / "bilder" / "hand-S002.png").read_bytes() == b"png"

    # Ohne alte Prüfsumme gibt es keinen Beleg für unveränderte Quellen.
    ohne_hash = json.loads((tmp / "out" / "manifest.json").read_text(encoding="utf-8"))
    for d in ohne_hash:
        d.pop("sha256", None)
    (tmp / "out" / "manifest.json").write_text(json.dumps(ohne_hash), encoding="utf-8")
    assert lauf("check", tmp / "out").returncode != 0
    r = lauf("extract", quelle, tmp / "ohne_hash", "--alt", tmp / "out")
    assert r.returncode == 0, r.stdout + r.stderr
    ohne = next(d for d in json.loads((tmp / "ohne_hash" / "manifest.json").read_text(encoding="utf-8")) if "page_index" in d)
    assert ohne["page_index"][1]["text_read"] is False
    assert ohne["page_index"][1]["original_image_viewed"] is False
    assert not (tmp / "ohne_hash" / "bilder" / "hand-S002.png").exists()

    # Geändertes PDF: check meldet VERALTET, alter Prüfstatus wird nicht übernommen
    pdf.write_bytes(pdf.read_bytes() + b"\n%geaendert\n")
    r = lauf("check", tmp / "neu")
    assert r.returncode != 0 and "VERALTET" in r.stdout, r.stdout
    lauf("extract", quelle, tmp / "neu2", "--alt", tmp / "neu")
    neu2 = json.loads((tmp / "neu2" / "manifest.json").read_text(encoding="utf-8"))
    test = next(d for d in neu2 if d["pdf"] == "Test.pdf")
    assert test["page_index"][1]["text_read"] is False, "Status eines geänderten PDFs wurde übernommen"

    r = lauf("render", pdf, 2, tmp / "bilder")
    assert r.returncode == 0 and (tmp / "bilder" / "Test-S002.png").exists(), r.stderr
    assert lauf("render", pdf, 9, tmp / "bilder").returncode != 0

    pdf.unlink()
    assert lauf("check", tmp / "neu2").returncode != 0, "entfernte PDF übersehen"

print("Selbsttest bestanden")
