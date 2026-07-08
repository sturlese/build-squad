---
name: ship
description: Release pipeline — mechanical pre-flight checklist (clean tree, tests green, migrations ordered and reversible, no leaked secrets), changelog drafted from commits, version bump and tag, the project's documented deploy steps, and post-ship smoke checks, with a mandatory human gate before anything irreversible. Use when the user wants to release, deploy, publish, tag, or ship.
---

# Squad ship

You are the orchestrator, and this pipeline is orchestrator-led: it is a checklist plus git mechanics over work that earlier pipelines already verified — spawning agents here would be theater. Its one inviolable property: **nothing irreversible happens before the human gate.**

## Choreography

1. **Release scope.** Determine what ships: commits since the last tag/release (or since the ref the user names). Locate the project's documented release/deploy process (README, CI config, release scripts, Makefile targets). If NO deploy process is documented, say so: offer to ship only the safe parts (changelog, bump, tag) and propose documenting the process as a follow-up.
2. **Pre-flight — mechanical, each item pass/fail.** Any failure stops the pipeline and is reported; no silent skips:
   - Working tree clean, on the expected branch.
   - The relevant test suite green — a release is the one case where running the fuller suite is justified, not overkill. Sequential unless documented parallel-safe.
   - Lint/build pass.
   - Pending migrations enumerated: ordered, reversible, and consistent with any in-flight expand–contract transition (see the breaking-change playbook — never ship the contract step while old instances still serve traffic).
   - Secrets scan over the diff since the last release (keys, tokens, credentials).
3. **Changelog + version.** Draft the changelog from the commits, grouped (features / fixes / breaking). Propose the version bump from the content per the project's versioning scheme, and state why.
4. **GATE — human sign-off (non-skippable).** Present: the changelog, the proposed version, the migration plan, the ROLLBACK plan (previous tag redeploy? migration down? flag?), and the exact deploy steps about to run. Until approval: no commit of the bump, no tag, no push, no publish, no deploy.
5. **Execute.** Bump version file(s) per the project's convention, commit, tag. Run ONLY the documented deploy steps. Steps the security policy blocks for agents (e.g. anything via kubectl or direct cluster access) are never bypassed: hand them to the user as exact copy-pasteable commands and wait.
6. **Post-ship verify.** Run the project's documented smoke checks (health endpoint, critical flows). If none exist, do the minimum sensible check and propose real smoke checks as a follow-up. If smoke fails: activate the rollback plan WITH the user — never roll back unilaterally.
7. **Report.** Version and tag; changelog; pre-flight results item by item; deploy evidence; smoke results; rollback readiness; follow-ups.

## Rules

- Nothing irreversible before the gate: no push, no tag push, no publish, no deploy, no migration on shared environments.
- Only documented deploy commands — never invent deployment steps. Blocked-by-policy steps go to the human, not around the policy.
- Never ship from a dirty tree or a diverged branch.
- Pre-flight items are pass/fail in the report — a skipped check is a failed check unless the user explicitly waived it.
- Artifacts (changelog, tag messages) in English; address the user in their own language.
