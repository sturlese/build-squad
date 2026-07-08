#!/usr/bin/env python3
"""claude-squad security guard (PreToolUse hook).

Mechanical enforcement of the plugin's security policy:

  - no kubectl / direct cluster access
  - no reading or writing .env files (except .env.example/.sample/.template/.test)
  - no `git reset --hard`

Exit code 2 blocks the tool call; stderr is fed back to the model.
Everything else exits 0 (allow). Stdlib only.
"""
import json
import re
import sys


def deny(reason: str) -> None:
    print(f"Blocked by claude-squad security policy: {reason}", file=sys.stderr)
    sys.exit(2)


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)  # unparseable input: never break the session over the guard

    tool = data.get("tool_name", "") or ""
    tool_input = data.get("tool_input") or {}

    env_ok = re.compile(r"\.env\.(example|sample|template|test)$", re.IGNORECASE)
    # basename starts with ".env", optionally followed by ".something"
    env_re = re.compile(r"(^|[\\/])\.env(\.[\w.-]+)?$", re.IGNORECASE)

    def is_protected_env(path: str) -> bool:
        return bool(path) and bool(env_re.search(path)) and not env_ok.search(path)

    if tool == "Bash":
        cmd = tool_input.get("command", "") or ""
        if re.search(r"(^|[\s;&|(`])kubectl\b", cmd):
            deny("kubectl / direct cluster access is forbidden.")
        if re.search(r"\bgit\s+(?:-\S+\s+)*reset\s+(?:-\S+\s+)*--hard\b", cmd):
            deny("`git reset --hard` is forbidden.")
        for match in re.finditer(r"[^\s'\"();|&<>]*\.env[^\s'\"();|&<>]*", cmd):
            token = match.group(0)
            if is_protected_env(token):
                deny(
                    f"the command references {token} — .env files are managed "
                    "by the human, never by agents."
                )
    elif tool in ("Read", "Edit", "Write", "MultiEdit", "NotebookEdit"):
        path = (
            tool_input.get("file_path")
            or tool_input.get("notebook_path")
            or tool_input.get("path")
            or ""
        )
        if is_protected_env(path):
            deny(
                f"access to {path} is forbidden — .env files are managed "
                "by the human, never by agents."
            )

    sys.exit(0)


if __name__ == "__main__":
    main()
