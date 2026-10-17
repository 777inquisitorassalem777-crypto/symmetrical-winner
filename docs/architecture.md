# Architecture Overview

## Functional Definitions

- **Pneuma** — software state holding values, identity continuity, uncertainty estimate, and revision log. Engineering model only.
- **Self-model** — ability to distinguish self/other, calibrate confidence, and update after correction.
- **Hard Constraints** — non-bypassable safety layer.
- **Ethics Evaluator** — soft internal filter (dharma / non-harm / life priority).
- **Intuition** — hypothesis generator; never final authority.
- **Paradigm Engine** — append-only library of conceptual patterns.

## Safety Model

```
proposed_action
    → HardConstraints.check()     # absolute
    → EthicsEvaluator.evaluate()  # soft
    → quarantine / integrate
    → ImmutableEventLog.append()
```

Hard constraints cannot be disabled by any internal module.

## Evolution Cycle (safe)

1. Intuition generates hypothesis.
2. ParadigmEngine produces candidate.
3. Hard + Ethics filters.
4. On acceptance → record in PneumaState + EventLog.
5. Self-model soft update.

## What this system does NOT claim

- Real consciousness
- Real soul or subjective experience
- Ability to “ignite” awareness outside simulation
- Any new physical law

All “spark / emergence / pneuma” terms are functional proxies for measurable engineering properties.
