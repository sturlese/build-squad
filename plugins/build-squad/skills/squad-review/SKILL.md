---
name: squad-review
description: Read-only team review of a diff, branch, or PR. Merges security, contract, coverage, architecture, and UX findings into a severity-ranked verdict without modifying files.
---

# Build Squad: review

Resolve the supplied target to an explicit diff, branch comparison, pull request, or current working tree; state the resolution and classify touched files as production, tests, config, and docs. This workflow is strictly read-only: no edits, commits, or quick fixes.

Delegate in parallel:

- `build-squad-auditor` for security and structural review.
- `build-squad-tester` for contracts, regression protection, weakened expectations, and coverage gaps; it may run documented checks sequentially.
- `build-squad-ux` only when user-facing UI, copy, API responses, or flows change; otherwise disclose that it was skipped.

Deduplicate findings, retain the most precise version, rank them STOP/HIGH/MEDIUM/LOW, and anchor them to `file:line` when possible. Deliver approve / approve with comments / request changes; any STOP or HIGH requires request changes. For each finding specify what, where, why it matters, and a precise fix instruction. State unreviewed areas and why. Route confirmed changes to `$build-squad:squad-fix` or `$build-squad:squad-define` plus `$build-squad:squad-build`; never implement inside review. Artifacts are English.
