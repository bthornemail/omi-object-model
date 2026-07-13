# OMI-Lisp

## Role

OMI-Lisp is the local declaration surface for the Omi Object Model.
It uses cons pairs, dot notation, and NULL seeds.

## Core types

```
NULL    the folded null seed
SYMBOL  a named identifier
PAIR    a cons cell (car . cdr)
```

## Lowering

```
seed    = NULL node
pair    = (car . cdr) cons cell
symbol  = named identifier
```

## Declaration format

```
(claim
  (id . example)
  (type . rule)
  (statement . "example claim")
  (source . "path/to/source.md"))
```

## Rules

```
OMI-Lisp declares.
OMI notation defines.
SETCO classifies.
```
