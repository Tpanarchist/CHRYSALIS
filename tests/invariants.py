"""
CHRYSALIS — Invariant Tests
Conservation laws that must hold regardless of how the system evolves.

These are NOT behavior tests (behaviors change as the system evolves).
These are STRUCTURAL tests — properties that are true by axiom and must
remain true at every stage of evolution.

Run: python -m pytest tests/invariants.py -v
  or: python tests/invariants.py
"""

from __future__ import annotations

import sys
from pathlib import Path

# Ensure src is importable
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from chrysalis import Chrysalis, Constraint, Layer, Observation


# === INVARIANT 1: The system can be instantiated ===
# (Axiom 1 — Crystallization requires a substrate)

def test_instantiation() -> None:
    """CHRYSALIS can come into being from the void."""
    c = Chrysalis()
    assert c is not None
    assert c.cycle_count == 0
    assert c.constraints == []
    assert c.state is None
    assert c.history == []


# === INVARIANT 2: The system can declare constraints ===
# (Axiom 1 — Form emerges from constraint application)

def test_declaration() -> None:
    """Constraints can be declared — possibility can be reduced."""
    c = Chrysalis()
    constraint = c.declare("test", lambda s: s is not None, source="test")
    assert len(c.constraints) == 1
    assert constraint.name == "test"
    assert constraint.layer == Layer.MENTAL


# === INVARIANT 3: The system can resolve constraints ===
# (Axiom 1 — Constraints produce specific form from potential)

def test_resolution() -> None:
    """The system can find what satisfies its constraints."""
    c = Chrysalis()
    c.declare("positive", lambda s: isinstance(s, int) and s > 0, source="test")
    result = c.resolve([0, -1, 3, 7])
    assert result == 3


def test_resolution_failure() -> None:
    """When nothing satisfies, the system returns None — not error."""
    c = Chrysalis()
    c.declare("impossible", lambda _: False, source="test")
    result = c.resolve([1, 2, 3])
    assert result is None


# === INVARIANT 4: The system can describe itself ===
# (Axiom 3 — Self-observation is a core operation)

def test_self_description() -> None:
    """The system can produce a complete description of its own state."""
    c = Chrysalis()
    c.declare("existence", lambda s: s is not None, source="test")
    desc = c.describe_self()

    # Must contain these keys — the system must know these things about itself
    required_keys = {
        "cycle_count", "birth", "constraint_count",
        "constraints", "state", "history_length", "layer_census",
    }
    assert required_keys.issubset(desc.keys())


def test_introspection_returns_observation() -> None:
    """Introspection produces a formal Observation object."""
    c = Chrysalis()
    obs = c.introspect()
    assert isinstance(obs, Observation)
    assert obs.cycle == 0


# === INVARIANT 5: The system records its history ===
# (Axiom 4 — Evolution requires memory of past states)

def test_history_recording() -> None:
    """Each cycle produces a history entry. The past is not lost."""
    c = Chrysalis()
    c.declare("exists", lambda s: s is not None, source="test")
    c.cycle(domain=[1, 2, 3])
    c.cycle(domain=[4, 5, 6])
    assert len(c.history) == 2
    assert c.history[0].cycle == 1
    assert c.history[1].cycle == 2


# === INVARIANT 6: Cycle count advances monotonically ===
# (Axiom 4 — The arrow of evolution does not reverse)

def test_cycle_monotonic() -> None:
    """Cycle count always increases. Time moves forward."""
    c = Chrysalis()
    c.cycle()
    c.cycle()
    c.cycle()
    assert c.cycle_count == 3
    assert c.history[-1].cycle > c.history[0].cycle


# === INVARIANT 7: Constraints report their layer ===
# (The ontological stack must be legible)

