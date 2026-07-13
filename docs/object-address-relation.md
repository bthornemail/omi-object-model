# Object / Address / Relation

## The Model

The OMI Object Model is the inside-out pure object/address/relation
model. It defines six operations in strict order:

```
1. Sign establishes role.
2. Tuple establishes compatibility.
3. Nesting establishes place.
4. Address binds place value.
5. Lowering supplies bits.
6. XOR computes the relation witness.
```

No step may be skipped. No step may be reordered.

## Sign Establishes Role

Before any quantity exists, the sign declares what kind of relation this
is. A sign is not a bit or a flag — it is the identity of the relation
itself. Signs come before quantities.

## Tuple Establishes Compatibility

Two signs form a tuple. The tuple declares that these two signs belong
together in a single relation. The tuple does not compute — it
establishes that computation may occur.

## Nesting Establishes Place

When tuples nest, they create place. Place is not address. Place is the
structural position that an address will later bind. The cons pair
`(car . cdr)` is the primitive nesting form.

## Address Binds Place Value

Address converts structural place into referenced value. The address
binds a specific value to a specific nested position. This is where
notation meets structure.

## Lowering Supplies Bits

Lowering converts the abstract address-bound structure into concrete bit
patterns. The bits are not the relation — they are the material the
relation operates on.

## XOR Computes the Relation Witness

XOR takes the lowered bits and produces a deterministic witness. The
witness is not an interpretation. It is a bitwise result. Same inputs
produce same witness, always.

## Authority

```
OMI defines the object/address/relation model.
SETCO classifies how other things relate to it.
Projection is not authority.
```
