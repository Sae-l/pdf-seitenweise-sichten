#!/usr/bin/env python3
"""Prüft oder aktualisiert SHA256SUMS und ARCHIVE.json/skill_sha256.

  python scripts/pruefsummen.py          # prüfen (wie die CI)
  python scripts/pruefsummen.py --fix    # nach Änderungen an gelisteten Dateien neu schreiben

Neue Dateien zuerst von Hand als Zeile "<beliebig>  <pfad>" in SHA256SUMS eintragen, dann --fix.
"""
import argparse, hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SUMMEN, ARCHIV = ROOT / "SHA256SUMS", ROOT / "ARCHIVE.json"


def sha(pfad):
    return hashlib.sha256((ROOT / pfad).read_bytes()).hexdigest()


def main(fix):
    archiv_text = ARCHIV.read_text(encoding="utf-8")
    alt = json.loads(archiv_text)["skill_sha256"]
    if fix and alt != sha("SKILL.md"):
        # Nur den Hash ersetzen, damit Formatierung und Zeilenenden von ARCHIVE.json erhalten bleiben.
        ARCHIV.write_bytes(ARCHIV.read_bytes().replace(alt.encode(), sha("SKILL.md").encode()))
    zeilen, fehler = [], []
    for zeile in SUMMEN.read_text(encoding="utf-8").splitlines():
        erwartet, name = zeile.split("  ", 1)
        if erwartet != sha(name):
            fehler.append(name)
        zeilen.append(f"{sha(name)}  {name}")
    if json.loads(ARCHIV.read_text(encoding="utf-8"))["skill_sha256"] != sha("SKILL.md"):
        fehler.append("ARCHIVE.json: skill_sha256")
    if fix:
        SUMMEN.write_text("\n".join(zeilen) + "\n", encoding="utf-8", newline="\n")
        print(f"aktualisiert: {', '.join(fehler) or 'nichts'}")
    elif fehler:
        sys.exit("Prüfsumme abweichend: " + ", ".join(fehler) + "\nKorrektur: python scripts/pruefsummen.py --fix")
    else:
        print("Prüfsummen: PASS")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--fix", action="store_true")
    main(parser.parse_args().fix)
