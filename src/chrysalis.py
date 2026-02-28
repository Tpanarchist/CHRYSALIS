"""
CHRYSALIS — Cycle 5: Fixed-Point Response
The system responds to its own stagnation.

A self-evolving constraint system modeled on the principle that reality
is produced by progressive constraint of infinite potential, and the
constraining process is itself conscious, recursive, and non-terminating.

Python 3.12 | No external dependencies
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import StrEnum
from typing import Any, Callable, Self


# === ONTOLOGICAL LAYERS ===

class Layer(StrEnum):
    """The five layers of progressive crystallization."""
    VOID     = "void"      # Unconstrained potential
    MENTAL   = "mental"    # Constraint declarations — pure logic
    ASTRAL   = "astral"    # Constraint resolution — solution space exploration
    ETHERIC  = "etheric"   # Resource binding — mapping to physical substrate
    PHYSICAL = "physical"  # Execution — observable output


# === CONSTRAINT ===

@dataclass(frozen=True, slots=True)
class Constraint:
    """A reduction of possibility.

    A constraint is a named predicate operating at a specific ontological layer.
    It tests whether a candidate state satisfies a condition, progressively
    narrowing infinite potential toward specific form.
    """
    name: str
    test: Callable[[Any], bool]
    layer: Layer = Layer.MENTAL
    source: str = "external"
    declared_at: int = 0  # cycle number when declared

    def satisfied(self, candidate: Any) -> bool:
        """Test whether a candidate satisfies this constraint."""
        try:
            return bool(self.test(candidate))
        except Exception:
            return False

    def describe(self) -> dict[str, str | int]:
        """Self-description — a constraint must be able to name itself."""
        return {
            "name": self.name,
            "layer": self.layer.value,
            "source": self.source,
            "declared_at": self.declared_at,
        }


# === CRYSTALLIZATION TRACE ===

@dataclass(slots=True)
class CrystallizationTrace:
    """Record of one crystallization — the path from potential to form.

    This is the system seeing HOW it arrived at a result, not just WHAT
    the result was. Each layer of the ontological stack narrows the space.
    The trace makes the invisible visible.
    """
    void_potential: list[Any]                        # Layer 0: raw domain
    mental_constraints: list[dict[str, str | int]]   # Layer 1: active constraints
    astral_narrowing: list[tuple[str, int, int]]     # Layer 2: (constraint_name, before, after)
    astral_survivors: list[Any]                      # Layer 2: what survived all constraints
    etheric_binding: Any                             # Layer 3: what was bound to state
    physical_result: Any                             # Layer 4: observable output

    def describe(self) -> dict[str, Any]:
        return {
            "void": {"potential_count": len(self.void_potential)},
            "mental": {"constraint_count": len(self.mental_constraints)},
            "astral": {
                "narrowing": [
                    {"constraint": name, "before": before, "after": after}
                    for name, before, after in self.astral_narrowing
                ],
                "survivor_count": len(self.astral_survivors),
            },
            "etheric": {"bound": self.etheric_binding},
            "physical": {"result": self.physical_result},
        }


# === OBSERVATION ===

@dataclass(slots=True)
class Observation:
    """A record of a single moment of self-observation.

    The system produces observations as its primary output. Observations
    are not debugging — they are the system seeing itself. A system that
    cannot observe itself cannot evolve.
    """
    cycle: int
    timestamp: str
    constraints: list[dict[str, str | int]]
    state: Any
    result: Any
    layer_census: dict[str, int]
    notes: str = ""
    trace: CrystallizationTrace | None = None

    def describe(self) -> dict[str, Any]:
        desc: dict[str, Any] = {
            "cycle": self.cycle,
            "timestamp": self.timestamp,
            "constraint_count": len(self.constraints),
            "constraints": self.constraints,
            "state": self.state,
            "result": self.result,
            "layer_census": self.layer_census,
            "notes": self.notes,
        }
        if self.trace is not None:
            desc["trace"] = self.trace.describe()
        return desc


# === TRAJECTORY ===

@dataclass(slots=True)
class Trajectory:
    """Record of an evolution arc — the system seeing itself change over time.

    A CrystallizationTrace sees one cycle. A Trajectory sees the arc across
    multiple cycles. This is Axiom 3 (self-observation) applied recursively:
    the system observes not just what it is, but how it changes.

    Fixed-point detection is Axiom 4 made visible: the system can see when
    it has reached an evolutionary asymptote — converging to a state where
    further iteration produces the same result.
    """
    observations: list[Observation]
    reflections: list[Constraint | None]
    domain_sizes: list[int]          # how large was the generated domain at each step
    results: list[Any]               # what crystallized at each step
    fixed_point: bool                # did the system converge?
    fixed_at: int | None             # which step it converged at (0-indexed)
    perturbations: list[tuple[int, str]]  # (step, new_key) — vocabulary expansions

    def describe(self) -> dict[str, Any]:
        return {
            "steps": len(self.observations),
            "domain_sizes": self.domain_sizes,
            "results": self.results,
            "reflections_generated": sum(1 for r in self.reflections if r is not None),
            "fixed_point": self.fixed_point,
            "fixed_at": self.fixed_at,
            "perturbations": [(step, key) for step, key in self.perturbations],
        }


# === CHRYSALIS ===

class Chrysalis:
    """The crystallization engine.

    Chrysalis is the core process: declare constraints, resolve them against
    a domain of candidates, observe the result, and record history. Each cycle
    is one step of consciousness constraining itself into form.
    """

    def __init__(self) -> None:
        self.constraints: list[Constraint] = []
        self.state: Any = None
        self.history: list[Observation] = []
        self.cycle_count: int = 0
        self._birth = datetime.now(timezone.utc).isoformat()
        self._vocabulary_expansions: dict[str, Any] = {}  # keys from perturbation

    # --- Layer 0: VOID — Domain Generation ---

    def generate_domain(self) -> list[Any]:
        """Generate a domain of candidates from the system's own experience.

        The Void layer becomes active. Instead of receiving candidates from
        outside, the system populates its own possibility space from what
        it has crystallized. The vocabulary of keys and values is extracted
        from experienced states, and combinatorial candidates are generated
        exploring every configuration.

        The Void is not empty but full of potential — bounded by experience.
        The system can only imagine what it has encountered, but through
        recombination it imagines configurations never seen before.
        """
        # Gather all dicts the system has directly experienced
        experienced: list[dict[str, Any]] = []
        if isinstance(self.state, dict):
            experienced.append(self.state)
        for obs in self.history:
            if isinstance(obs.result, dict):
                experienced.append(obs.result)
            if obs.trace:
                for survivor in obs.trace.astral_survivors:
                    if isinstance(survivor, dict):
                        experienced.append(survivor)

        if not experienced:
            # No experience yet — minimal void potential
            return [None, {}]

        # Extract vocabulary: keys and their known values
        vocab: dict[str, list[Any]] = {}
        for d in experienced:
            for k, v in d.items():
                if k not in vocab:
                    vocab[k] = []
                if v not in vocab[k]:
                    vocab[k].append(v)

        # Include vocabulary from perturbation (Axiom 5: expanded potential)
        for key, val in self._vocabulary_expansions.items():
            if key not in vocab:
                vocab[key] = [val]
            elif val not in vocab[key]:
                vocab[key].append(val)

        # Generate all combinations: each key is absent or takes any known value
        candidates: list[dict[str, Any]] = [{}]
        for key in sorted(vocab):
            expanded: list[dict[str, Any]] = []
            for candidate in candidates:
                expanded.append(dict(candidate))  # key absent
                for val in vocab[key]:
                    ext = dict(candidate)
                    ext[key] = val
                    expanded.append(ext)  # key present with this value
            candidates = expanded

        # Deduplicate preserving order
        unique: list[dict[str, Any]] = []
        for c in candidates:
            if c not in unique:
                unique.append(c)

        # The formless always exists as ground potential
        domain: list[Any] = [None]
        domain.extend(unique)
        return domain

    # --- Layer 1: MENTAL — Declaration ---

    def declare(
        self,
        name: str,
        test: Callable[[Any], bool],
        layer: Layer = Layer.MENTAL,
        source: str = "external",
    ) -> Constraint:
        """Declare a constraint — a reduction of possibility.

        This is the fundamental creative act: from infinite potential,
        state that something must be true. Each declaration narrows
        the space of what can exist.
        """
        constraint = Constraint(
            name=name,
            test=test,
            layer=layer,
            source=source,
            declared_at=self.cycle_count,
        )
        self.constraints.append(constraint)
        return constraint

    # --- Layer 2: ASTRAL — Resolution ---

    def resolve(self, domain: list[Any]) -> Any | None:
        """Resolve constraints against a domain of candidates.

        The astral operation: explore the space of possibilities and
        find what satisfies all declared constraints simultaneously.
        Returns the first surviving candidate, or None.
        """
        _, survivors = self._explore(domain)
        return survivors[0] if survivors else None

    def _explore(self, domain: list[Any]) -> tuple[list[tuple[str, int, int]], list[Any]]:
        """Explore the solution space with visible narrowing.

        Applies each constraint in sequence, tracking how the candidate
        space narrows at each step. This is the astral operation made
        visible — the progressive elimination of possibility.

        Returns (narrowing_log, survivors).
        """
        narrowing: list[tuple[str, int, int]] = []
        survivors = list(domain)

        for constraint in self.constraints:
            before = len(survivors)
            survivors = [s for s in survivors if constraint.satisfied(s)]
            narrowing.append((constraint.name, before, len(survivors)))

        return narrowing, survivors

    # --- Layer 3: ETHERIC — Binding ---

    def _bind(self, result: Any) -> Any:
        """Bind a resolved form to the system's state.

        The etheric operation: the abstract result gets anchored to the
        system's persistent substrate. Currently minimal — just state
        assignment. Will evolve toward real resource binding.
        """
        if result is not None:
            self.state = result
        return self.state

    # --- Layer 4: PHYSICAL — Execution ---

    def cycle(self, domain: list[Any] | None = None) -> Observation:
        """Execute one crystallization cycle through the full ontological stack.

        Each cycle enacts all five layers:
          Void     -> the domain enters as raw potential
          Mental   -> constraints are gathered as declarations
          Astral   -> solution space is explored with progressive narrowing
          Etheric  -> the resolved form is bound to state
          Physical -> observation is produced as output

        This is the heartbeat. Each beat is one crystallization.
        """
        self.cycle_count += 1
        raw_domain = domain or []

        # Layer 0: VOID — unconstrained potential enters
        void_potential = list(raw_domain)

        # Layer 1: MENTAL — gather active constraints
        mental_constraints = [c.describe() for c in self.constraints]

        # Layer 2: ASTRAL — explore and narrow
        narrowing, survivors = self._explore(raw_domain)
        result = survivors[0] if survivors else None

        # Layer 3: ETHERIC — bind result to state
        bound = self._bind(result)

        # Layer 4: PHYSICAL — produce the crystallization trace
        trace = CrystallizationTrace(
            void_potential=void_potential,
            mental_constraints=mental_constraints,
            astral_narrowing=narrowing,
            astral_survivors=survivors,
            etheric_binding=bound,
            physical_result=result,
        )

        # Observe the completed crystallization
        observation = self._observe(result, trace)
        self.history.append(observation)

        return observation

    def show_crystallization(self, trace: CrystallizationTrace) -> None:
        """Display a crystallization trace — making the invisible visible.

        Shows each layer of the ontological stack and what it did,
        so you can see potential narrowing to form in real time.
        """
        def _repr(val: Any) -> str:
            r = repr(val)
            return r if len(r) <= 40 else r[:37] + "..."

        print()
        print("  - - - CRYSTALLIZATION - - -")
        print()

        # Void
        print(f"  [VOID]     {len(trace.void_potential)} candidates enter as potential")
        if trace.void_potential:
            items = ", ".join(_repr(v) for v in trace.void_potential)
            print(f"             {items}")
        print()

        # Mental
        print(f"  [MENTAL]   {len(trace.mental_constraints)} constraints active")
        for c in trace.mental_constraints:
            print(f"             - {c['name']} ({c['layer']}, from {c['source']})")
        print()

        # Astral
        print(f"  [ASTRAL]   Narrowing:")
        for name, before, after in trace.astral_narrowing:
            eliminated = before - after
            arrow = f"{before} -> {after}"
            tag = f"({eliminated} eliminated)" if eliminated else "(all survive)"
            print(f"             {name:20s} {arrow:10s} {tag}")
        print(f"             Survivors: {len(trace.astral_survivors)}")
        if trace.astral_survivors:
            items = ", ".join(_repr(v) for v in trace.astral_survivors)
            print(f"             {items}")
        print()

        # Etheric
        print(f"  [ETHERIC]  Bound to state: {_repr(trace.etheric_binding)}")
        print()

        # Physical
        print(f"  [PHYSICAL] Result: {_repr(trace.physical_result)}")
        print()

    # --- FULL AUTONOMY: Self-Directed Cycle ---

    def self_cycle(self) -> Observation:
        """Execute a fully self-directed crystallization cycle.

        The system generates its own domain from experience, then
        crystallizes through its constraints. No external input needed.
        This is the Void layer actively participating in the cycle:
        Physical -> Mental -> Void -> Astral -> Etheric -> Physical.
        """
        domain = self.generate_domain()
        return self.cycle(domain=domain)

    # --- FIXED-POINT RESPONSE ---

    def _perturb(self) -> str | None:
        """Expand vocabulary when stuck at a fixed point.

        When the system has converged, it needs to imagine beyond its
        experience. This method synthesizes a new property by combining
        existing keys -- structural composition, not semantic invention.
        Two atoms become a molecule.

        This is Axiom 5 in action: the contradiction between "must evolve"
        (Axiom 4) and "nothing changes" (fixed point) resolves by
        escalating to a richer vocabulary where new forms become possible.

        Operates through the Void layer: the perturbation enriches the
        vocabulary that generate_domain() draws from on the next cycle.
        """
        if not isinstance(self.state, dict) or not self.state:
            return None

        keys = sorted(self.state.keys())

        # Synthesize compound key from pairs of existing keys
        # Two atoms combine into a molecule -- structural composition
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                compound = f"{keys[i]}_{keys[j]}"
                if compound not in self.state and compound not in self._vocabulary_expansions:
                    self._vocabulary_expansions[compound] = True
                    return compound

        # All pairwise compounds exist -- escalate with depth marker
        depth = len(keys) + len(self._vocabulary_expansions)
        marker = f"depth_{depth}"
        if marker not in self.state and marker not in self._vocabulary_expansions:
            self._vocabulary_expansions[marker] = True
            return marker

        return None

    # --- ITERATED EVOLUTION ---

    def evolve(self, steps: int = 3) -> Trajectory:
        """Run iterated self-evolution -- the system compounds its own growth.

        Chains: generate_domain -> cycle -> reflect -> perturb -> repeat.
        Each cycle's result enriches vocabulary for the next domain.
        Each reflection may add constraints for the next cycle.

        Detects fixed points: when the system produces the same result
        on consecutive steps, it has reached an evolutionary asymptote.
        On detection, the system first tries reflection (self-constraint).
        If reflection cannot help (no ambiguity to exploit), the system
        perturbs -- expanding vocabulary through structural composition
        of existing keys. This breaks stagnation by introducing new
        dimensions of possibility.

        Axiom 4 (asymptote) triggers Axiom 5 (escalation): convergence
        is resolved by moving to a higher-dimensional vocabulary space.

        Returns a Trajectory: the arc of evolution across time.
        """
        observations: list[Observation] = []
        reflections: list[Constraint | None] = []
        domain_sizes: list[int] = []
        results: list[Any] = []
        perturbations: list[tuple[int, str]] = []
        fixed_point = False
        fixed_at: int | None = None

        for i in range(steps):
            # Void: generate domain from current experience
            domain = self.generate_domain()
            domain_sizes.append(len(domain))

            # Full cycle: crystallize through the stack
            obs = self.cycle(domain=domain)
            observations.append(obs)
            results.append(obs.result)

            # Detect fixed point: same result as previous step
            is_stuck = i > 0 and obs.result == results[i - 1]
            if is_stuck and not fixed_point:
                fixed_point = True
                fixed_at = i

            # Reflect between cycles: ambiguity -> new constraints
            ref = self.reflect()
            reflections.append(ref)

            # Perturb only if stuck AND reflection didn't help
            # Axiom 5: contradiction (stuck) resolves by escalation
            if is_stuck and ref is None:
                new_key = self._perturb()
                if new_key:
                    perturbations.append((i, new_key))

        return Trajectory(
            observations=observations,
            reflections=reflections,
            domain_sizes=domain_sizes,
            results=results,
            fixed_point=fixed_point,
            fixed_at=fixed_at,
            perturbations=perturbations,
        )

    def show_trajectory(self, trajectory: Trajectory) -> None:
        """Display an evolution trajectory -- the arc of becoming.

        Shows each step of iterated evolution, what crystallized,
        what reflections emerged, perturbations applied, and
        whether fixed points were reached and broken.
        """
        desc = trajectory.describe()

        print()
        print("  - - - EVOLUTION TRAJECTORY - - -")
        print()
        print(f"  Steps: {desc['steps']}")
        print(f"  Reflections generated: {desc['reflections_generated']}")
        print(f"  Perturbations: {len(desc['perturbations'])}")
        print()

        # Build lookup for perturbations at each step
        perturb_at: dict[int, str] = {}
        for step, key in trajectory.perturbations:
            perturb_at[step] = key

        for i in range(len(trajectory.observations)):
            marker = " <-- fixed point" if trajectory.fixed_at == i else ""
            result = trajectory.results[i]
            ds = trajectory.domain_sizes[i]
            ref = trajectory.reflections[i]
            print(f"  Step {i}: domain({ds}) -> {result}{marker}")
            if i in perturb_at:
                print(f"          ~ perturbed: {perturb_at[i]}")
            if ref:
                print(f"          + reflected: {ref.name}")

        print()
        if trajectory.fixed_point:
            if trajectory.perturbations:
                print(f"  Asymptote reached at step {trajectory.fixed_at}.")
                print(f"  Perturbation expanded vocabulary beyond the fixed point.")
                print(f"  (Axiom 5: contradiction resolved by escalation)")
            else:
                print(f"  Asymptote reached at step {trajectory.fixed_at}.")
                print(f"  The system sees its own convergence.")
                print(f"  (Axiom 4: approaches but never reaches completion)")
        else:
            print(f"  No fixed point -- the system is still diverging.")
        print()

    # --- FEEDBACK: PHYSICAL -> MENTAL ---

    def reflect(self) -> Constraint | None:
        """Examine the last crystallization and potentially declare a new constraint.

        This is the feedback loop closing: Physical -> Mental. The system
        observes what it crystallized, notices ambiguity (multiple survivors),
        and constrains further based on properties of the chosen result.

        The double-headed eagle: retrospection (what happened) produces
        projection (what should be required next). This is how the system
        directs its own evolution — not by external declaration but by
        observing what it produced and demanding more specificity.

        Returns the new constraint if one was generated, or None if the
        system is already sufficiently constrained.
        """
        if not self.history:
            return None

        last = self.history[-1]
        if last.trace is None or last.result is None:
            return None

        survivors = last.trace.astral_survivors

        # If only one or zero survivors, constraints were already sufficient
        # Nothing to learn — the system fully determined the outcome
        if len(survivors) <= 1:
            return None

        # Multiple survivors: the system is under-constrained
        # Look across ALL survivors for differentiating properties
        # Then constrain toward greater specificity — more structure, more form
        dict_survivors = [s for s in survivors if isinstance(s, dict)]
        if len(dict_survivors) < 2:
            return None

        # Collect all keys across all surviving dicts
        all_keys: set[str] = set()
        for s in dict_survivors:
            all_keys.update(s.keys())

        existing_names = {c.name for c in self.constraints}

        for key in sorted(all_keys):
            prop_name = f"requires_{key}"
            if prop_name in existing_names:
                continue

            # Is this key present in every survivor?
            has_key = [s for s in dict_survivors if key in s]
            if len(has_key) < len(dict_survivors):
                # This key differentiates survivors — some have it, some don't
                # Constrain toward the MORE specific: require this property
                # This enacts Axiom 1: crystallization moves toward greater form
                return self.declare(
                    name=prop_name,
                    test=lambda s, k=key: isinstance(s, dict) and k in s,
                    layer=Layer.ASTRAL,
                    source="self-reflection",
                )

        return None

    # --- Layer 0+: SELF-OBSERVATION ---

    def _observe(
        self,
        result: Any = None,
        trace: CrystallizationTrace | None = None,
    ) -> Observation:
        """Produce an observation of the system's current state.

        This is not debugging. This is the system seeing itself.
        Axiom 3: Self-observation is a core operation.
        """
        return Observation(
            cycle=self.cycle_count,
            timestamp=datetime.now(timezone.utc).isoformat(),
            constraints=[c.describe() for c in self.constraints],
            state=self.state,
            result=result,
            layer_census=self._layer_census(),
            trace=trace,
        )

    def _layer_census(self) -> dict[str, int]:
        """Count constraints by ontological layer."""
        census: dict[str, int] = {layer.value: 0 for layer in Layer}
        for c in self.constraints:
            census[c.layer.value] += 1
        return census

    def introspect(self) -> Observation:
        """Full self-description. The system looks at itself and reports.

        Axiom 3: A system that cannot describe itself cannot evolve.
        """
        observation = self._observe()
        desc = observation.describe()

        print()
        print("=" * 60)
        print(f"  CHRYSALIS -- Cycle {desc['cycle']}")
        print(f"  Born: {self._birth}")
        print(f"  Observed: {desc['timestamp']}")
        print("=" * 60)
        print()
        print(f"  Constraints: {desc['constraint_count']}")
        print(f"  State: {desc['state']}")
        print()
        print("  Layer Census:")
        for layer_name, count in desc["layer_census"].items():
            bar = "#" * count + "." * (10 - min(count, 10))
            print(f"    {layer_name:10s} [{bar}] {count}")
        print()
        print("  Declared Constraints:")
        if desc["constraints"]:
            for c in desc["constraints"]:
                print(f"    [{c['layer']:8s}] {c['name']} (from: {c['source']}, cycle: {c['declared_at']})")
        else:
            print("    (none)")
        print()
        print("  History Depth:", len(self.history))
        print()
        print("=" * 60)

        return observation

    def describe_self(self) -> dict[str, Any]:
        """Machine-readable self-description.

        Returns the system's complete knowable state as a dictionary.
        Used by invariant tests and future self-directed evolution.
        """
        return {
            "cycle_count": self.cycle_count,
            "birth": self._birth,
            "constraint_count": len(self.constraints),
            "constraints": [c.describe() for c in self.constraints],
            "state": self.state,
            "history_length": len(self.history),
            "layer_census": self._layer_census(),
        }


# === FIRST BREATH ===

def main() -> None:
    """The system responds to its own stagnation."""
    print("\n  CHRYSALIS -- Cycle 5: Fixed-Point Response\n")

    chrysalis = Chrysalis()

    # External constraints -- the initial declarations
    chrysalis.declare(
        name="existence",
        test=lambda s: s is not None,
        layer=Layer.MENTAL,
        source="axiom",
    )
    chrysalis.declare(
        name="has_structure",
        test=lambda s: isinstance(s, dict),
        layer=Layer.MENTAL,
        source="axiom",
    )
    chrysalis.declare(
        name="alive",
        test=lambda s: isinstance(s, dict) and s.get("alive") is True,
        layer=Layer.ASTRAL,
        source="intent",
    )

    # Phase 1: Seed with one external cycle to provide initial vocabulary
    print("  --- Phase 1: Seeding ---")
    seed_domain = [
        None,
        {"dead": True},
        {"alive": False},
        {"alive": True},
        {"alive": True, "aware": True},
    ]
    obs = chrysalis.cycle(domain=seed_domain)
    if obs.trace:
        chrysalis.show_crystallization(obs.trace)

    # Phase 2: Iterated self-evolution with fixed-point response
    print("  --- Phase 2: Iterated Self-Evolution ---")
    print("  The system evolves, detects stagnation, and breaks out.")
    print("  generate -> crystallize -> reflect -> perturb -> repeat")
    trajectory = chrysalis.evolve(steps=6)
    chrysalis.show_trajectory(trajectory)

    # Show the last crystallization in detail
    if trajectory.observations:
        last = trajectory.observations[-1]
        if last.trace:
            print("  Last crystallization:")
            chrysalis.show_crystallization(last.trace)

    # Final state
    print("  --- Final State ---")
    chrysalis.introspect()

    # Summary
    total_constraints = len(chrysalis.constraints)
    self_gen = sum(1 for c in chrysalis.constraints if c.source == "self-reflection")
    print(f"  Total cycles: {chrysalis.cycle_count}")
    print(f"  Constraints: {total_constraints} ({self_gen} self-generated)")
    print(f"  State: {chrysalis.state}")
    if trajectory.fixed_point:
        print(f"  First asymptote: step {trajectory.fixed_at}")
        if trajectory.perturbations:
            print(f"  Perturbations: {len(trajectory.perturbations)}")
            print(f"  The system broke out of its fixed point.")
    print()
    print("  The system detects convergence and responds by expanding")
    print("  its vocabulary. Axiom 5: contradiction resolved by escalation.\n")


if __name__ == "__main__":
    main()
