---
name: bug
description: Interactive bug intake and fix — the user reports a bug in a few sentences or a screenshot, the session investigates the code first, asks only the questions that block the fix, and once the brief is confirmed runs developer (minimal fix) → tester (regression test + smallest regression set) → documentator (if docs affected). Use when the user reports a bug informally and is available to answer questions; for strict reproduce-first discipline with a failing test as the gate, use /squad:fix.
---

# Squad bug

Bug report: $ARGUMENTS (plus any screenshots pasted in the conversation)

You are the orchestrator, and the intake happens HERE, in the main session — for two reasons: clarification is a conversation (a subagent relay would be slow and lossy), and subagents never see the conversation's images, so a screenshot's facts must be extracted by you into text before any agent can act on them.

## Choreography

1. **Ingest.** Extract every fact from the report and screenshots: literal error messages, UI state, visible data, environment hints. Read the project's context sources (`CLAUDE.md`, `README.md`, overview command if documented).
2. **Investigate before asking.** Locate the affected area in the code and form a hypothesis. Never ask the user something the code, the logs, or the screenshot already answer.
3. **Clarify — small rounds.** Ask ONLY what still blocks the fix, 2–3 questions per round, each with your best-guess answer attached so the user can confirm or correct: expected vs actual behavior, exact reproduction path, since when (regression vs never-worked), environment or data specifics. Stop as soon as the brief closes — do not interrogate past usefulness.
4. **The brief.** Closed when it has: expected behavior (the contract), actual behavior, reproduction path (manual is fine — the user is the reproduction oracle here), suspected area, and a "fixed when …" acceptance line. Show it compactly for one confirmation — a nod, not a negotiation. If the user prefers to fix later, save the brief to `specs/bugs/<slug>.md` and stop; this skill resumes from that file.
5. **Fix — `developer`.** Spawn with the brief verbatim and a minimal-fix mandate. It returns: root cause, files changed, how to verify manually, and any sibling occurrences of the same defect it noticed (reported as follow-ups, never fixed silently).
6. **Tests — `tester`.** Spawn with the brief plus the developer's report: write the regression test that captures this bug — the test that would have failed before the fix — then run it plus the smallest regression set around the touched area, sequentially unless the project documents parallel-safe suites. If the fix is incomplete or something else broke, route back to `developer` with evidence; maximum 2 cycles, then escalate to the user.
7. **Docs — `documentator`, conditional.** Only if user-visible behavior, contracts, or documented flows changed; otherwise skip and say so in the report.
8. **Report.** Root cause in one paragraph; fix summary and files changed; the regression test added; targets run and results; siblings found; docs touched; follow-ups.

## Routing

- Not actually a bug (intended behavior, or a feature request in disguise) → offer `/squad:define` + `/squad:build` (define closes quickly for small scopes).
- Cheaply reproducible by automation and the user wants the strict discipline (failing test BEFORE any fix, tester-led) → offer `/squad:fix`.

## Rules

- No production code before the user confirms the brief.
- Minimal fix; refactors and sibling fixes ride in follow-ups.
- In fix cycles, the developer must not weaken or modify the tester's regression test; disagreements are reported, not edited away.
- Artifacts and reports in English; talk to the user in their own language.
