#!/usr/bin/env python3
"""Build Squad's Codex PreToolUse guard (stdlib only)."""
import json
import re
import shlex
import sys

SEGMENT = re.compile(r"\$\(|\)|`|&&|\|\||[;\n|&<>]")
WRAPPERS = {"sudo", "doas", "env", "command", "nice", "time", "nohup", "xargs", "exec"}
GIT_VALUE_OPTIONS = {"-C", "-c", "--git-dir", "--work-tree", "--namespace", "--exec-path"}


def tokens(segment):
    try:
        return shlex.split(segment)
    except ValueError:
        return segment.split()


def segments(command):
    return [part for part in SEGMENT.sub("\0", command).split("\0") if part.strip()]


def git_args(parts):
    index = 0
    while index < len(parts) and (re.match(r"^[A-Za-z_]\w*=", parts[index]) or parts[index] in WRAPPERS):
        index += 1
    if index < len(parts) and parts[index].rsplit("/", 1)[-1] == "git":
        return parts[index + 1 :]
    return None


def subcommand(arguments):
    index = 0
    while index < len(arguments):
        argument = arguments[index]
        if not argument.startswith("-"):
            return argument, arguments[index + 1 :]
        index += 2 if argument in GIT_VALUE_OPTIONS else 1
    return None, []


def short_flag(arguments, letter):
    return any(re.fullmatch(r"-[A-Za-z]*" + re.escape(letter) + r"[A-Za-z]*", arg) for arg in arguments)


def destructive_git(arguments):
    command, rest = subcommand(arguments)
    if command == "reset" and "--hard" in rest:
        return "`git reset --hard` discards uncommitted work."
    if command == "clean" and ("--force" in rest or short_flag(rest, "f")) and not ("--dry-run" in rest or short_flag(rest, "n")):
        return "`git clean -f` deletes untracked files."
    if command == "checkout" and ("--" in rest or "--force" in rest or short_flag(rest, "f") or "." in rest):
        return "This `git checkout` discards working-tree changes."
    if command == "restore" and ("--worktree" in rest or short_flag(rest, "W") or "--staged" not in rest):
        return "This `git restore` discards working-tree changes."
    if command == "stash" and rest[:1] in (["clear"], ["drop"]):
        return "`git stash clear/drop` destroys stashed work."
    if command == "push" and ("--force" in rest or short_flag(rest, "f")) and not any(arg.startswith("--force-with-lease") or arg.startswith("--force-if-includes") for arg in rest):
        return "`git push --force` rewrites shared history; use --force-with-lease when justified."
    return None


def evaluate(tool_name, tool_input):
    if tool_name != "Bash":
        return None
    command = (tool_input or {}).get("command", "") or ""
    for segment in segments(command):
        parts = tokens(segment)
        if any(token.rsplit("/", 1)[-1] == "kubectl" for token in parts):
            return "kubectl / direct cluster access is forbidden."
        arguments = git_args(parts)
        if arguments is not None:
            reason = destructive_git(arguments)
            if reason:
                return reason
    return None


def main():
    try:
        event = json.load(sys.stdin)
    except Exception:
        return
    reason = evaluate(event.get("tool_name", ""), event.get("tool_input", {}))
    if reason:
        message = "Blocked by Build Squad security policy: " + reason
        print(json.dumps({
            "decision": "block",
            "reason": message,
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": message,
            },
        }))


if __name__ == "__main__":
    main()
