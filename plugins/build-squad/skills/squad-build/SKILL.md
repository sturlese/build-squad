---
name: squad-build
description: Delivery pipeline for a closed specification. Validates the contract, delegates UX/development/testing/audit/documentation in bounded stages, and verifies each acceptance criterion.
---

# Build Squad: build

Use the supplied spec path or inline spec as the contract. Refuse politely and route to `$build-squad:squad-define` if the spec lacks a problem, explicit excluded scope, numbered individually verifiable acceptance criteria, or has unresolved questions/draft status.

1. Read project context (`AGENTS.md`, README, architecture docs, documented overview commands) and pass the relevant slice to every delegated role.
2. Determine whether the scope is user-facing. Delegate `build-squad-ux` first only when it is; otherwise state why it is skipped.
3. Delegate `build-squad-developer` with the closed scope, acceptance criteria, UX findings, and an instruction to apply `$build-squad:squad-semantic-architecture`, `$build-squad:squad-breaking-change`, and `$build-squad:squad-final-validation` whenever their triggers apply.
4. Delegate `build-squad-tester` and `build-squad-auditor` after the implementation. The tester maps every criterion to evidence; the auditor is read-only. Run test commands sequentially unless the project proves they are parallel-safe.
5. Route evidenced failures or STOP/HIGH audit findings back to the developer, at most twice. Escalate remaining issues to the user rather than silently accepting them.
6. Delegate `build-squad-documentator` only when behavior, contracts, or structural maps changed.

Scope never changes mid-build. If implementation proves the spec wrong or incomplete, stop and return to `$build-squad:squad-define`. End with a delivery report: criterion-by-criterion pass/fail evidence; files changed; validation commands/results; audit verdict; documentation changes; known follow-ups; and the user's required sign-off. Artifacts are English.
