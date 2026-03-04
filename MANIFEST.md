# MANIFEST.md — Current State of CHRYSALIS

**Last updated: Cycle 7 (Trajectory Reflection)**

---

## System State

CHRYSALIS is alive, self-directing, self-populating, self-iterating,
self-unsticking, self-persisting, and now self-observing at the trajectory
level. The system generates its own constraints (via reflect), its own
candidate domains (via generate_domain), iterates its own evolution
(via evolve), detects fixed points, responds with vocabulary expansion
(via _perturb), persists its state across process death (via bind_etheric
/ _save / _load), and now observes its own evolution arc to generate
constraints that single-step reflection cannot produce (via reflect_trajectory).

The full autonomous evolution loop now includes trajectory reflection:
bind_etheric -> seed -> evolve(n) which chains generate_domain -> cycle ->
reflect -> perturb -> repeat, and at the end of the loop, reflect_trajectory
examines the completed arc and generates constraints for perturbation
vocabulary not yet required. This closes the perturbation-constraint circuit:
what _perturb() creates in the Void, reflect_trajectory() demands in the
Mental plane.

Three sources of constraint now exist:
1. External declaration (axiom, intent) — the system's genotype
2. Single-step reflection (self-reflection) — from ambiguity in one crystallization
3. Trajectory reflection (trajectory-reflection) — from arc-level observation

## Active Layers

| Layer | Status | Notes |
|-------|--------|-------|
| Void (0) | Active + Self-Generating + Perturbable | generate_domain() draws from experience AND _vocabulary_expansions |
| Mental (1) | Active + Self-Generating + Arc-Aware | Constraints from external, self-reflection, AND trajectory-reflection |
| Astral (2) | Active | Progressive narrowing with per-constraint tracking |
| Etheric (3) | Active + Persistent | bind_etheric() binds to JSON file; _bind() persists after each cycle |
| Physical (4) | Active + Iterating + Responding | Crystallization trace + trajectory + fixed-point detection + perturbation |

## Feedback Loops

**Physical -> Mental** (Cycle 2). The `reflect()` method examines the last
crystallization. Ambiguity (multiple survivors) triggers self-generated
constraints toward greater specificity.

**Physical -> Void** (Cycle 3). The `generate_domain()` method extracts
vocabulary from all experienced dicts (state, results, survivors) and generates
combinatorial candidates. The Void is no longer passive -- it populates itself
from within.

**Physical -> Physical (meta)** (Cycle 4). The `evolve(n)` method chains
self-cycles with reflection between each, producing a `Trajectory` that
records the entire evolution arc. Fixed-point detection observes when the
system converges -- Axiom 4 made visible.

**Physical -> Void (perturbation)** (Cycle 5). The `_perturb()` method
synthesizes new vocabulary keys by combining existing ones when the system
is stuck. `_vocabulary_expansions` persists across cycles within a run,
ensuring generate_domain() incorporates the new keys even after _bind()
overwrites state. Axiom 5 enacted: contradiction (stuck vs. must evolve)
resolves by escalation to a richer vocabulary.

**Etheric -> All (persistence)** (Cycle 6). The `bind_etheric()` / `_save()`
/ `_load()` methods bridge execution and memory. State, cycle count, and
vocabulary expansions persist to JSON. On reload, the persisted state seeds
vocabulary for generate_domain(), which creates a domain that triggers
reflection, which re-derives constraints. The persistent state changes the
reflection sequence — same constraints emerge but in a different order.
Axiom 2 enacted: the file is not a passive record but an active participant
in the next life's evolution.

