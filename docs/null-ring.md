# The Null Ring

## Definition

The Null Ring is the folded null seed `(NULL . NULL)` and its byte-ring
interpretation. It begins at zero, traverses the byte space, and closes
back to zero through deterministic XOR.

## The Byte Ring

```
0x00  NUL   (origin)
0x20  SP    (readable boundary)
0x7F  DEL   (deletion / seal boundary)
0xFF        (saturated carrier horizon)
```

## XOR Witness

```
0x00 ^ 0x20 = 0x20
0x20 ^ 0x7F = 0x5F
0x7F ^ 0xFF = 0x80
0xFF ^ 0x00 = 0xFF
```

Full witness closure:

```
0x20 ^ 0x5F ^ 0x80 ^ 0xFF = 0x00
```

## What It Demonstrates

A relation can begin at zero, traverse the entire byte space, and close
back to zero through XOR — no floating interpretation required.

```
Start:   0x00
Step 1:  0x20   (earned readable boundary)
Step 2:  0x5F   (cross-witness)
Step 3:  0x80   (inversion point)
Step 4:  0xFF   (saturation)
Close:   0x00   (full closure to zero)
```

## Boundary

```
The Null Ring closes to zero. Closure is earned, not assumed.
Projection is not authority.
```

## Doctrine

```
OMI defines. SETCO classifies. Projection is not authority.
```
