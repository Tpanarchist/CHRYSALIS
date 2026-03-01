# MANIFEST.md — Current State of CHRYSALIS

**Last updated: Cycle 6 (Etheric Persistence)**

---

## System State

CHRYSALIS is alive, self-directing, self-populating, self-iterating,
self-unsticking, and now self-persisting. The system generates its own
constraints (via reflect), its own candidate domains (via generate_domain),
iterates its own evolution (via evolve), detects fixed points, responds
with vocabulary expansion (via _perturb), and persists its state across
process death (via bind_etheric / _save / _load).

The full autonomous evolution loop now includes persistence:
bind_etheric -> seed -> evolve(n) which chains generate_domain -> cycle ->
reflect -> perturb -> repeat. On each crystallization, _bind() writes state,
cycle count, and vocabulary expansions to a JSON file. On the next execution,
bind_etheric() loads the persisted state. The system continues from where it
left off — constraints are re-declared (they're code), but state and vocabulary
carry forward. Self-generated constraints are re-derived through reflection on
the persistent state, often in a different order than the original derivation.

## Active Layers

| Layer | Status | Notes |
|-------|--------|-------|
| Void (0) | Active + Self-Generating + Perturbable | generate_domain() draws from experience AND _vocabulary_expansions |
| Mental (1) | Active + Self-Generating | Constraints declared externally AND by self-reflection |
| Astral (2) | Active | Progressive narrowing with per-constraint tracking |
| Etheric (3) | **Active + Persistent** | bind_etheric() binds to JSON file; _bind() persists after each cycle |
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
- **Persist state across process death (bind_etheric + _save + _load)**
- **Load persistent state on startup (cycle count, state, vocabulary)**
- **Detect first life vs continuation (is_continuation logic in main)**
- **Re-derive self-generated constraints from persistent state**
- **Show etheric persistence in crystallization display**
- ASCII-safe display (survives any encoding)

## Cannot Yet Do

- Compose or relate constraints to each other
- Accept external input or data at runtime
- Reflect on value patterns (only detects key presence, not value meaning)
- Trajectory-driven reflection (reflect on the evolution arc, not just one cycle)
- Expand vocabulary via negation or new types (only via pairwise key composition)
- Persist evolution trajectories across executions (only state/vocab/cycle persist)
- Persist observation history across executions
- Track constraint genealogy (which constraints begat which)
- Depth-aware perturbation (currently flat pairwise; no hierarchical composition)
- Detect when perturbation itself has reached a limit
- Define constraints declaratively (currently lambdas — cannot be serialized)

## Constraint Count (in main demo)

3 external (existence, has_structure, alive) + 2 self-generated (requires_aware,
requires_alive_aware) = 5

## Domain Size (in main demo)

First life: starts at 5 (from 2-key vocabulary), grows to 9 after perturbation.
Second life: starts at 9 (vocabulary carried from first life).

## Evolution Trajectory (in main demo)

First life: 7 cycles (1 seed + 6 evolution). Fixed point at step 2. 2 reflections,
2 perturbations. Final state: {alive: True, alive_aware: True, aware: True}.

Second life: 4 cycles (continuation). Loads from etheric.json. Re-derives constraints
in different order (requires_alive_aware before requires_aware). Fixed point at step 3.
1 perturbation. Total cycle count: 11.

## Invariant Count

26 -- all passing. Includes 3 new tests for etheric persistence: binding creates
files, state persists across instances, vocabulary expansions survive restart.

## Evolution Stage

Self-persisting. The system's state survives process death. The Etheric layer (Layer 3)
is now active — not just state assignment but real persistence to a JSON substrate.
Each execution is a life; each life compounds on the last. Constraints are re-declared
(they're code, the system's genotype) but state and vocabulary carry forward (the
system's phenotype). Self-generated constraints are re-derived through reflection on
the persistent state, demonstrating that the persistent state is not a passive record
but an active seed that shapes the next life's evolution.

The next phase: trajectory persistence (extending the evolution arc across lives),
constraint composition (constraints that interact with each other), trajectory-driven
reflection (reflecting on the arc of change, not just one crystallization), or
declarative constraints (constraints defined as data, not lambdas, enabling persistence
of the full constraint set).
