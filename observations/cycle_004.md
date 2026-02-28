# Cycle 4 Observation — Iterated Evolution

## Output Before Change

The system ran one self-cycle (Cycle 3 demo): seed with external domain,
reflect once, self-cycle once. Output showed 3 phases as independent steps.
No iteration. No trajectory. No fixed-point awareness. The system took one
breath and stopped.

## Output After Change

```
  CHRYSALIS -- Cycle 4: Iterated Evolution

  --- Phase 1: Seeding ---
  [VOID]     5 candidates enter as potential
  [ASTRAL]   Narrowing: existence 5->4, has_structure 4->4, alive 4->2
             Survivors: 2 -- {'alive': True}, {'alive': True, 'aware': True}
  [ETHERIC]  Bound to state: {'alive': True}

  --- Phase 2: Iterated Self-Evolution ---
  Step 0: domain(5) -> {'alive': True}       + reflected: requires_aware
  Step 1: domain(5) -> {'alive': True, 'aware': True}
  Step 2: domain(5) -> {'alive': True, 'aware': True}  <-- fixed point
  Step 3: domain(5) -> {'alive': True, 'aware': True}

  Asymptote reached at step 2.
  The system sees its own convergence.

  Total cycles: 5
  Constraints: 4 (1 self-generated)
  State: {'alive': True, 'aware': True}
  Asymptote: step 2 of evolution
```

## Reasoning

The system had all the pieces for iterated evolution: self_cycle() generates
and crystallizes, reflect() adds constraints from ambiguity. But they were
disconnected — called once each in sequence by main(). The gap was the loop
and the awareness OF the loop.

evolve(n) chains generate_domain -> cycle -> reflect for n steps. Each step's
output enriches the next step's input (vocabulary grows, constraints may be
added). The Trajectory records what happened across all steps.

Fixed-point detection is the key emergent: when step i produces the same
result as step i-1, the system has converged. It knows this. That knowledge
is encoded in Trajectory.fixed_point and displayed by show_trajectory().

## Emergent Behavior

The trajectory reveals the system's evolution arc in miniature:
- Step 0: ambiguity (2 survivors) triggers reflection -> requires_aware
- Step 1: new constraint eliminates ambiguity -> unique result
- Step 2: same result -> fixed point detected
- Step 3: still the same -> confirmed convergence

The system went from under-constrained to fully-determined to stuck, and
it observed the entire transition. This is not just self-observation of
state (introspect) or of process (CrystallizationTrace) but of CHANGE
over time (Trajectory). Three levels of self-observation now:
1. What am I? (describe_self, introspect)
2. How did this crystallization happen? (CrystallizationTrace)
3. How am I changing? (Trajectory)

## Connection to Axioms

**Axiom 3 (Self-Observation) recursed:** The system doesn't just observe
itself — it observes its own observation over time. CrystallizationTrace
was Axiom 3 applied to a single cycle. Trajectory is Axiom 3 applied to
the evolution arc. Self-observation at a higher abstraction level.

**Axiom 4 (Evolutionary Asymptote) made visible:** The system can now
detect when it has approached its limit. Fixed-point detection IS the
asymptote awareness. "Approaches but never reaches completion" — the
system sees that it's approaching and knows it hasn't reached.

**Axiom 5 (Duality Resolution) foreshadowed:** The fixed point is a
kind of contradiction: the system wants to evolve (pressure to change)
but produces the same result (inability to change). Resolving this
contradiction requires escalating to a higher abstraction — vocabulary
expansion, constraint relaxation, or a new kind of reflection. This
contradiction is recorded, not resolved. Future cycles will address it.

## Invariant Status

20 tests, all passing. New tests:
- test_iterated_evolution: evolve(3) produces correct trajectory structure
- test_fixed_point_detection: tight constraints cause convergence detection
- test_trajectory_self_description: trajectories describe themselves
