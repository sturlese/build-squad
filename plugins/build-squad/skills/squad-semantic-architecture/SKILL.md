---
name: squad-semantic-architecture
description: Apply to lifecycle states, active/inactive or archived resources, management versus operational lists, shared selectors, state-dependent writes, and reused operational filters. Requires semantic architecture rather than copied filtering logic.
---

# Semantic architecture

Apply this when a task involves active/inactive or archived state, visibility/lifecycle, shared selectors, management versus operational contexts, “can view” versus “can use”, state-dependent writes, or recurring operational filters. When in doubt, apply it and discard irrelevant parts only after analysis.

Close all four layers:

1. One shared base query/list function owns search, common filters, pagination, ordering, permissions, and state filtering.
2. Semantic wrappers expose each business intent, such as management and operational lists; screens must not own ad-hoc state filtering.
3. A backend/service write guard enforces operational usability even if the UI filters choices.
4. History and detail reads remain available for inactive resources unless the product explicitly decides otherwise.

Do not accept per-screen filters, duplicated query logic, frontend-only validation, loose flags that obscure intent, or operational filters that break historical reads. Search for and reuse existing services, selectors, hooks, and queries before adding anything. If a contract changes, regenerate clients/types only when appropriate.

Resolve and report the matrix: management visibility; operational selectability; backend-blocked writes; historical readability. The delivery must name the shared base, semantic wrappers, backend guard, history handling, duplication removed/avoided, and consumers now using the shared piece. If the task does not close this architecture, propose the base/wrappers/guard pattern and wait for alignment.
