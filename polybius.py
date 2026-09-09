"""Polybius cipher using the exact 5x5 grid shown in the workshop."""

SQUARE = [
    ["A", "B", "C", "D", "E"],
    ["F", "G", "H", "I", "J"],
    ["K", "L", "M", "N", "O"],
    ["P", "Q", "R", "S", "T"],
    ["U", "V", "W", "X", "YZ"],
]

# The workshop combines Y and Z in the final cell, so both map to 55.
LETTER_TO_COORD = {
    letter: f"{row}{col}"
    for row, values in enumerate(SQUARE, 1)
    for col, cell in enumerate(values, 1)
    for letter in cell
}

COORD_TO_LETTER = {
    f"{row}{col}": ("Y/Z" if cell == "YZ" else cell)
    for row, values in enumerate(SQUARE, 1)
    for col, cell in enumerate(values, 1)
}


def create_square():
    """Return the 5x5 square."""
    return SQUARE


def show_square() -> str:
    """Return the workshop-style Polybius square."""
    lines = ["    1  2  3  4  5"]
    for row, values in enumerate(SQUARE, 1):
        lines.append(f"{row}   " + "  ".join(values))
    return "\n".join(lines)


def show_mappings() -> str:
    """Return letter-to-coordinate mappings."""
    return "\n".join(
        f"  {letter} -> {LETTER_TO_COORD[letter]}"
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )


def encrypt(text: str) -> str:
    """Encrypt text using the exact workshop grid.

    Spaces and punctuation are preserved. Y and Z both map to 55.
    """
    result = []
    for char in text.upper():
        if char in LETTER_TO_COORD:
            result.append(LETTER_TO_COORD[char])
        else:
            result.append(char)
    return " ".join(result)


def decrypt(text: str) -> str:
    """Decrypt space-separated two-digit coordinates.

    Coordinate 55 is returned as Y/Z because the workshop combines Y
    and Z in the same cell, so the original letter cannot be known.
    """
    if not text.strip():
        return ""
    result = []
    for token in text.split():
        if len(token) != 2 or not token.isdigit() or token not in COORD_TO_LETTER:
            raise ValueError(f"Invalid coordinate: {token}. Use rows and columns 1-5.")
        result.append(COORD_TO_LETTER[token])
    return "".join(result)


def encrypt_with_steps(text: str) -> str:
    """Return the encryption steps and final result."""
    encrypted = encrypt(text)
    lines = []
    for char in text.upper():
        if char in LETTER_TO_COORD:
            lines.append(f"  {char} -> {LETTER_TO_COORD[char]}")
        else:
            lines.append(f"  {char} -> {char} (unchanged)")
    lines.append("")
    lines.append(f"  Result: {encrypted}")
    return "\n".join(lines)


def example() -> str:
    """Return the workshop-style HELLO example."""
    return """  Example: Encrypting 'HELLO'
  H -> 23
  E -> 15
  L -> 32
  L -> 32
  O -> 35
  Result: 23 15 32 32 35"""
