---
name: squad-refactor
description: Behavior-preserving restructuring pipeline. Freezes existing test results as the invariant, delegates implementation and audit, and rejects hidden behavior changes.
---

# Build Squad: refactor

Use the user's target as a restructuring request only when behavior, public contracts, and persisted formats must remain unchanged. Read AGENTS/README and documented context first.

1. Delegate `build-squad-tester` to select and run the smallest sequential baseline. Record every result, including pre-existing failures, and assess whether coverage protects the target. If it does not, stop for characterization tests or explicit human approval.
2. State the structural objective, explicit non-changes, and done condition: baseline results are identical. A necessary public-contract change routes to `$build-squad:squad-define` and `$build-squad:squad-build` with `$build-squad:squad-breaking-change`.
3. Delegate `build-squad-developer`. Test expectations are frozen; only declared mechanical import/path changes are allowed. A discovered defect is a separate `$build-squad:squad-fix` follow-up.
4. Delegate `build-squad-tester` and read-only `build-squad-auditor` to compare against the exact baseline and judge whether coupling/duplication/layering actually improved. Route evidence back to development at most twice.
5. Delegate `build-squad-documentator` to update affected maps.

Report what moved and why, reuse and consumer rewiring, baseline-versus-after results, declared mechanical test edits, findings not fixed, and documentation changes. Artifacts are English.
