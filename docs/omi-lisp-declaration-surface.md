# OMI-Lisp: Local Declaration Surface

## Role

OMI-Lisp is the local declaration surface. It uses cons pairs, dot
notation, and NULL seeds.

## Core Types

```
NULL    the folded null seed
SYMBOL  a named identifier
PAIR    a cons cell (car . cdr)
```

NULL is origin. SYMBOL names. PAIR relates.

## Declaration Format

```
(claim
  (id . example)
  (type . rule)
  (statement . "example claim"))
```

Declarations are candidates. Acceptance requires validation.

## Boundary

```
OMI-Lisp declares. OMI notation defines. SETCO classifies.
Projection is not authority.
```
