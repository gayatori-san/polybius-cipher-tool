# Polybius Cipher Tool

A simple Python terminal app based on the **exact 5x5 Polybius grid shown in the workshop**.

> **Educational only:** Polybius is a classical cipher and is NOT secure modern encryption.

## Grid

```text
    1  2  3  4  5
1   A  B  C  D  E
2   F  G  H  I  J
3   K  L  M  N  O
4   P  Q  R  S  T
5   U  V  W  X  Y
```

The first digit is the row and the second digit is the column.

Examples:

```text
H = 23
E = 15
L = 32
O = 35

HELLO = 23 15 32 32 35
```

**Z has no coordinate** because the workshop grid contains A-Y only. The program reports an error if Z is entered.

## Run

```bash
python3 main.py
```

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Web version

The `web/` folder contains a simple browser version using HTML, CSS and JavaScript. It uses the same workshop grid.

## Files

- `polybius.py` — cipher logic
- `main.py` — terminal interface
- `tests/test_polybius.py` — tests
- `web/` — browser interface
