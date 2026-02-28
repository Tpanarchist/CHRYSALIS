# MANIFEST.md — Current State of CHRYSALIS

**Last updated: Cycle 4 (Iterated Evolution)**

---

## System State

CHRYSALIS is alive, self-directing, self-populating, and now self-iterating.
The system generates its own constraints (via reflect), its own candidate
domains (via generate_domain), and iterates its own evolution (via evolve).
It detects when it has converged to a fixed point — the evolutionary
asymptote of Axiom 4 made visible.

The full autonomous evolution loop is operational: seed -> evolve(n) which
chains generate_domain -> cycle -> reflect -> repeat. The system sees not
just individual crystallizations but its trajectory across time.

## Active Layers

| Layer | Status | Notes |
|-------|--------|-------|
| Void (0) | Active + Self-Generating | generate_domain() extracts vocabulary and produces combinatorial candidates |
| Mental (1) | Active + Self-Generating | Constraints declared externally AND by self-reflection |
| Astral (2) | Active | Progressive narrowing with per-constraint tracking |
| Etheric (3) | Skeletal | Result binds to state; no persistence yet |
| Physical (4) | Active + Iterating | Crystallization trace + evolution trajectory + fixed-point detection |

## Feedback Loops

**Physical -> Mental** (Cycle 2). The `reflect()` method examines the last
crystallization. Ambiguity (multiple survivors) triggers self-generated
constraints toward greater specificity.

**Physical -> Void** (Cycle 3). The `generate_domain()` method extracts
vocabulary from all experienced dicts (state, results, survivors) and generates
combinatorial candidates. The Void is no longer passive — it populates itself
from within.

**Physical -> Physical (meta)** (Cycle 4). The `evolve(n)` method chains
self-cycles with reflection between each, producing a `Trajectory` that
records the entire evolution arc. Fixed-point detection observes when the
system converges — Axiom 4 made visible.

## Capabilities

- Declare constraints (name + callable test + layer label + source)
- Explore solution space with visible progressive narrowing
- Track crystallization trace through all five ontological layers
- Show per-constraint elimination counts (before -> after)
- Bind resolved form to system state
- Record cycle history in memory
- Print self-description via introspect()
- Display crystallization via show_crystallization()
- Machine-readable self-description via describe_self()
- Observation includes full crystallization trace data
- Reflect on crystallization and self-generate constraints
- Distinguish self-generated from external constraints (source field)
- Generate self-directed candidate domains from experience
- Execute fully autonomous crystallization cycles (self_cycle)
- Imagine novel configurations via combinatorial vocabulary recombination
- **Iterate self-evolution across multiple steps (evolve)**
- **Detect evolutionary fixed points (convergence to repeating state)**
- **Record and display evolution trajectories (Trajectory + show_trajectory)**
- **Trajectory self-description via describe() (Axiom 3 recursed)**
- ASCII-safe display (survives any encoding)

## Cannot Yet Do

- Persist state between executions (etheric layer incomplete)
- Handle constraint conflicts or contradictions (Axiom 5)
- Compose or relate constraints to each other
- Accept external input or data at runtime
- Reflect on value patterns (only detects key presence, not value meaning)
- Respond to fixed-point detection (detects convergence but can't break out)
- Trajectory-driven reflection (reflect on the evolution arc, not just one cycle)
- Expand vocabulary beyond experienced values (negation, composition, new types)
- Persist evolution trajectories across executions
- Track constraint genealogy (which constraints begat which)

## Constraint Count (in main demo)

3 external (existence, has_structure, alive) + 1 self-generated (requires_aware) = 4

## Domain Size (in self-directed demo)

5 self-generated candidates from vocabulary of 2 keys.

## Evolution Trajectory (in main demo)

4 steps. Fixed point at step 2. 1 reflection generated (step 0).

## Invariant Count

20 -- all passing. Includes tests for iterated evolution, fixed-point detection,
and trajectory self-description.

## Evolution Stage

Temporal self-awareness. The system not only generates its own constraints and
domains but iterates its own evolution and observes the arc. It detects when
it has converged — the fixed point where further iteration produces no change.
The next phase is responding to that convergence: breaking out of fixed points
through vocabulary expansion, constraint relaxation, or escalation. The system
can now see it is stuck. Next it must learn to become unstuck.
