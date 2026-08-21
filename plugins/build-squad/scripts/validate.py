#!/usr/bin/env python3
"""Portable structural validation for the Build Squad Codex plugin."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []


def fail(message):
    errors.append(message)


try:
    manifest = json.loads((ROOT / ".codex-plugin" / "plugin.json").read_text())
except Exception as exc:  # noqa: BLE001
    fail(f"Invalid plugin manifest: {exc}")
    manifest = {}

for key in ("name", "version", "description", "author", "interface"):
    if not manifest.get(key):
        fail(f"plugin.json missing {key}")
if not re.fullmatch(r"\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?", manifest.get("version", "")):
    fail("plugin.json version is not semver")
for name in ("displayName", "shortDescription", "longDescription", "developerName", "category", "capabilities", "defaultPrompt"):
    if name not in manifest.get("interface", {}):
        fail(f"plugin.json interface missing {name}")

for folder in ("skills", "agents", "hooks", "scripts"):
    if not (ROOT / folder).is_dir():
        fail(f"missing {folder}/")
for skill in sorted((ROOT / "skills").glob("*/SKILL.md")):
    text = skill.read_text()
    match = re.match(r"^---\nname:\s*([^\n]+)\ndescription:\s*(.+)\n---\n", text, re.DOTALL)
    if not match:
        fail(f"{skill.relative_to(ROOT)} has invalid frontmatter")
    elif match.group(1).strip() != skill.parent.name:
        fail(f"{skill.relative_to(ROOT)} name does not match its directory")
if len(list((ROOT / "skills").glob("*/SKILL.md"))) != 8:
    fail("expected eight skills")
if len(list((ROOT / "agents").glob("build-squad-*.toml"))) != 5:
    fail("expected five agent definitions")
if not (ROOT / "hooks" / "hooks.json").is_file() or not (ROOT / "hooks" / "guard.py").is_file():
    fail("missing hook configuration or guard")

if errors:
    print("Build Squad Codex plugin validation FAILED:")
    print("\n".join(f"- {error}" for error in errors))
    sys.exit(1)
print("Build Squad Codex plugin validation OK")
