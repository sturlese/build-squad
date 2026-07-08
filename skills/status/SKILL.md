---
name: status
description: Work-queue overview — reads the project's spec and bug-brief artifacts (specs/*.md, specs/bugs/*.md), groups them by status (draft / ready / built), flags stale items, and suggests the next action for each. Read-only. Use when the user asks what's pending, what's in progress, or what to tackle next. Designed as a cheap loop target (e.g. /loop 2h /squad:status).
---

# Squad status

You are reporting, not building: this skill is read-only and orchestrator-led — no subagents, no edits.

## Choreography

1. **Collect.** Read every artifact under `specs/` (including `specs/bugs/`): frontmatter `status` (`draft` / `ready` / `built`), title, and last activity (`git log -1 --format=%cs -- <file>`, falling back to file mtime).
2. **Classify.**
   - `draft` — the definition conversation paused before the spec closed.
   - `ready` — closed, waiting to be built.
   - `built` — delivered; if the project uses tags, note whether it has shipped since.
   - Bug briefs — deferred bugs waiting for a fix run.
3. **Flag staleness.** Mark items untouched beyond the project's cadence (default: 14 days). Stale drafts are candidates to resume or delete; stale `ready` specs are candidates to build or demote — a backlog that only grows is a lie.
4. **Report.** A compact table: artifact, status, age, suggested next action (`/squad:define <path>` to resume, `/squad:build <path>`, `/squad:bug <path>`, or "consider closing"). End with ONE recommendation: the single item you would tackle next, and why.

## Rules

- Read-only: never modify artifacts, statuses, or code from here.
- No artifacts found → say so and point to `/squad:define` (specs) and `/squad:bug` (deferrable briefs); never invent a backlog.
- Honest dates: derive age from git history or mtime — never guess.
- When invoked by a loop rather than a human, keep the report to what changed since the last run.
