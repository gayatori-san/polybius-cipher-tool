# Polybius Cipher Tool

A simple Python terminal app and web version based on the **exact 5x5 Polybius grid shown in the workshop**.

> **Educational only:** Polybius is a classical cipher and is NOT secure modern encryption.

## Grid

```text
    1  2  3  4  5
1   A  B  C  D  E
2   F  G  H  I  J
3   K  L  M  N  O
4   P  Q  R  S  T
5   U  V  W  X  YZ
```

The first digit is the row and the second digit is the column. The workshop puts **Y and Z together in 55**, so both Y and Z encrypt to `55`.

Examples:

```text
H = 23
E = 15
L = 32
O = 35
Y = 55
Z = 55

HELLO = 23 15 32 32 35
```

When decrypting `55`, the result is shown as `Y/Z` because the original letter cannot be known.

## Run

```bash
python3 main.py
```

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Web version

The `web/` folder contains a simple browser version using HTML, CSS and JavaScript. It uses the same workshop grid and logic.

## Files

- `polybius.py` — cipher logic
- `main.py` — terminal interface
- `tests/test_polybius.py` — tests
- `web/` — browser interface
