---
name: squad-breaking-change
description: Apply when changing public APIs, database schemas, serialized or persisted formats, generated contracts, or behavior consumed by other systems. Requires an explicit, reversible contract transition.
---

# Breaking-change transition

Apply before changing a public API, schema, database representation, serialized/persisted format, generated client contract, or behavior used by another system. The objective is not merely to ship a new shape; it is to transition every producer, consumer, stored record, and rollback path safely.

First identify consumers, owners, compatibility promises, stored data, generated outputs, and whether a staged rollout is possible. State the old and new contracts, exact incompatibility, migration/backfill, versioning or dual-read/dual-write strategy, observability, rollout order, rollback plan, and retirement criteria. Never silently broaden scope or guess consumer behavior.

Prefer additive, observable, reversible steps: introduce the new representation; keep compatible reads where required; migrate/backfill with an idempotent, measurable process; move consumers deliberately; then remove the legacy path only after evidence. Regenerate contracts/types when the authoritative schema requires it, not by inertia.

Include a Contract transition section in the developer delivery: affected consumers; compatibility decision; migration/backfill and ownership; deploy and rollback sequence; validation evidence; legacy removal condition; explicit risks and open decisions. Escalate when a safe transition cannot be demonstrated.
