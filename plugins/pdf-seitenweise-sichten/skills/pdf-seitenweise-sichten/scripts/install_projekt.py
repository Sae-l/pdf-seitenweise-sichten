#!/usr/bin/env python3
"""Installiert portable Skill-Kopien für lokale Agenten und GitHub Copilot.

  python scripts/install_projekt.py <vorhandener-projektordner>

Erzeugt .agents/skills/pdf-seitenweise-sichten und .claude/skills/pdf-seitenweise-sichten.
Bestehende Ziele bleiben unverändert. Original-PDFs werden nicht kopiert.
"""
import argparse
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
NAME = "pdf-seitenweise-sichten"


def install(project):
    project = Path(project).resolve()
    if not project.is_dir():
        raise ValueError(f"Projektordner fehlt: {project}")
    targets = [project / folder / "skills" / NAME for folder in (".agents", ".claude")]
    for target in targets:
        if not target.resolve().is_relative_to(project):
            raise ValueError(f"Skill-Ziel verweist aus dem Projekt heraus: {target}")
        if target.exists() or target.is_symlink() or target.is_junction():
            raise FileExistsError(f"Ziel bleibt unverändert: {target}. Für ein Update erst vergleichen und sichern.")
    for target in targets:
        kopiere_skill(target)
        print(f"installiert: {target}")


def kopiere_skill(target):
    """Vollständige Skill-Kopie; auch Quelle des Plugin-Pakets (plugin_paket.py)."""
    target.mkdir(parents=True)
    for name in ("SKILL.md", "LICENSE", "ARCHIVE.json"):
        shutil.copy2(ROOT / name, target / name)
    dateien = git_dateien("scripts", "references")
    if dateien is None:
        for name in ("scripts", "references"):
            shutil.copytree(ROOT / name, target / name, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
        return
    for name in dateien:
        (target / name).parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / name, target / name)


def git_dateien(*ordner):
    """Dateien ohne .gitignore-Treffer (z. B. lokale Kursunterlagen in references/); None außerhalb eines Git-Repos."""
    # shortcut: ohne Git (ZIP-Download) wird alles kopiert; dann references/ vorher frei von eigenen Dateien halten.
    try:
        result = subprocess.run(["git", "-C", str(ROOT), "ls-files", "-z", "--cached", "--others",
                                 "--exclude-standard", "--", *ordner], capture_output=True, check=True)
    except (OSError, subprocess.CalledProcessError):
        return None
    namen = [name for name in result.stdout.decode("utf-8").split("\0") if name]
    return [name for name in namen if (ROOT / name).is_file() and "__pycache__" not in name and not name.endswith(".pyc")]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("projekt", type=Path)
    args = parser.parse_args()
    try:
        install(args.projekt)
    except (OSError, ValueError) as error:
        parser.exit(1, f"FEHLER: {error}\n")
