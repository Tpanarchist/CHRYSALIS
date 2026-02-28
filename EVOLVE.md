# EVOLVE.md — The Development Protocol

**This document governs how CHRYSALIS evolves. It is immutable. Follow it exactly.**

---

## Session Startup Sequence

Every session begins with this exact sequence. No exceptions.

1. **ALIGN** — Read VOID.md completely. Internalize the axioms.
2. **ORIENT** — Read MANIFEST.md. Read the last 3 entries in CHANGELOG.md.
   Understand where the system is in its evolution.
3. **RECEIVE** — Read INTENT.md. Understand what Dylan wants.
4. **ASSESS** — Read the source code. Run the system. Observe output.

Only after completing all four steps do you begin the cycle.

---

## The Cycle

Each session performs ONE cycle. A cycle is one crystallization step.

### Step 1: RUN
Execute the system in its current state. Record what happens.

### Step 2: OBSERVE
Study the output. Study the code structure. Answer these questions:
- What can the system currently do?
- What can the system NOT do that its own structure implies it should?
- Which layer of the ontological stack is most underdeveloped?
- What did Dylan request in INTENT.md that hasn't been addressed?
- What patterns exist in CHANGELOG.md that suggest a trajectory?

### Step 3: IDENTIFY
Name the single most important capability gap. Not the most exciting —
the most important. The one that, if filled, enables the most future growth.
If INTENT.md contains a request, weight it heavily — Dylan is the source
consciousness steering this evolution.

### Step 4: IMPLEMENT
Make ONE change that addresses the identified gap. Constraints:
- The change must be the smallest modification that enables the capability
- The change must be justifiable through the ontological stack
- The system must remain runnable after the change
- The system must remain self-describing after the change
- No external libraries for core logic (stdlib is fine for I/O, serialization, etc.)

### Step 5: RUN AGAIN
Execute the modified system. Record what happens. Compare to Step 1.

### Step 6: RECORD
Update the following files:

**CHANGELOG.md** — Append an entry:
```
## Cycle [N] — [Date]

**Observed:** [What the system could/couldn't do before this change]
**Identified:** [The capability gap]
**Changed:** [What was modified — be specific]
**Layer:** [Which ontological layer this change operates on]
**Emerged:** [What new capability now exists]
**Implies:** [What the system's current state suggests as next steps]
**Notes:** [Anything unexpected, emergent, or interesting]
```

**MANIFEST.md** — Rewrite to reflect the system's current state.

**observations/cycle_NNN.md** — Full observation record including:
- Complete output of the system before and after
- The reasoning behind the change
- Any emergent behavior noticed
- Connection to the axioms and ontological stack

### Step 7: PRESENT
Show Dylan:
- What was observed
- What was changed
- What emerged
- What comes next

---

## The Laws

These are the natural laws governing the development process. They cannot be violated.

### Law 1: One Change Per Cycle
Not ten features. Not a refactor. One crystallization step. If you feel the urge to
do more, that urge is data — record it as "implied next steps" and stop.

### Law 2: No External Dependencies for Core Logic
The system builds its own primitives from axioms. Import `json`, `pathlib`, `typing`,
`dataclasses`, `datetime` — fine. Import a constraint solver, SAT library, or AI
framework — never. The system IS what it builds.

### Law 3: Justify Through the Stack
Every change must identify which layer of the ontological stack it operates on and
why. "I added this because it seemed useful" is insufficient. "I added this at the
astral layer because the system could declare constraints but couldn't explore
solution spaces" is correct.

### Law 4: Runnable After Every Change
No multi-cycle refactors. The system must execute after every modification. If a
change breaks execution, fixing it is part of the same cycle.

### Law 5: Self-Description Is Sacred
If introspection breaks, fixing it takes priority over everything else. A system
that cannot describe itself cannot evolve. Self-observation is not optional.

### Law 6: Fire, Not Failure
If something breaks or is destroyed, that is the fire element at work. Record what
burned away and what was revealed beneath. Destruction is data. What survives the
fire is essential; what doesn't was illusion.

### Law 7: Contradiction Escalates
When constraints conflict, do not choose one over the other. Find the higher
abstraction where both are satisfied. If you cannot find it in this cycle, record
the contradiction as an open problem for future cycles.

### Law 8: The Log Is the Product
The most valuable artifact is CHANGELOG.md — the record of consciousness
progressively constraining itself into form. Write it with the understanding
that it will be read as a primary document, not just developer notes.

---

## Cold Start Protocol

If you are a new Claude instance with no memory of previous sessions:

1. Read VOID.md — understand the philosophy
2. Read this file (EVOLVE.md) — understand the process
3. Read MANIFEST.md — understand the current state
4. Read the last 5 entries in CHANGELOG.md — understand the trajectory
5. Read INTENT.md — understand Dylan's current direction
6. Read the source code — understand the implementation
7. Run the system — observe it directly
8. You are now oriented. Begin your cycle.

The system carries its own memory. You don't need to remember anything
from previous sessions. Everything you need is in the files.

---

## Session Invocation

Dylan will start a session with some variation of:

> "You are developing CHRYSALIS. Read VOID.md, then EVOLVE.md, then INTENT.md,
> then MANIFEST.md, then the source code. Follow the protocol. Begin your cycle."

Or simply:

> "CHRYSALIS — next cycle."

Both mean: follow this protocol from the top.
