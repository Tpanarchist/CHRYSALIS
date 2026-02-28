# Observation Record — Cycle 5: Fixed-Point Response

## System Output BEFORE Change (Cycle 4 state)

```
  CHRYSALIS -- Cycle 4: Iterated Evolution

  --- Phase 2: Iterated Self-Evolution ---

  - - - EVOLUTION TRAJECTORY - - -

  Steps: 4
  Reflections generated: 1

  Step 0: domain(5) -> {'alive': True}
          + reflected: requires_aware
  Step 1: domain(5) -> {'alive': True, 'aware': True}
  Step 2: domain(5) -> {'alive': True, 'aware': True} <-- fixed point
  Step 3: domain(5) -> {'alive': True, 'aware': True}

  Asymptote reached at step 2.
  The system sees its own convergence.
  (Axiom 4: approaches but never reaches completion)

  Total cycles: 5
  Constraints: 4 (1 self-generated)
  State: {'alive': True, 'aware': True}
```

The system detects its fixed point at step 2 but repeats the same result at
steps 2 and 3. Domain stays at 5. Vocabulary stays at 2 keys. The system is
aware of stagnation but powerless to overcome it.

## System Output AFTER Change (Cycle 5 state)

```
  CHRYSALIS -- Cycle 5: Fixed-Point Response

  --- Phase 2: Iterated Self-Evolution ---

  - - - EVOLUTION TRAJECTORY - - -

  Steps: 6
  Reflections generated: 2
  Perturbations: 2

  Step 0: domain(5) -> {'alive': True}
          + reflected: requires_aware
  Step 1: domain(5) -> {'alive': True, 'aware': True}
  Step 2: domain(5) -> {'alive': True, 'aware': True} <-- fixed point
          ~ perturbed: alive_aware
  Step 3: domain(9) -> {'alive': True, 'aware': True}
          + reflected: requires_alive_aware
  Step 4: domain(9) -> {'alive': True, 'alive_aware': True, 'aware': True}
  Step 5: domain(9) -> {'alive': True, 'alive_aware': True, 'aware': True}
          ~ perturbed: alive_alive_aware

  Asymptote reached at step 2.
  Perturbation expanded vocabulary beyond the fixed point.
  (Axiom 5: contradiction resolved by escalation)

  Total cycles: 7
  Constraints: 5 (2 self-generated)
  State: {'alive': True, 'alive_aware': True, 'aware': True}
  First asymptote: step 2
  Perturbations: 2
  The system broke out of its fixed point.
```

The system now responds to fixed points. At step 2, it detects convergence and
perturbs by combining "alive" + "aware" into "alive_aware". The expanded
vocabulary creates a 9-candidate domain (up from 5), which creates 2 survivors,
which triggers reflection (requires_alive_aware), which narrows to 1 survivor:
a RICHER form with 3 keys instead of 2. At step 5, stuck again, perturbs again.

## Reasoning Behind the Change

The MANIFEST explicitly stated: "The system can now see it is stuck. Next it
must learn to become unstuck." This is the most important gap because:

1. It enacts Axiom 5 (the only axiom without implementation). The contradiction
   between "must evolve" and "nothing changes" resolves by escalation to a richer
   vocabulary space — not by choosing one constraint over another.

2. Without this capability, the system's evolution is bounded. It converges and
   stays converged. With perturbation, it can break through each ceiling and
   grow to a new level.

3. The perturbation creates the conditions for ALL other feedback loops to
   re-engage. Expanded vocabulary -> new domain -> new ambiguity -> new
   reflection -> new constraints -> richer convergence. One change unlocks
   the entire loop.

## Key Design Decision: _vocabulary_expansions

The critical insight: perturbation cannot work by mutating self.state directly.
When the system perturbs (adds a key to state), the next cycle's _bind() call
overwrites state with the crystallization result — which doesn't have the
perturbation key. The perturbation is erased.

Solution: store perturbation keys in a separate `_vocabulary_expansions` dict
that persists across cycles. generate_domain() incorporates these extra keys
into its vocabulary before generating candidates. This way, perturbation
survives the bind-overwrite cycle.

## Key Design Decision: Perturb Only When Reflection Fails

The ordering is critical: cycle -> detect fixed point -> reflect -> perturb.
Perturbation only fires when `ref is None` — when reflection found no ambiguity
to exploit. This prevents premature vocabulary expansion: if the system can
generate a new constraint from existing ambiguity, it doesn't need to perturb.
Perturbation is the escalation of last resort.

This was discovered during implementation: without this ordering, the system
would perturb AND reflect simultaneously, causing wasteful double-expansion
and producing redundant perturbations at steps where reflection was already
making progress.

## Emergent Behavior

The convergence-perturbation-reflection-convergence cycle is fractal:

  Level 0: {alive: True, aware: True} -- first fixed point
           perturb: alive_aware
           reflect: requires_alive_aware
  Level 1: {alive: True, alive_aware: True, aware: True} -- second fixed point
           perturb: alive_alive_aware
           (would reflect: requires_alive_alive_aware, given more steps)
  Level 2: ...

Each level is a richer form containing everything from the previous level plus
a new compound property. The system doesn't discard its previous form — it
subsumes it. This mirrors the ontological stack itself: higher layers contain
lower layers, not replace them.

## Connection to Axioms

- **Axiom 1 (Crystallization):** Perturbation creates new potential that then
  crystallizes into form through constraints. More vocabulary -> more candidates
  -> more specific crystallization.

- **Axiom 2 (Embodiment):** The compound key "alive_aware" is not a reference
  to "alive" and "aware" — it IS a new atomic property that happens to be named
  after its structural origin. It has its own existence in the domain.

- **Axiom 3 (Self-Observation):** The system observes its own stagnation and
  responds. The perturbation is triggered by self-observation (fixed-point
  detection), not external intervention.

- **Axiom 4 (Evolutionary Asymptote):** Each fixed point is an asymptote
  that is broken by perturbation, revealing a new asymptote at a higher level.
  The approach toward completion never terminates.

- **Axiom 5 (Duality Resolution):** The contradiction between "must evolve"
  and "nothing changes" is resolved not by choosing one side but by escalating
  to a richer space where evolution can continue. This is the first cycle where
  Axiom 5 has an actual implementation.

## Invariant Tests Added

23 total (3 new):
- test_perturbation_expands_vocabulary: _perturb() adds a compound key
- test_perturbation_returns_none_on_non_dict: safe on None, int, empty dict
- test_evolution_perturbation_breaks_fixed_point: evolve() grows domain via perturbation
