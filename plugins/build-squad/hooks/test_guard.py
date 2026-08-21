#!/usr/bin/env python3
"""Behavior contract for the Codex Build Squad guard."""
import json
import os
import subprocess
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from guard import evaluate  # noqa: E402


class GuardContract(unittest.TestCase):
    def test_denies_cluster_and_destructive_git_commands(self):
        for command in [
            "kubectl get pods", "sudo kubectl delete ns prod", "result=$(kubectl get pods)",
            "git reset --hard", "git clean -fdx", "git checkout -- src/app.py",
            "git restore src/app.py", "git stash drop", "git push --force origin main",
        ]:
            self.assertIsNotNone(evaluate("Bash", {"command": command}), command)

    def test_allows_safe_commands(self):
        for command in [
            "git status", "git checkout main", "git reset --soft HEAD~1", "git clean -n",
            "git restore --staged file.py", "git push --force-with-lease origin main",
            'git commit -m "run kubectl to check"', "cat kubectl.log",
        ]:
            self.assertIsNone(evaluate("Bash", {"command": command}), command)

    def test_emits_a_valid_codex_deny_response(self):
        guard = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guard.py")
        result = subprocess.run(
            [sys.executable, guard], input=json.dumps({"tool_name": "Bash", "tool_input": {"command": "git reset --hard"}}),
            capture_output=True, text=True, check=True,
        )
        output = json.loads(result.stdout)
        self.assertEqual(output["decision"], "block")
        self.assertEqual(output["hookSpecificOutput"]["permissionDecision"], "deny")


if __name__ == "__main__":
    unittest.main(verbosity=2)
