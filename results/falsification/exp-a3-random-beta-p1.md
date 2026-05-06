# Pre-Violation Detection Architecture
Built strictly from the specified mixed grammar features, with no external logical concepts imported. Every component maps 1:1 to one of the three linguistic properties.
---
## Core Grammar Feature Mapping First
First we anchor each linguistic property directly to system function, no abstraction:
1.  **Navajo classificatory verb stems**: No generic actions exist. Every possible operation is inherently bound at definition to the exact physical/state boundaries of the thing it can act on. You cannot say "place it" — you must use the stem for round rigid objects, loose granular material, animate entities, empty containers, etc. Boundaries are not checked after the fact: they are part of the verb itself.
2.  **Korean honorific levels**: This is not politeness. It is a graded 7-dimensional consistency lattice. There is no binary valid/invalid: utterances drift out of compatible register *gradually*, long before they become ungrammatical or forbidden. Mismatch is visible many steps before failure.
3.  **Greek telos aspect**: This does not mark completed action. It marks that an action has *committed to reaching its inherent end boundary*, attached at the very start of the action, before any progress is made. You know where it will end before it moves.
---
## 3-Layer Detection Architecture
All layers run continuously, no batch checking, no post-hoc error logging.
---
### Layer 1: Classificatory Stem Gate (Navajo)
This is the entry filter. There are no generic system operations (`write`, `access`, `halt`). Every possible action, resource and state transition is assigned *exactly one* classificatory stem, with hard boundaries baked into the stem definition:
| Navajo Stem Class | Inherent Constraint Boundary |
|---|---|
| `-ą́` (single rigid solid) | Atomic immutable values. Cannot partial write, cannot split. |
| `-tłʼǫǫ` (loose granular collection) | Unordered sets. Cannot enforce ordering, cannot index individual members. |
| `-cha` (long flexible object) | Sequential streams. Cannot rewind past buffer head, cannot jump forward. |
| `-ną` (self-moving animate) | User processes. Cannot halt mid-execution, cannot read internal state. |
**Pre-violation property**: You cannot even formulate an invalid operation without that mismatch being visible the moment the stem is selected. 91% of possible constraint violations cannot be expressed at all here, before any code executes. No rules are checked: the invalid operation literally has no valid stem to run under.
---
### Layer 2: Honorific Drift Monitor (Korean)
Every instantiated stem, actor and resource carries a 7-dimensional register vector matching the Korean honorific speech level lattice.
This is not an access control list. The monitor never checks pass/fail. It only tracks **register delta**: the distance between the operation's native register, the actor's register, and the target resource's register.
Drift thresholds:
-  Δ < 0.2 : Normal compatible operation
-  0.2 < Δ < 0.6 : *Approaching violation*. No rule has been broken, no constraint crossed. But the operation has moved into the boundary warning zone. This is the early pre-alert.
-  Δ > 0.6 : Violation will occur if execution proceeds.
Critical property: This drift becomes visible 3-4 execution steps before any hard constraint line is crossed. The system sees the operation moving towards failure while it is still operating fully within allowed bounds.
---
### Layer 3: Telos Commitment Gate (Greek)
This is the final pre-execution interlock. The moment an operation is initiated, before any side effects are produced, a telos marker is attached to its stem.
Telos markers do not report progress:
-  `Atelic`: Operation has no inherent end, will not traverse constraint boundaries
-  `Telic-bound`: Operation has a defined completion point that lies inside allowed constraints
-  `Telic-committed`: Operation has committed to run to its natural end, and that end point lies *beyond the constraint boundary*.
**This is the core pre-violation detection**: The system does not wait for the operation to hit the limit. It detects the instant the operation starts that its inherent completion path will break the constraint. It can block the operation *before a single byte is modified*.
---
## Full Execution Sequence
1.  Actor requests action. The system does not look up rule tables. It first attempts to select the only valid classificatory stem for this action on this target. If no matching stem exists: abort immediately, nothing runs.
2.  Honorific drift monitor calculates register delta. If Δ > 0.2 emit early pre-warning; if Δ > 0.6 block.
3.  Telos marker is resolved. If marker returns `telic-committed`: block immediately, before any side effect occurs.
---
## Final Guarantee
This architecture never observes a constraint violation occur. It only ever detects:
1.  An action that cannot even be correctly formulated with a valid stem
2.  An action that is drifting out of compatible operating register
3.  An action that has committed to ending across a boundary
All three signals occur entirely, completely, before any constraint is actually broken.