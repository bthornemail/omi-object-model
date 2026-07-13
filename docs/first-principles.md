# First Principles

## Core Axioms

The OMI Object Model rests on three load-bearing axioms:

```
Sign establishes role.
XOR computes the relation witness.
Deterministic closure decides the result.
```

No other axiom is required. Everything else is derived structure.

## Sign-First

Every relation begins with a sign. The sign is not a label applied after
the fact. The sign *is* the role. Before bits, before bytes, before
quantity or magnitude — the sign determines what the relation is.

## XOR Computes

XOR is the only computation that decides a relation witness. It does not
interpret. It does not float. It produces a deterministic bit-level
result from two inputs. The result is the same on every platform, in
every language, at every scale.

## Deterministic Closure

A relation closes when its XOR witness returns to zero. This is not a
metaphor. The null-byte ring demonstrates it concretely:

```
0x20 ^ 0x5F ^ 0x80 ^ 0xFF = 0x00
```

Closure is earned, not assumed. No projection, notation, or
interpretation changes the bitwise witness.

## Non-Collapse

```
Projection is not authority.
Notation is not execution.
Interpretation is not acceptance.
No layer may impersonate another.
```

## Core Sentence

```
OMI defines.
SETCO classifies.
Projection is not authority.
```
