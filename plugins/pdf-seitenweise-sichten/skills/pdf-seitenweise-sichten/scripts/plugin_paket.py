#!/usr/bin/env python3
"""Erzeugt das Plugin-Paket für Claude Code und Codex/ChatGPT aus den Quelldateien im Repository.

  python scripts/plugin_paket.py           # plugins/pdf-seitenweise-sichten/ neu erzeugen
  python scripts/plugin_paket.py --check   # nur prüfen, ob das eingecheckte Paket aktuell ist

Das Paket ist eine erzeugte Kopie: nur an der Quelle (SKILL.md, scripts/, references/) ändern.
"""
import argparse, filecmp, json, shutil, sys, tempfile
from pathlib import Path

from install_projekt import NAME, ROOT, kopiere_skill

ZIEL = ROOT / "plugins" / NAME
BESCHREIBUNG = ("Token-sparing page-by-page review of local PDFs (lecture slides, exercise sheets, formula collections): "
                "page index, per-page Markdown, targeted original-page rendering. "
                "PDF-Unterlagen tokensparsam seitenweise sichten.")


def bauen(ziel):
    archiv = json.loads((ROOT / "ARCHIVE.json").read_text(encoding="utf-8"))
    kopiere_skill(ziel / "skills" / NAME)
    gemeinsam = dict(name=NAME, version=archiv["version"], description=BESCHREIBUNG,
                     author=dict(name=archiv["owner"]), homepage=f"https://github.com/Sae-l/{NAME}",
                     repository=f"https://github.com/Sae-l/{NAME}", license="MIT",
                     keywords=["pdf", "lecture-notes", "study", "markdown", "token-efficient"])
    schreibe(ziel / ".claude-plugin" / "plugin.json", gemeinsam)
    schreibe(ziel / "plugin.json", {"$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json", **gemeinsam})


def schreibe(pfad, daten):
    pfad.parent.mkdir(parents=True, exist_ok=True)
    pfad.write_text(json.dumps(daten, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def abweichungen(a, b):
    vergleich = filecmp.dircmp(a, b, ignore=["__pycache__"])
    fehler = [f"{a / n}" for n in vergleich.left_only] + [f"{b / n}" for n in vergleich.right_only]
    fehler += [f"{a / n}" for n in vergleich.common_files if not filecmp.cmp(a / n, b / n, shallow=False)]
    for unter in vergleich.common_dirs:
        fehler += abweichungen(a / unter, b / unter)
    return fehler


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            soll = Path(tmp) / NAME
            bauen(soll)
            fehler = abweichungen(soll, ZIEL) if ZIEL.is_dir() else [f"fehlt: {ZIEL}"]
        if fehler:
            sys.exit("Plugin-Paket veraltet; `python scripts/plugin_paket.py` ausführen:\n" + "\n".join(fehler))
        print("Plugin-Paket: aktuell")
    else:
        if ZIEL.exists():
            shutil.rmtree(ZIEL)  # erzeugte Kopie; Quelle bleibt unberührt
        bauen(ZIEL)
        print(f"erzeugt: {ZIEL.relative_to(ROOT)}")