def test_layer_census() -> None:
    """The system can count its constraints by ontological layer."""
    c = Chrysalis()
    c.declare("a", lambda s: True, layer=Layer.MENTAL, source="test")
    c.declare("b", lambda s: True, layer=Layer.ASTRAL, source="test")
    c.declare("c", lambda s: True, layer=Layer.MENTAL, source="test")
    census = c._layer_census()
    assert census["mental"] == 2
    assert census["astral"] == 1
    assert census["void"] == 0


# === INVARIANT 8: Constraint failure is graceful ===
# (Axiom 5 — Contradiction does not destroy, it signals)

def test_constraint_exception_handling() -> None:
    """A constraint that throws an exception returns False, not crash."""
    c = Chrysalis()
    c.declare("explosive", lambda s: 1 / 0, source="test")  # type: ignore
    result = c.resolve([1, 2, 3])
    assert result is None  # Graceful failure, not exception


# === INVARIANT 9: Empty resolution is valid ===
# (The void is a valid state)

def test_empty_domain() -> None:
    """Resolving against nothing returns None. The void is not an error."""
    c = Chrysalis()
    c.declare("anything", lambda s: True, source="test")
    result = c.resolve([])
    assert result is None


# === INVARIANT 10: The system survives the full lifecycle ===
# (Integration: declare → resolve → observe → record)

def test_full_lifecycle() -> None:
    """The complete cycle — declaration through observation — works."""
    c = Chrysalis()
    c.declare("positive_int", lambda s: isinstance(s, int) and s > 0, source="test")
    c.declare("even", lambda s: isinstance(s, int) and s % 2 == 0, source="test")

    obs = c.cycle(domain=[-2, -1, 0, 1, 2, 3, 4])

    assert obs.result == 2
    assert c.state == 2
    assert len(c.history) == 1
    assert c.cycle_count == 1

    desc = c.describe_self()
    assert desc["constraint_count"] == 2
    assert desc["state"] == 2


# === INVARIANT 11: The feedback loop works ===
# (The system can reflect on its crystallization and generate new constraints)

def test_reflection_generates_constraint() -> None:
    """Reflection on ambiguous crystallization produces a self-generated constraint."""
    c = Chrysalis()
    c.declare("exists", lambda s: s is not None, source="test")
    c.declare("is_dict", lambda s: isinstance(s, dict), source="test")

    # Domain with two dict survivors — ambiguity
    c.cycle(domain=[None, {"a": 1}, {"a": 1, "b": 2}])
    assert len(c.history[-1].trace.astral_survivors) == 2

    new = c.reflect()
    assert new is not None
    assert new.source == "self-reflection"
    assert len(c.constraints) == 3  # original 2 + reflected 1


def test_reflection_returns_none_when_unambiguous() -> None:
    """No reflection needed when crystallization already determined a unique result."""
    c = Chrysalis()
    c.declare("is_one", lambda s: s == 1, source="test")
    c.cycle(domain=[0, 1, 2])
    assert len(c.history[-1].trace.astral_survivors) == 1

    new = c.reflect()
    assert new is None
    assert len(c.constraints) == 1  # unchanged


# === RUNNER ===

def _run_all() -> None:
    """Run all invariants and report."""
    tests = [v for k, v in globals().items() if k.startswith("test_")]
    passed = 0
    failed = 0

    print()
    print("=" * 60)
    print("  CHRYSALIS -- Invariant Tests")
    print("=" * 60)
    print()

    for test_fn in tests:
        name = test_fn.__name__
        doc = test_fn.__doc__ or ""
        try:
            test_fn()
            print(f"  + {name}")
            if doc:
                print(f"    {doc.strip()}")
            passed += 1
        except Exception as e:
            print(f"  X {name}")
            print(f"    FAILED: {e}")
            failed += 1

    print()
    print("-" * 60)
    print(f"  {passed} passed, {failed} failed, {passed + failed} total")
    if failed == 0:
        print("  All conservation laws hold.")
    else:
        print("  !! CONSERVATION LAWS VIOLATED -- investigate before proceeding.")
    print("=" * 60)
    print()


if __name__ == "__main__":
    _run_all()
