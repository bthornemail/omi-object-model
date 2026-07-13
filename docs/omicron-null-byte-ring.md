# Omicron: Deterministic Closure Surface

## Role

Omicron is the deterministic normalization and closure surface. It owns
the null-byte ring, algorithmic carry-forward, and closure law.

## Null-Byte Ring

```
0x00  NUL   (origin)
0x20  SP    (readable boundary)
0x7F  DEL   (deletion / seal boundary)
0xFF        (saturated carrier horizon)
```

## Deterministic Closure

```
0x00 ^ 0x20 = 0x20
0x20 ^ 0x7F = 0x5F
0x7F ^ 0xFF = 0x80
0xFF ^ 0x00 = 0xFF

Full witness closure: 0x20 ^ 0x5F ^ 0x80 ^ 0xFF = 0x00
```

## Resolver Envelope

```
FF 00 1C 1D 1E 1F 20 FF
```

| Byte | Meaning |
|------|---------|
| FF   | Gauge / closure horizon |
| 00   | Null origin |
| 1C   | FS (file/frame boundary) |
| 1D   | GS (group/graph boundary) |
| 1E   | RS (record/relation boundary) |
| 1F   | US (unit/symbol boundary) |
| 20   | Readable boundary / earned space |
| FF   | Closure of the same horizon |

## Rules

```
Omicron normalizes and closes.
Omicron does not change.
Omicron does not resolve lived experience.
That belongs to Omnicron.
```

## Doctrine

```
OMI defines. SETCO classifies. Projection is not authority.
```
