#!/usr/bin/env python3
"""Install Build Squad's optional Codex agent definitions into ~/.codex/agents."""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path


PLUGIN_ROOT = Path(__file__).resolve().parents[1]
SOURCE = PLUGIN_ROOT / "agents"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--destination", type=Path, default=Path.home() / ".codex" / "agents")
    args = parser.parse_args()
    args.destination.mkdir(parents=True, exist_ok=True)
    for source in sorted(SOURCE.glob("build-squad-*.toml")):
        target = args.destination / source.name
        shutil.copy2(source, target)
        print(f"Installed {target}")


if __name__ == "__main__":
    main()
