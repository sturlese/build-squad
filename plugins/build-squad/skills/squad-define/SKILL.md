---
name: squad-define
description: Conversational specification mode for a feature, product idea, or existing spec. Interviews the user until the scope closes, then writes a verifiable implementation contract for squad-build.
---

# Build Squad: define

Use this in the main session. Product definition is a conversation, not a subagent relay. Begin from the user's stated idea or supplied spec path. First read `AGENTS.md`, `README.md`, existing specs, and documented overview commands so you never ask what the project already answers.

Work in short rounds: extract known facts; identify the smallest questions that block a decision; offer a best-guess answer; then wait for the user. Do not begin implementation, silently choose product policy, or invent scope. For an existing spec, preserve accepted decisions and identify only what must be revised.

Close only when the document includes:

- Problem and objective.
- User and primary flow, including significant empty/loading/error states when relevant.
- Numbered, individually verifiable acceptance criteria.
- Explicit excluded scope.
- Compatibility, migration, security, and operational implications when relevant.
- Resolved decisions with rationale, plus only truly non-blocking follow-ups.

Write the closed result to `specs/<slug>.md` (or update the provided path), mark it `status: ready`, and report its path. Tell the user that `$build-squad:squad-build` consumes it. Artifacts are English; speak to the user in their language.
