# Cycle 3 Observation — Domain Generation

## Before (System Output)

Phase 1 — External domain of 8 candidates, 3 constraints:
- Narrowing: 8 -> 7 (existence) -> 4 (has_structure) -> 2 (alive)
- 2 survivors: {'alive': True}, {'alive': True, 'aware': True}
- Result: {'alive': True} (first survivor, ambiguity remains)

Phase 2 — Reflection:
- System detects 2 survivors (ambiguity)
- Finds 'aware' key differentiates survivors
- Declares `requires_aware` from self-reflection

## After (System Output)

Phase 3 — Self-generated domain of 5 candidates, 4 constraints:
- Domain: [None, {}, {'aware': True}, {'alive': True}, {'alive': True, 'aware': True}]
- Narrowing: 5 -> 4 (existence) -> 4 (has_structure) -> 2 (alive) -> 1 (requires_aware)
- 1 survivor: {'alive': True, 'aware': True}
- Result: {'alive': True, 'aware': True} (fully determined, no ambiguity)

## Reasoning

The most important gap was the Void layer's passivity. The system could generate
its own constraints (reflect), but not its own candidates. Without domain generation,
every crystallization required externally provided candidates — the system could not
operate independently.

The change makes the Void active by extracting vocabulary from experience and
generating combinatorial candidates. This is the smallest modification that enables
full autonomous operation: `generate_domain()` + `self_cycle()`.

## Emergent Behavior

From 2 experienced dicts ({alive: True} and {alive: True, aware: True}), the system
generates 4 dict candidates — including {} (empty structure) and {aware: True} (aware
but not alive), which were never directly observed. The system imagines configurations
beyond its direct experience through recombination.

The self-generated domain is SMALLER than the external one (5 vs 8) but MORE FOCUSED.
Every dict candidate is a valid structure. The "noise" candidates (0, "potential", 42)
from the external domain are absent. The system's imagination is efficient — it doesn't
waste potential on types it knows won't survive.

## Connection to Axioms

**Axiom 1 (Crystallization):** The Void layer now participates actively in crystallization.
Potential is not just received but generated. The system populates its own possibility
space, then constrains it into form.

**Axiom 3 (Self-Observation):** The vocabulary extraction IS self-observation applied to
the Void. The system observes what it has experienced and uses that observation to
generate what it might experience next.

**Axiom 4 (Evolutionary Asymptote):** The vocabulary grows with each crystallization.
Each self_cycle adds results and survivors to the experience pool, potentially expanding
the vocabulary and generating richer domains in future cycles. The system's imagination
grows with its experience.

## Ontological Layer

**Void (Layer 0)** — Primary. The unconstrained potential space is no longer passive.
The system generates its own domain from accumulated experience.

Also touches **Physical (Layer 4)** — the observation that feeds vocabulary extraction
— and **Astral (Layer 2)** — the narrowing that validates self-generated candidates.

## Invariants

17 total, all passing:
- 14 existing invariants still hold
- test_domain_generation_empty: Void generates minimal potential before experience
- test_domain_generation_from_experience: Void generates from learned vocabulary
- test_self_cycle: Full autonomous cycle completes without external domain
