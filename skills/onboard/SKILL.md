---
name: onboard
description: Bootstrap a project's living documentation so every role performs better — per-directory index.md maps, a system overview, and verified build/test/lint commands, written by the documentator with the auditor flagging sensitive areas. Run once on a new or undocumented repo; safe to re-run to refresh stale maps. Documentation only, no code changes.
---

# Team onboard

You are the orchestrator. Goal: leave the project with the maps this plugin's roles read — per-directory `index.md` files, a system overview, and documented, verified commands — so every later pipeline runs faster and more precisely. This pipeline changes documentation only.

## Choreography

0. **Inventory (you).** Map the top level: structure, manifests (`package.json`, `pyproject.toml`, `Makefile`, CI config…), existing docs (`README.md`, `CLAUDE.md`, any `index.md`). Identify the real modules — directories with a cohesive responsibility — not every folder. In large repos, prioritize where work actually happens (recent git activity) over dead corners, and say what you deprioritized.
1. **Commands — verify, don't guess (you).** The documentator has no shell by design, so YOU verify: extract the project's build/test/lint/run commands from manifests and CI, and confirm the cheap ones actually work (`--help`, dry-runs, a lint pass — not full test suites). Pass the verified list, with evidence, to the documentator as facts to document.
2. **Maps — `documentator`.** Spawn it with the inventory and verified commands. It writes: one `index.md` per significant module in its standard format (purpose, key entry points, use these, avoid/anti-patterns, data & contracts, tests, common tasks, notes) and a system overview (a README architecture section or dedicated doc: architecture, main modules, critical flows, services and entry points, the verified commands). If the project would benefit from a dedicated overview command (e.g. a `make info` target), it proposes the content as a developer follow-up — it never touches build files.
3. **Sensitive areas — `auditor`.** In parallel: a quick read-only pass to flag security-sensitive zones (auth, payments, PII, migrations, secrets handling) so the maps can mark them — "sensitive: audit changes here".
4. **GATE — delivery.** Present: docs created/updated (one line each), the overview, the verified command list with evidence, sensitive-area flags, gaps the documentator could not justify from code (it never invents), and follow-ups (e.g. the proposed overview command for the developer).

## Rules

- Document only what the code justifies — inventing structure is worse than missing it.
- Verifying that a command exists and starts is enough; do not run full test suites to onboard.
- Idempotent: re-running refreshes stale maps in place; never create duplicate index files.
- Respect boundaries: you verify commands, the documentator writes docs, the auditor only flags.
