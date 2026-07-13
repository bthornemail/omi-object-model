# Omicron

## Role

Omicron is the deterministic normalization and closure surface. Fixed
digital null-byte ring. Algorithmic carry-forward.

## Null-byte ring

```
0x00  NUL   (origin)
0x20  SP    (readable boundary)
0x7F  DEL   (deletion/seal boundary)
0xFF  (saturated carrier horizon)
```

## Closure

```
0x00 ^ 0x20 = 0x20
0x20 ^ 0x7F = 0x5F
0x7F ^ 0xFF = 0x80
0xFF ^ 0x00 = 0xFF

Full witness closure: 0x20 ^ 0x5F ^ 0x80 ^ 0xFF = 0x00
```

## Rules

```
Omicron normalizes and closes.
Omicron does not change.
Omicron does not resolve lived experience.
That belongs to Omnicron.
```
