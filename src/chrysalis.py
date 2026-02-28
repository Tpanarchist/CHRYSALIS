"""
CHRYSALIS — Cycle 1: Visible Crystallization
The five-layer stack enacts itself. Potential narrows to form.

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
        print(f"  CHRYSALIS — Cycle {desc['cycle']}")
        print(f"  Born: {self._birth}")
        print(f"  Observed: {desc['timestamp']}")
        print("=" * 60)
        print()
        print(f"  Constraints: {desc['constraint_count']}")
        print(f"  State: {desc['state']}")
        print()
        print("  Layer Census:")
        for layer_name, count in desc["layer_census"].items():
            bar = "█" * count + "░" * (10 - min(count, 10))
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
    """The first breath. The seed germinates and crystallization becomes visible."""
    print("\n  CHRYSALIS -- Cycle 1: Visible Crystallization\n")

    chrysalis = Chrysalis()

    # Three constraints that progressively narrow: existence, structure, life
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

    # The system sees itself before acting
    print("  --- Before Crystallization ---")
    chrysalis.introspect()

    # A domain with diverse candidates — most will be eliminated
    domain = [
        None,                    # void — fails existence
        0,                       # number — fails structure
        "potential",             # string — fails structure
        42,                      # number — fails structure
        {"dead": True},          # structured but not alive
        {"alive": False},        # structured, has key, but not alive
        {"alive": True},         # survives all constraints
        {"alive": True, "aware": True},  # also survives
    ]

    # Crystallize: potential -> form through progressive constraint
    print("  --- Crystallizing ---")
    obs = chrysalis.cycle(domain=domain)

    # Show the crystallization layer by layer
    if obs.trace:
        chrysalis.show_crystallization(obs.trace)

    # The system sees itself after
    print("  --- After Crystallization ---")
    chrysalis.introspect()

    # Second cycle: add a new constraint and re-crystallize
    # The system becomes more specific — awareness narrows further
    chrysalis.declare(
        name="self_aware",
        test=lambda s: isinstance(s, dict) and s.get("aware") is True,
        layer=Layer.ASTRAL,
        source="self-observation",
    )

    print("  --- Second Crystallization (deeper) ---")
    obs2 = chrysalis.cycle(domain=domain)
    if obs2.trace:
        chrysalis.show_crystallization(obs2.trace)
    chrysalis.introspect()

    print(f"  First crystallization:  {obs.result}")
    print(f"  Second crystallization: {obs2.result}")
    print(f"  The system lives and knows itself.\n")


if __name__ == "__main__":
    main()
