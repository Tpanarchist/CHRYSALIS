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

from chrysalis import Chrysalis, Constraint, Layer, Observation, Trajectory


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


# === INVARIANT 12: The Void generates potential from nothing ===
# (Layer 0 — the formless produces minimal candidates before experience)

def test_domain_generation_empty() -> None:
    """Before experience, the Void generates minimal potential."""
    c = Chrysalis()
    domain = c.generate_domain()
    assert None in domain  # the formless is always present
    assert {} in domain    # empty structure is always possible
    assert len(domain) >= 2


# === INVARIANT 13: The Void generates from experience ===
# (Layer 0 — experienced vocabulary populates the possibility space)

def test_domain_generation_from_experience() -> None:
    """After crystallization, the Void generates from learned vocabulary."""
    c = Chrysalis()
    c.declare("exists", lambda s: s is not None, source="test")
    c.cycle(domain=[None, {"a": 1}, {"b": 2}])

    domain = c.generate_domain()
    # Should contain candidates built from keys "a" and "b"
    assert len(domain) > 2
    assert any(isinstance(d, dict) and "a" in d for d in domain)
    assert any(isinstance(d, dict) and "b" in d for d in domain)
    # Should contain combinations never directly seen
    assert any(isinstance(d, dict) and "a" in d and "b" in d for d in domain)


# === INVARIANT 14: Self-cycle completes without external domain ===
# (Full autonomy — the system operates on self-generated potential)

def test_self_cycle() -> None:
    """The system crystallizes from self-generated potential."""
    c = Chrysalis()
    c.declare("is_dict", lambda s: isinstance(s, dict), source="test")
    c.cycle(domain=[None, {"x": 1}])  # seed with experience

    obs = c.self_cycle()
    assert obs is not None
    assert obs.result is not None  # found a dict from generated domain
    assert isinstance(obs.result, dict)


# === INVARIANT 15: Iterated self-evolution completes ===
# (The system can compound its own growth across multiple cycles)

def test_iterated_evolution() -> None:
    """The system can run iterated self-evolution across multiple steps."""
    c = Chrysalis()
    c.declare("is_dict", lambda s: isinstance(s, dict), source="test")
    c.cycle(domain=[None, {"x": 1}])  # seed with experience

    trajectory = c.evolve(steps=3)
    assert isinstance(trajectory, Trajectory)
    assert len(trajectory.observations) == 3
    assert len(trajectory.reflections) == 3
    assert len(trajectory.domain_sizes) == 3
    assert all(ds > 0 for ds in trajectory.domain_sizes)


# === INVARIANT 16: Fixed-point detection works ===
# (Axiom 4 — The system can see its own evolutionary asymptote)

def test_fixed_point_detection() -> None:
    """The system detects when it converges to a repeating state."""
    c = Chrysalis()
    c.declare("is_dict", lambda s: isinstance(s, dict), source="test")
    c.declare("has_x", lambda s: isinstance(s, dict) and "x" in s, source="test")
    c.cycle(domain=[None, {"x": 1}])  # seed — tight constraints, one survivor

    # With tight constraints and no ambiguity, it should converge
    trajectory = c.evolve(steps=3)
    assert trajectory.fixed_point is True
    assert trajectory.fixed_at is not None
    assert trajectory.fixed_at > 0  # can't be fixed on step 0


# === INVARIANT 17: Trajectory describes itself ===
# (Axiom 3 recursed — self-observation of the evolution arc)

def test_trajectory_self_description() -> None:
    """Trajectories produce self-descriptions (Axiom 3 applied to evolution)."""
    c = Chrysalis()
    c.declare("exists", lambda s: s is not None, source="test")
    c.cycle(domain=[None, {"a": 1}])

    trajectory = c.evolve(steps=2)
    desc = trajectory.describe()
    required_keys = {"steps", "domain_sizes", "results", "reflections_generated", "fixed_point", "fixed_at"}
    assert required_keys.issubset(desc.keys())
    assert desc["steps"] == 2


