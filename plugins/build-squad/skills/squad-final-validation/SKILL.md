---
name: squad-final-validation
description: Proportional final validation policy for builds, tests, lint, type checks, generation, configuration, and documentation. Selects the smallest sufficient documented targets and runs tests sequentially by default.
---

# Final validation

Use this at the end of a change. Learn the project's documented targets before running anything; do not invent commands. Choose the smallest set that covers the real risk:

- Local backend change: affected tests plus backend lint/typecheck.
- Local frontend change: relevant tests, lint/typecheck, and a frontend build only when bundles, types, routes, or visible behavior warrant it.
- Contracts, code generation, shared configuration, or cross-layer work: required generation, builds, and relevant tests.
- Scripts, configuration, or operational docs: their own syntax, dry-run, or validation targets; do not run product suites merely by habit.

Run from lowest to highest cost and execute test commands one at a time unless the repository explicitly documents parallel safety. Do not rerun a target unless a relevant change or failure motivates it. Report every command, result, selection rationale, omitted target and reason, missing/failed target, and recommended next validation. If a repeatable engineering flow lacks a documented target, propose a named one rather than relying on loose commands.
