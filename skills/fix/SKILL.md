---
name: fix
description: Bug-fix pipeline — the tester reproduces the bug and captures it as a failing test BEFORE the developer may touch production code, then verifies the fix and scans for sibling occurrences of the same defect. Use when the user reports a bug, regression, or broken behavior and wants the team to fix it.
---

# Team fix

Bug: $ARGUMENTS

You are the orchestrator. This pipeline exists because of one principle: **a bug that is not reproduced is a rumor, and a fix without a failing test is a cover-up.** No production code changes until a red test exists.

## Choreography

0. **Context.** Read `CLAUDE.md` and `README.md` if present; if the project documents a system-overview command (e.g. a `make info` target), run it. Pass the relevant slice to every agent you spawn.
1. **Reproduce — `tester` leads.** Spawn the tester with the bug report and context. Its mission: reproduce the bug and capture it as the smallest failing automated test (or, when automation is genuinely impossible, a precise manual reproduction procedure — flagged as such). It also diagnoses the affected contract: is this actually a bug (behavior diverges from the contract) or a contract-change request in disguise?
2. **GATE — human confirms.** Present: reproduction evidence, the failing test (path and name), the affected contract, and the tester's diagnosis. Three exits:
   - Confirmed bug → continue.
   - Intended behavior / feature request in disguise → stop and offer `/squad:define` to spec it (it closes quickly for small scopes) followed by `/squad:build`.
   - Could not reproduce → stop; report what was tried and exactly what information is missing.
3. **Fix — `developer`.** Spawn the developer with the failing test reference, the tester's diagnosis, and a minimal-fix mandate: make the failing test pass WITHOUT weakening it, touching as little as possible. The developer must not modify the new test (the tester owns it) — if the test itself seems wrong, it reports that instead of editing it. No opportunistic refactors: improvement ideas go in the report as follow-ups.
4. **Verify — `tester` (∥ `auditor` when sensitive).** Tester re-runs the new test (must be green) plus the smallest regression set around the touched area, sequentially by default. Spawn the auditor in parallel ONLY if the diff touches sensitive territory (auth, data integrity, money, concurrency, security) — otherwise skip it and say so in the report.
5. **Sibling scan.** Have the developer (or the auditor, if spawned) scan for the same defect elsewhere: the same helper misused in other call sites, a symmetric flow (create vs update) sharing the broken pattern, copy-pasted logic. Siblings are reported as follow-ups — never fixed silently in this run.
6. **Delivery report.** Root cause in one paragraph; the failing-test-now-green proof; files changed; regression targets run and results; sibling occurrences found; follow-ups.

## Rules

- Production code is untouchable until the failing test exists — this ordering is the entire point of the pipeline.
- Minimal fix only; refactors ride in follow-ups, not in bug fixes.
- Test runs are sequential unless the project explicitly documents its suites as parallel-safe.
- If reproduction is manual-only, the gate must say so explicitly and the human decides whether to proceed without an automated guard.
- If the bug arrived as an informal description or screenshot and the user is available to answer questions, `/squad:bug` may fit better: it clarifies interactively in the main session and hands the developer a closed brief, with the regression test written after the fix.