# === INVARIANT 18: Perturbation expands vocabulary ===
# (Axiom 5 — contradiction resolves by escalation)

def test_perturbation_expands_vocabulary() -> None:
    """Perturbation adds a new structural key when the system is stuck."""
    c = Chrysalis()
    c.state = {"a": True, "b": True}
    original_keys = set(c.state.keys())

    new_key = c._perturb()
    assert new_key is not None
    assert new_key not in original_keys
    assert new_key in c._vocabulary_expansions
    assert c._vocabulary_expansions[new_key] is True


# === INVARIANT 19: Perturbation is safe on non-dict state ===
# (Graceful handling of unperturbable states)

def test_perturbation_returns_none_on_non_dict() -> None:
    """Perturbation returns None when state cannot be expanded."""
    c = Chrysalis()
    c.state = None
    assert c._perturb() is None

    c.state = 42
    assert c._perturb() is None

    c.state = {}
    assert c._perturb() is None


# === INVARIANT 20: Evolution with perturbation breaks fixed points ===
# (Axiom 5 — the system responds to stagnation)

def test_evolution_perturbation_breaks_fixed_point() -> None:
    """The system breaks out of fixed points through vocabulary expansion."""
    c = Chrysalis()
    c.declare("exists", lambda s: s is not None, source="test")
    c.declare("is_dict", lambda s: isinstance(s, dict), source="test")
    c.declare("has_a", lambda s: isinstance(s, dict) and "a" in s, source="test")
    c.cycle(domain=[None, {"a": 1}, {"a": 1, "b": 2}])

    trajectory = c.evolve(steps=5)
    assert trajectory.fixed_point is True
    assert len(trajectory.perturbations) > 0
    # After perturbation, domain should grow
    assert trajectory.domain_sizes[-1] > trajectory.domain_sizes[0]


# === INVARIANT 21: Etheric binding persists state ===
# (Layer 3 — the blueprint survives between executions)

def test_etheric_binding_persists() -> None:
    """State persists to the etheric substrate after crystallization."""
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "test_etheric.json"
        c = Chrysalis()
        c.bind_etheric(path)
        c.declare("exists", lambda s: s is not None, source="test")
        c.cycle(domain=[None, {"a": 1}])

        assert path.exists()
        import json
        data = json.loads(path.read_text(encoding="utf-8"))
        assert data["state"] == {"a": 1}
        assert data["cycle_count"] == 1


# === INVARIANT 22: Etheric state loads across instances ===
# (Layer 3 — new life inherits the old)

def test_etheric_persistence_across_instances() -> None:
    """A new Chrysalis loads state from the same etheric substrate."""
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "test_etheric.json"

        # First life
        c1 = Chrysalis()
        c1.bind_etheric(path)
        c1.declare("exists", lambda s: s is not None, source="test")
        c1.cycle(domain=[None, {"x": 42}])

        # Second life — new instance, same substrate
        c2 = Chrysalis()
        c2.bind_etheric(path)
        assert c2.state == {"x": 42}
        assert c2.cycle_count == 1


# === INVARIANT 23: Vocabulary expansions persist ===
# (Perturbation vocabulary survives process death)

def test_etheric_vocabulary_persists() -> None:
    """Vocabulary expansions from perturbation survive across lives."""
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "test_etheric.json"

        # First life — create state and perturb
        c1 = Chrysalis()
        c1.bind_etheric(path)
        c1.declare("exists", lambda s: s is not None, source="test")
        c1.cycle(domain=[None, {"a": True, "b": True}])
        c1._perturb()
        c1._save()  # persist the perturbation

        assert len(c1._vocabulary_expansions) > 0
        original_expansions = dict(c1._vocabulary_expansions)

        # Second life — vocabulary should be loaded
        c2 = Chrysalis()
        c2.bind_etheric(path)
        assert c2._vocabulary_expansions == original_expansions


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
