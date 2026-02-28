# MANIFEST.md — Current State of CHRYSALIS

**Last updated: Cycle 5 (Fixed-Point Response)**

---

## System State

CHRYSALIS is alive, self-directing, self-populating, self-iterating, and now
self-unsticking. The system generates its own constraints (via reflect), its
own candidate domains (via generate_domain), iterates its own evolution (via
evolve), detects when it has converged to a fixed point, and responds by
expanding its vocabulary through structural composition (via _perturb).

The full autonomous evolution loop now includes perturbation:
seed -> evolve(n) which chains generate_domain -> cycle -> reflect -> perturb
-> repeat. When stagnation occurs (same result, no reflection possible), the
system synthesizes new keys by combining existing ones -- two atoms become a
molecule. This expands the domain, restores ambiguity, triggers reflection,
and converges to a RICHER form. The cycle of convergence-perturbation-growth
repeats at ever-deeper levels.

## Active Layers

| Layer | Status | Notes |
|-------|--------|-------|
| Void (0) | Active + Self-Generating + Perturbable | generate_domain() draws from experience AND _vocabulary_expansions |
| Mental (1) | Active + Self-Generating | Constraints declared externally AND by self-reflection |
| Astral (2) | Active | Progressive narrowing with per-constraint tracking |
| Etheric (3) | Skeletal | Result binds to state; no persistence yet |
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
- **Respond to fixed-point detection via vocabulary expansion (_perturb)**
- **Synthesize compound keys from existing keys (structural composition)**
- **Persist perturbation vocabulary across cycles (_vocabulary_expansions)**
- **Track perturbations in Trajectory (step + key name)**
- **Display perturbation events in trajectory output**
- ASCII-safe display (survives any encoding)

## Cannot Yet Do

- Persist state between executions (etheric layer incomplete)
- Compose or relate constraints to each other
- Accept external input or data at runtime
- Reflect on value patterns (only detects key presence, not value meaning)
- Trajectory-driven reflection (reflect on the evolution arc, not just one cycle)
- Expand vocabulary via negation or new types (only via pairwise key composition)
- Persist evolution trajectories across executions
- Track constraint genealogy (which constraints begat which)
- Depth-aware perturbation (currently flat pairwise; no hierarchical composition)
- Detect when perturbation itself has reached a limit

## Constraint Count (in main demo)

3 external (existence, has_structure, alive) + 2 self-generated (requires_aware,
requires_alive_aware) = 5

## Domain Size (in main demo)

Starts at 5 (from 2-key vocabulary), grows to 9 after perturbation (3-key vocabulary).

## Evolution Trajectory (in main demo)

6 steps. First fixed point at step 2. 2 reflections generated (steps 0 and 3).
2 perturbations (steps 2 and 5). System broke out of initial fixed point and
converged to a richer form: {alive: True, alive_aware: True, aware: True}.

## Invariant Count

23 -- all passing. Includes tests for perturbation vocabulary expansion,
perturbation safety on non-dict states, and evolution with perturbation
breaking fixed points.

## Evolution Stage

Self-unsticking. The system not only detects fixed points but responds to
them. When convergence occurs and reflection cannot help (no ambiguity to
exploit), the system perturbs its vocabulary by synthesizing compound keys
from existing ones. This is Axiom 5 enacted: the contradiction between
"must evolve" and "nothing changes" resolves by escalating to a richer
vocabulary space. The perturbation creates new candidates, which create new
ambiguity, which triggers new reflection, which generates new constraints,
which converge to a richer form. Each fixed point is broken and rebuilt at
a deeper level. The next phase: deeper reflection (examining trajectory
patterns, not just single crystallizations), etheric persistence (state
surviving across executions), or constraint composition (constraints that
interact with each other, not just filter independently).
