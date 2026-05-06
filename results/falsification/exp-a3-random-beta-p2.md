### Concrete Constraint Conflict Resolution Architecture
This architecture implements conflict resolution *as grammatical validity checking*: no invalid tradeoff can ever be articulated, proposed or executed, because it will fail grammatical syntax. No numerical utility functions, no weighted scoring, no "least bad" fallbacks exist.
---
#### 1. Core Grammar Mapping to Constraint Domains
Each linguistic feature is bound directly to resolution mechanics, with no exceptions:
| Source Language Feature | System Role | Binding Rules |
|---|---|---|
| **Navajo classificatory handle stems** | Constraint typing. All constraints *must* be bound to exactly one stem, no generic "priority" labels are permitted. | <ul><li>`-ʼąą` = Safety constraint (maps to Navajo stem for handling fragile / dangerous animate load)</li><li>`-tłʼoo` = Performance constraint (stem for rigid high-mass single object)</li><li>`-tsįįd` = Cost constraint (stem for loose granular countable collection)</li></ul> No constraint may exist unbound. Unclassified constraints are rejected before evaluation.
| **Korean honorific registers** | Contextual priority. Priority is never an inherent property of a constraint type: it is set by the *decision context*, and enforced via grammatical conjugation rules. | 4 mutually exclusive registers, assigned only by impact domain (never stakeholder request): <ul><li>`hasoseo-che` (sacred formal): active when human physical harm is possible. *Grammatical rule: no lower register verb may refer to a higher ranked referent*. In this register `-ʼąą` safety stems cannot be traded against any other stem. This tradeoff is syntactically impossible.</li><li>`haeyo-che` (polite public): active for production user-facing systems. Safety +2 elevation, Performance +1, Cost 0. Tradeoffs only permitted between constraints of equal adjusted elevation.</li><li>`haera-che` (plain informal): active for internal test environments. All constraints receive equal base elevation, bidirectional tradeoffs permitted only with immutable audit logging.</li><li>`hae-che` (casual intimate): active only for offline prototype work. Cost may receive temporary elevation, limited to 72 hour locked windows.</li></ul>
| **Greek telos-aspect marking** | Termination guard. Eliminates infinite tradeoff drift and provisional decision creep. | Every resolution is marked for one of two aspects: <ul><li>`-tos` (Telic): Resolution has a defined termination boundary, will not re-run. Only permitted when *all* constraints remain at or above their base elevation for the active register. Once marked telic, the decision is immutable until context register changes.</li><li>`-menos` (Atelic): Provisional resolution only. Will automatically re-evaluate every cycle. May never persist longer than 12 cycles: after this threshold it must either be upgraded to telic, or rolled back entirely.</li></ul>
---
#### 2. Resolution Execution Flow
1.  **Binding Step**
    On decision request, classify every constraint to exactly one Navajo stem. Any proposition containing unbound constraints is discarded immediately.
2.  **Register Assignment Step**
    Assign exactly one honorific register to the decision context. Mixed registers are grammatically invalid.
3.  **Elevation Check**
    Apply register elevation multipliers. *Any proposed tradeoff that would have a lower elevation constraint override a higher one cannot be conjugated*. There is no code path, no syntax, no way to write this proposition. It is rejected automatically.
4.  **Telos Marking Step**
    If candidate resolution maintains all constraints at or above base elevation: mark `telic`, lock and execute.
    If any tradeoff required lowering a constraint below base elevation: mark `atelic`, schedule mandatory re-evaluation.
5.  **Hard Failure Rule**
    If no grammatically valid proposition can be constructed for the active register, the system returns explicit failure. It will never select an invalid "least bad" tradeoff. This is enforced at the grammar level.
---
### Critical Property
This system cannot drift over time. There is no way to quietly degrade safety for cost, no edge case that can slip through scoring logic: bad tradeoffs are not just forbidden, they are literally unutterable in the grammar the system uses to make decisions.