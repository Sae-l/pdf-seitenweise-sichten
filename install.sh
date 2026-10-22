#!/usr/bin/env bash
# Verknüpft diesen Klon in die Skill-Ordner von Claude Code, VS Code/Copilot/Codex und Antigravity.
# Aktualisieren: im Klon `git pull` – alle Verknüpfungen zeigen auf denselben Stand.
set -euo pipefail
NAME=pdf-seitenweise-sichten
SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_HOME="${1:-$HOME}"
conflicts=0

for dir in "$SKILL_HOME/.claude/skills" "$SKILL_HOME/.agents/skills" "$SKILL_HOME/.gemini/config/skills" "$SKILL_HOME/.gemini/antigravity-cli/skills"; do
  mkdir -p "$dir"
  target="$dir/$NAME"
  if [ -L "$target" ] && [ "$(readlink "$target")" = "$SRC" ]; then
    echo "bereits verknüpft: $target"
    continue
  fi
  if [ -e "$target" ] || [ -L "$target" ]; then
    echo "Konflikt: $target bleibt unverändert; vorhandene Kopie oder fremde Verknüpfung zuerst prüfen" >&2
    conflicts=1
    continue
  fi
  ln -s "$SRC" "$target"
  echo "verknüpft: $target -> $SRC"
done

echo "Benötigt Python-Paket: python3 -m pip install -r \"$SRC/scripts/requirements.txt\""
exit "$conflicts"
