# Manifest: OMI Object Model

```yaml
manifest_id: setco-omi-meta-compile-v0
repo: omi-object-model
role: inside-out pure object/address/relation model
root: /home/main/omi
corpus_root: /home/main/omi/omi---imo/declarations
source_format: omilisp-corpus
targets:
  - /home/main/omi/setco-framework-model
  - /home/main/omi/omi-object-model
mode: manifest-driven-generation
pass: 1-of-3
```

## Doctrine

```
OMI defines the object model.
SETCO classifies how other things relate to it.
NLP proposes.
OMI-Lisp declares.
Coq proves.
C witnesses execution.
Haskell types/projects.
Canvas displays.
Projection is not authority.
No layer may impersonate another.
```

## Role

The Omi Object Model is the inside-out pure object/address/relation model.

It owns:
- omi-notation
- omi-lisp
- omi-port
- null ring
- gauge ring
- Omicron
- Metatron
- Tetragrammatron
- Omnicron

OMI defines. SETCO classifies.

## Corpus classification — port directories

```yaml
# OMI Object Model target only
omi-canon-port:
  target: omi-object-model
  reason: canonical OMI doctrine, notation, symbolic grammar

omi-lisp-port:
  target: omi-object-model
  reason: local declaration surface

omi-port-port:
  target: omi-object-model
  reason: external/adaptive declaration surface

o---o-port:
  target: omi-object-model
  reason: first-principles OMI doctrine and older object-model root

canon-operational:
  target: omi-object-model
  reason: operational OMI canon declarations

metatron-operational:
  target: omi-object-model
  reason: Metatron scribe/transposition operational declarations

# Both targets
omi-isa-port:
  target: both
  reason: executable witness rail; SETCO classifies implementation status

omi-docs-port:
  target: both
  reason: NLP source, doctrine history, transition material

omnicron-port:
  target: both
  reason: resolver-facing binary core and surface bridge

omi-tetragrammatron-port:
  target: both
  reason: bounded validation/governor surface

omi-protocol-port:
  target: both
  reason: legacy protocol language to classify and mine

omnicron-operational:
  target: both
  reason: resolver operational declarations bridge OMI core and SETCO-facing surfaces
```

## Corpus classification — standalone files

```yaml
# OMI Object Model target
addr128.omilisp:
  target: omi-object-model
universal-closure-coding.omilisp:
  target: omi-object-model

# Both targets
boundary-geometry-constitution.omilisp:
  target: both
omi-system.omilisp:
  target: both
omnicron-pair-machine.omilisp:
  target: both
network-bootable-runtime-resolver.omilisp:
  target: both
omi-transmutator-roundtrip.omilisp:
  target: both
```

## Source documents for content emission

```yaml
omi_docs:
  - path: docs/OMI, Omnicron, Tetragrammatron, Metatron, and the Full Notation Hidden in NULL . NULL.md
    role: capstone — null seed, byte-ring, role assignments
  - path: docs/The 8-Tuple Basis of omi---imo?O_o.md
    role: sign-first 8-tuple reading, unary relations
  - path: docs/The Metatron Crossing.md
    role: Metatron role detail
  - path: docs/The Infinite Fraction.md
    role: infinite fraction detail
  - path: OMI Gauge Table, F-Column Surface, and.md
    role: F-column byte geometry, gauge table

reference_only:
  - path: dev-docs/OMI Canon Runtime Atlas.md
    role: runtime reference, not doctrine
  - path: dev-docs/OMI Lazy Distributed Evaluation.md
    role: distributed evaluation reference
```

## Build rules

```
Read from:
  /home/main/omi/omi---imo/declarations

Write only to:
  /home/main/omi/omi-object-model

Do not mutate:
  omi---imo
  omi-canon
  omi-axioms
  omi-canvas
  omi-isa
  omi-lisp
  omi-port
  omnicron
  omi-tetragrammatron
  neighboring source repos

Pass 1: manifest-driven generation (no .omilisp semantic parsing)
Pass 2: semantic .omilisp parsing (deferred)
Pass 3: classified claim promotion (deferred)
```
