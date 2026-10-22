#!/usr/bin/env bash
# Verknüpft diesen Klon in die Skill-Ordner von Claude Code, VS Code/Copilot/Codex und Antigravity.
# Aktualisieren: im Klon `git pull` – alle Verknüpfungen zeigen auf denselben Stand.
set -euo pipefail
NAME=pdf-seitenweise-sichten
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

for dir in "$HOME/.claude/skills" "$HOME/.agents/skills" "$HOME/.gemini/config/skills"; do
  mkdir -p "$dir"
  target="$dir/$NAME"
  if [ -e "$target" ] && [ ! -L "$target" ]; then
    echo "übersprungen: $target ist eine echte Kopie, keine Verknüpfung – erst sichern und entfernen"
    continue
  fi
  ln -sfn "$SRC" "$target"
  echo "verknüpft: $target -> $SRC"
done

echo "Benötigt Python-Paket: python3 -m pip install -r \"$SRC/scripts/requirements.txt\""
