#!/usr/bin/env python3
"""Selbsttest für sichtung.py: python scripts/selbsttest.py (benötigt zusätzlich reportlab)."""
import subprocess, sys, tempfile
from pathlib import Path

from reportlab.pdfgen import canvas

SKRIPT = Path(__file__).with_name("sichtung.py")


def lauf(*args):
    return subprocess.run([sys.executable, str(SKRIPT), *map(str, args)], capture_output=True, text=True)


with tempfile.TemporaryDirectory() as tmp:
    tmp = Path(tmp)
    pdf = tmp / "quelle" / "Test.pdf"
    pdf.parent.mkdir()
    c = canvas.Canvas(str(pdf))
    c.drawString(72, 750, "Kapitel 1 Einführung in die Mechanik"); c.showPage()
    c.drawString(72, 750, "Formel: F = m · a, Einheit kg·m/s²"); c.drawString(72, 730, "Lösung: 12 N"); c.showPage()
    c.showPage()  # leere Seite ≈ Scan ohne Textschicht
    c.save()

    r = lauf("extract", pdf.parent, tmp / "out")
    assert r.returncode == 0, r.stdout + r.stderr
    index = (tmp / "out" / "Seitenindex.md").read_text(encoding="utf-8")
    zeilen = [z for z in index.splitlines() if z.startswith("| [Test.pdf]")]
    assert len(zeilen) == 3, index
    assert "Kapitel 1" in zeilen[0] and "[wenig Text]" not in zeilen[0]
    assert "[Zeichen prüfen]" in zeilen[1] and "[Endantworten-Abschnitt]" in zeilen[1]
    assert "[wenig Text]" in zeilen[2]

    assert lauf("extract", pdf.parent, tmp / "out").returncode != 0, "bestehender Index wurde nicht geschützt"
    assert lauf("check", tmp / "out").returncode == 0

    pdf.write_bytes(pdf.read_bytes() + b"\n%geaendert\n")
    r = lauf("check", tmp / "out")
    assert r.returncode != 0 and "VERALTET" in r.stdout, r.stdout

    r = lauf("render", pdf, 2, tmp / "bilder")
    assert r.returncode == 0 and (tmp / "bilder" / "Test-S2.png").exists(), r.stderr
    assert lauf("render", pdf, 9, tmp / "bilder").returncode != 0

print("Selbsttest bestanden")
