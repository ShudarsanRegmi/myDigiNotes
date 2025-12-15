#!/usr/bin/env python3

import os
import stat
from pathlib import Path
from textwrap import dedent

# -----------------------------
# CONFIG
# -----------------------------

BIN_DIR = Path.home() / ".local" / "bin"

# Each key becomes an executable name
# Each value is the command that will run
ALIASES = {
    "ocr": "flatpak run com.github.dynobo.normcap",
    "sysinfo": "neofetch",
    "projv": "xdg-open obsidian://vault/ProjectsAndResearch",
    "lifev" : "xdg-open obsidian://vault/LifeLongLearning",
    "semv" : "xdg-open obsidian://vault/Sem6vault",
    "cybov" : "xdg-open obsidian://vault/CyboSec",
    "placev" : "xdg-open obsidian://vault/Placement",
    "tt" : "xdg-open $HOME/Desktop/ObsidianVaults/Sem6vault/SemAssets/tt-v1.pdf",
    "cal" : "xdg-open $HOME/Desktop/ObsidianVaults/Sem6vault/SemAssets/cal-v1.pdf"

}

# More complex scripts
SCRIPTS = {
    "todo": r'''
    FILE="$HOME/Desktop/ObsidianVaults/Sem6vault/Tracking/TODOS.md"

    if [ -z "$1" ]; then
        echo "Usage: todo \"task description\""
        exit 1
    fi

    TASK="$*"
    TIMESTAMP="$(date '+%Y-%m-%d %H:%M')"
    LINE="- [ ] ${TASK} - (${TIMESTAMP})"

    TMP_FILE="$(mktemp)"
    printf "%s\n" "$LINE" > "$TMP_FILE"
    cat "$FILE" >> "$TMP_FILE"
    mv "$TMP_FILE" "$FILE"
'''
}

# -----------------------------
# GENERATOR
# -----------------------------

WRAPPER_TEMPLATE = """\
#!/usr/bin/env bash
set -e

{body}
"""

def ensure_bin_dir():
    BIN_DIR.mkdir(parents=True, exist_ok=True)

def write_executable(name: str, body: str):
    path = BIN_DIR / name

    script = WRAPPER_TEMPLATE.format(body=body.strip())
    path.write_text(dedent(script))

    # Make executable
    path.chmod(path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    print(f"generated: {path}")

def main():
    ensure_bin_dir()

    for name, cmd in ALIASES.items():
        write_executable(name, cmd)

    for name, script in SCRIPTS.items():
        write_executable(name, script)

if __name__ == "__main__":
    main()

