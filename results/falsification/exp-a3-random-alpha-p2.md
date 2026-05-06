# Conflict Resolution Architecture
> Built exclusively on the specified mixed grammar features, no external linguistic rules are used.

---
## Core Grammar Primitives First
All system behaviour is bounded strictly by the three imported linguistic rules:
1.  **Arabic triconsonantal roots**: *Every functional concept in the system is derived from a 3-consonant root. No content term exists without a root base.*
    | Root | Core meaning |
    |------|--------------|
    | √K-T-B | constraint conflict |
    | √R-S-M | weight assignment |
    | √F-T-H | resolution output |
    | √N-Q-L | domain tradeoff |
    | √Ḥ-S-N | valid outcome |
2.  **Finnish abessive `-tta`**: *Exclusively marks a constraint domain that is excluded, unmeasured, or temporarily deprioritised for a given calculation. No other use of this suffix is permitted.*
3.  **Quechua evidential suffixes**: *Attached only to complete nodes, never to individual values. Exactly one evidential per system node, no stacking:*
    | Suffix | Epistemic status for this system |
    |--------|-----------------------------------|
    | `-mi`  | Confirmed direct empirical measurement |
    | `-si`  | Inferred from simulation, no live test |
    | `-cha` | Hypothetical edge case, unvalidated |

---
## Architecture Execution Layers
### 1. Constraint Registration Layer
All three domains are instantiated as root-derived terms. If a domain is not specified for input, it is automatically marked abessive:
- Safety = `kasif` < √K-S-F
- Performance = `tarum` < √T-R-M
- Cost = `baḥul` < √B-Ḥ-L
> Example: `baḥultta` = *cost-abessive* = this calculation will run without accounting for cost constraints

---
### 2. Conflict Detection Node
A conflict `katab` < √K-T-B is registered if ≥2 non-abessive constraints return opposing threshold values. Every conflict node is tagged with an evidential *before any processing occurs*:
| Conflict Node | Meaning |
|---|---|
| `katab-mi` | Conflict observed running live on the system |
| `katab-si` | Conflict predicted only from simulation models |
| `katab-cha` | Conflict hypothesised for untested boundary conditions |

---
### 3. Weight Assignment Step
Weights are derived from root √R-S-M. This layer enforces grammar-based hard rules for deprioritisation:
1.  For `katab-mi` (confirmed real conflict): mark the lowest-variance constraint abessive `-tta`. **Only one domain may ever be marked abessive per calculation.**
2.  For `katab-si` (modelled conflict): mark the constraint with largest measurement error abessive `-tta`. Abessive marking is optional here.
3.  For `katab-cha` (hypothetical conflict): **ABESSIVE MARKING IS FORBIDDEN ENTIRELY**. No domain may be excluded when evaluating hypothetical edge risks.

---
### 4. Resolution Production Layer
Resolutions `fatah` < √F-T-H inherit *exactly the same evidential marker* as the conflict they resolve. Evidential raising is grammatically impossible:
| Conflict Input | Permitted Resolution Output |
|---|---|
| `katab-mi` | Only `fatah-mi`. May carry maximum 1 abessive domain |
| `katab-si` | Only `fatah-si`. May carry 0 or 1 abessive domain |
| `katab-cha` | Only `fatah-cha`. No abessive domains allowed whatsoever |

*No resolution may ever carry a stronger evidential than the original conflict. There is no grammatical way to produce a confirmed `-mi` resolution for a hypothetical `-cha` conflict.*

---
### 5. Outcome Validation Layer
Valid outcomes `ḥasan` < √Ḥ-S-N. If after deployment the resolved state still produces constraint failure, the outcome is marked abessive:
- `ḥasan-mi` = resolution performed as expected, confirmed
- `ḥasantta-mi` = *outcome-abessive, confirmed* = resolution failed, loop back to conflict detection

---
## Grammar-Enforced Hard System Bounds
These are not design choices: they are unavoidable properties of the mixed grammar used:
1.  You can never run a calculation excluding 2 or more domains. There is no grammatical construction for `kasiftta tarumtta` (without safety AND without performance)
2.  You cannot attribute different epistemic status to individual constraints. Evidentials apply only to the whole resolution node. There is no such thing as "safe but uncertain cost".
3.  Hypothetical safety risks can never be resolved by deprioritising cost or performance. The grammar explicitly prohibits abessive marking on `-cha` nodes.