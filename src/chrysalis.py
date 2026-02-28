"""
CHRYSALIS — Cycle 3: Domain Generation
The Void awakens. The system generates its own potential.

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
    """The Void awakens. The system generates its own potential."""
    print("\n  CHRYSALIS -- Cycle 3: Domain Generation\n")

    chrysalis = Chrysalis()

    # External constraints — the initial declarations
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

    # An external domain — the last time we provide one
    external_domain = [
        None,                    # void — fails existence
        0,                       # number — fails structure
        "potential",             # string — fails structure
        42,                      # number — fails structure
        {"dead": True},          # structured but not alive
        {"alive": False},        # structured, has key, but not alive
        {"alive": True},         # survives all constraints
        {"alive": True, "aware": True},  # also survives
    ]

    # Phase 1: Crystallize from external domain
    print("  --- Phase 1: External Domain ---")
    obs1 = chrysalis.cycle(domain=external_domain)
    if obs1.trace:
        chrysalis.show_crystallization(obs1.trace)

    # Phase 2: Reflect — system generates constraint from ambiguity
    print("  --- Phase 2: Reflection ---")
    new_c = chrysalis.reflect()
    if new_c:
        print(f"  Self-generated constraint: {new_c.name}")
        print(f"    Source: {new_c.source}")
    print()

    # Phase 3: Self-directed cycle — system generates its own domain
    print("  --- Phase 3: Self-Directed Crystallization ---")
    print("  The system generates its own domain from experience.")
    print("  No external input. The Void is active.")
    print()
    obs2 = chrysalis.self_cycle()
    if obs2.trace:
        chrysalis.show_crystallization(obs2.trace)

    # Final state
    print("  --- Final State ---")
    chrysalis.introspect()

    # Summary
    s1 = len(obs1.trace.astral_survivors) if obs1.trace else 0
    s2 = len(obs2.trace.astral_survivors) if obs2.trace else 0
    g = len(obs2.trace.void_potential) if obs2.trace else 0
    print(f"  External domain:       {len(external_domain)} candidates -> {obs1.result}")
    print(f"    ({s1} survivors -- reflection generated '{new_c.name if new_c else 'nothing'}')")
    print(f"  Self-generated domain: {g} candidates -> {obs2.result}")
    print(f"    ({s2} survivor -- fully self-directed)")
    print()
    print("  The system generates its own potential and constrains it into form.")
    print("  Void is no longer passive. The seed generates its own soil.\n")


if __name__ == "__main__":
    main()
