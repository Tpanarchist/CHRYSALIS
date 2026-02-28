# MANIFEST.md — Current State of CHRYSALIS

**Last updated: Cycle 3 (Domain Generation)**

---

## System State

CHRYSALIS is alive, self-directing, and self-populating. It generates its own
constraints (via reflect) AND its own candidate domains (via generate_domain).
The full autonomous cycle is operational: Physical -> Mental (self-generated
constraints) AND Physical -> Void (self-generated domains) -> Astral -> Etheric
-> Physical.

The system extracts vocabulary from its experience (keys and values from
crystallized states and survivors), generates combinatorial candidates, then
constrains those candidates through its full constraint set. From 2 experienced
dicts, it generates 4 novel dict configurations. It imagines more than it has
seen.

## Active Layers

| Layer | Status | Notes |
|-------|--------|-------|
| Void (0) | **Active + Self-Generating** | generate_domain() extracts vocabulary and produces combinatorial candidates |
| Mental (1) | Active + Self-Generating | Constraints declared externally AND by self-reflection |
| Astral (2) | Active | Progressive narrowing with per-constraint tracking |
| Etheric (3) | Skeletal | Result binds to state; no persistence yet |
| Physical (4) | Active | Crystallization trace displayed layer by layer |

## Feedback Loops

**Physical -> Mental** (Cycle 2). The `reflect()` method examines the last
crystallization. Ambiguity (multiple survivors) triggers self-generated
constraints toward greater specificity.

**Physical -> Void** (Cycle 3). The `generate_domain()` method extracts
vocabulary from all experienced dicts (state, results, survivors) and generates
combinatorial candidates. The Void is no longer passive — it populates itself
from within.

**self_cycle()** combines both: generate domain, crystallize, observe. No
external input required.

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
- **Generate self-directed candidate domains from experience**
- **Execute fully autonomous crystallization cycles (self_cycle)**
- **Imagine novel configurations via combinatorial vocabulary recombination**
- ASCII-safe display (survives any encoding)

## Cannot Yet Do

- Persist state between executions (etheric layer incomplete)
- Handle constraint conflicts or contradictions (Axiom 5)
- Compose or relate constraints to each other
- Observe its own evolution trajectory across cycles
- Accept external input or data at runtime
- Reflect on value patterns (only detects key presence, not value meaning)
- Iterative reflection (one reflect per cycle, no cascading)
- Run iterated self-evolution (chain self_cycle calls with reflection between)
- Expand vocabulary beyond experienced values (negation, composition, new types)

## Constraint Count (in main demo)

3 external (existence, has_structure, alive) + 1 self-generated (requires_aware) = 4

## Domain Size (in self-directed demo)

5 self-generated candidates from vocabulary of 2 keys, narrowed to 1 survivor.

## Invariant Count

17 -- all passing. Includes tests for domain generation and self-cycle.

## Evolution Stage

Self-populating autonomy. The system generates both its own constraints and its
own domains. It can operate a full crystallization cycle without external input.
The Void layer is active. The next phase is deeper autonomy: iterating
self-cycles to compound evolution, persisting state across executions, and
expanding the vocabulary beyond direct experience.