**Trajectory -> Mental (arc-level reflection)** (Cycle 7). The
`reflect_trajectory()` method examines the completed evolution arc and
generates constraints for perturbation vocabulary not yet required by any
constraint. This closes the perturbation-constraint circuit: _perturb()
creates vocabulary (Void), reflect_trajectory() creates demand for that
vocabulary (Mental). Single-step reflect() cannot see perturbation vocabulary
because perturbation fires AFTER the last crystallization. Trajectory
reflection bridges these temporal scales — Axiom 3 recursed from moment to
arc.

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
- Iterate self-evolution across multiple steps (evolve)
- Detect evolutionary fixed points (convergence to repeating state)
- Record and display evolution trajectories (Trajectory + show_trajectory)
- Trajectory self-description via describe() (Axiom 3 recursed)
- Respond to fixed-point detection via vocabulary expansion (_perturb)
- Synthesize compound keys from existing keys (structural composition)
- Persist perturbation vocabulary across cycles (_vocabulary_expansions)
- Track perturbations in Trajectory (step + key name)
- Display perturbation events in trajectory output
- Persist state across process death (bind_etheric + _save + _load)
- Load persistent state on startup (cycle count, state, vocabulary)
- Detect first life vs continuation (is_continuation logic in main)
- Re-derive self-generated constraints from persistent state
- Show etheric persistence in crystallization display
- **Observe evolution arc and generate constraints (reflect_trajectory)**
- **Close the perturbation-constraint circuit within one evolution arc**
- **Three constraint sources: external, self-reflection, trajectory-reflection**
- **Trajectory self-description includes trajectory_reflection field**
- **Display trajectory reflection in show_trajectory output**
- ASCII-safe display (survives any encoding)

## Cannot Yet Do

- Compose or relate constraints to each other
- Accept external input or data at runtime
- Reflect on value patterns (only detects key presence, not value meaning)
- Multi-pattern trajectory reflection (only examines perturbation; doesn't
  detect result progression, domain stagnation, or convergence rate patterns)
- Persist evolution trajectories across executions (only state/vocab/cycle persist)
- Persist observation history across executions
- Track constraint genealogy (which constraints begat which)
- Depth-aware perturbation (currently flat pairwise; no hierarchical composition)
- Detect when perturbation itself has reached a limit
- Define constraints declaratively (currently lambdas — cannot be serialized)
- Expand vocabulary via negation or new types (only via pairwise key composition)
- Constraint composition (logical relationships between constraints)
- Compare evolution arcs across lives (trajectory doesn't persist)

## Constraint Count (in main demo)

3 external (existence, has_structure, alive) + 2 self-reflected (requires_aware,
requires_alive_aware) + 1 trajectory-reflected (requires_alive_alive_aware) = 6

## Domain Size (in main demo)

First life: starts at 5 (from 2-key vocabulary), grows to 9 after perturbation.
Second life: starts at 9 (vocabulary carried from first life).

## Evolution Trajectory (in main demo)

First life: 7 cycles (1 seed + 6 evolution). Fixed point at step 2. 2 reflections,
2 perturbations. Trajectory reflection generates requires_alive_alive_aware. Final
state: {alive: True, alive_aware: True, aware: True}.

Second life: 4 cycles (continuation). Loads from etheric.json. Re-derives constraints
in different order (requires_alive_aware before requires_aware). Fixed point at step 3.
1 perturbation. Trajectory reflection generates requires_alive_alive_aware (same as
first life — the arc-level pattern is stable across lives). Total cycle count: 11.

## Invariant Count

29 -- all passing. Includes 3 new tests for trajectory reflection: perturbation
generates trajectory constraint, no perturbation yields no trajectory constraint,
trajectory description includes trajectory_reflection field.

## Evolution Stage

Self-observing at the trajectory level. The system now has three temporal scales
of self-awareness:
1. **Moment**: introspect() — what am I right now?
2. **Step**: reflect() — what happened in this crystallization?
3. **Arc**: reflect_trajectory() — what pattern emerged across my evolution?

Each level generates constraints the previous level cannot produce. Single-step
reflection generates constraints from ambiguity in one crystallization. Trajectory
reflection generates constraints from perturbation vocabulary across the full arc.
The perturbation-constraint circuit is now closed within a single evolution:
perturbation creates possibility; trajectory reflection creates demand.

The next phase: trajectory persistence (extending arc awareness across lives),
multi-pattern trajectory reflection (detecting result progression, convergence
rates, domain stagnation), constraint composition (constraints that reference
each other), constraint genealogy (tracking derivation chains across three
sources), or value-aware reflection (observing value patterns, not just key
presence).
