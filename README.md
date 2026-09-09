# Polybius Cipher Tool

A simple Python 3 terminal app that implements the classical Polybius square cipher.

> **NOTE:** The Polybius cipher is a historical cipher and is **NOT secure** for modern use. This project is for educational purposes only.

## What It Does

- Encrypts text into numeric coordinates using a 5x5 Polybius square
- Decrypts coordinates back into text
- Shows the square and letter mappings
- Demonstrates step-by-step encryption

The 5x5 square combines I and J (a standard convention):

```
    1  2  3  4  5
1   A  B  C  D  E
2   F  G  H  I  K
3   L  M  N  O  P
4   Q  R  S  T  U
5   V  W  X  Y  Z
```

Each letter maps to its row and column: `H` is row 2, column 3 → `23`.

## How to Run

```bash
# Run the interactive app
python main.py

# Run the tests
python -m pytest tests/test_polybius.py -v

# Or without pytest
python -m unittest tests.test_polybius -v
```

## Quick Example

```python
from polybius import encrypt, decrypt

encrypted = encrypt("HELLO")
print(encrypted)   # 23 15 31 31 34

decrypted = decrypt("23 15 31 31 34")
print(decrypted)   # HELLO
```

## Files

- `polybius.py` — Core cipher logic (square, encrypt, decrypt)
- `main.py` — Interactive terminal app
- `tests/test_polybius.py` — Unit tests
