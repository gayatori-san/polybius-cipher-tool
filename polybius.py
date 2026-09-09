"""Polybius square cipher: classical substitution using a 5x5 grid.

The Polybius cipher maps each letter to a two-digit coordinate.
I and J share the same cell (a common convention).

NOTE: This is a classical cipher and NOT secure for modern use.
"""

# 5x5 Polybius square with I/J combined
SQUARE = [
    ['A', 'B', 'C', 'D', 'E'],
    ['F', 'G', 'H', 'I', 'K'],
    ['L', 'M', 'N', 'O', 'P'],
    ['Q', 'R', 'S', 'T', 'U'],
    ['V', 'W', 'X', 'Y', 'Z'],
]

# Build the letter-to-coordinate lookup table
LETTER_TO_COORD: dict[str, str] = {}
for row_idx, row in enumerate(SQUARE):
    for col_idx, letter in enumerate(row):
        LETTER_TO_COORD[letter] = f"{row_idx + 1}{col_idx + 1}"


def show_square() -> str:
    """Return a formatted string of the Polybius square."""
    header = "    " + "  ".join(str(i) for i in range(1, 6))
    lines = [header]
    for i, row in enumerate(SQUARE):
        lines.append(f"{i+1}   " + "  ".join(row))
    return "\n".join(lines)


def show_mappings() -> str:
    """Return all letter-to-coordinate mappings, sorted."""
    lines = []
    for letter in sorted(LETTER_TO_COORD):
        coord = LETTER_TO_COORD[letter]
        lines.append(f"  {letter} -> {coord}")
    return "\n".join(lines)


def encrypt(text: str) -> str:
    """Encrypt plaintext into Polybius coordinates.

    Converts to uppercase. I and J are treated the same.
    Spaces and punctuation are preserved as-is.

    Args:
        text: The plaintext to encrypt.

    Returns:
        A string of coordinate pairs separated by spaces,
        with original non-alpha characters kept in place.
    """
    result: list[str] = []
    for char in text.upper():
        if char in LETTER_TO_COORD:
            result.append(LETTER_TO_COORD[char])
        else:
            result.append(char)
    return " ".join(result)


def decrypt(text: str) -> str:
    """Decrypt Polybius coordinates back into plaintext.

    Expects pairs of digits like "23 15" or "2315" (space-separated
    or contiguous). Non-digit characters are preserved as-is.

    Args:
        text: The coordinate string to decrypt.

    Returns:
        The decrypted plaintext (uppercase, with I for the I/J cell).
    """
    result: list[str] = []
    digits = ""
    for char in text:
        if char.isdigit():
            digits += char
        else:
            if len(digits) >= 2:
                result.append(_decrypt_digits(digits))
                digits = digits[len(digits) - (len(digits) % 2):]
            result.append(char)
    if digits:
        result.append(_decrypt_digits(digits))
    return "".join(result)


def _decrypt_digits(digits: str) -> str:
    """Decrypt a string of digit pairs into letters."""
    result: list[str] = []
    for i in range(0, len(digits) - 1, 2):
        row = int(digits[i]) - 1
        col = int(digits[i + 1]) - 1
        if 0 <= row < 5 and 0 <= col < 5:
            result.append(SQUARE[row][col])
        else:
            result.append("?")
    return "".join(result)


def encrypt_with_steps(text: str) -> str:
    """Encrypt and show step-by-step mappings.

    Args:
        text: The plaintext to encrypt.

    Returns:
        A multi-line string showing each letter's mapping.
    """
    lines: list[str] = []
    for char in text.upper():
        if char in LETTER_TO_COORD:
            lines.append(f"  {char} -> {LETTER_TO_COORD[char]}")
        else:
            lines.append(f"  {char} -> {char} (unchanged)")
    lines.append("")
    lines.append(f"  Result: {encrypt(text)}")
    return "\n".join(lines)


def example() -> str:
    """Return a simple encryption example."""
    msg = "HELLO"
    encrypted = encrypt(msg)
    return (
        f"  Example: Encrypting '{msg}'\n"
        f"  H -> 23\n"
        f"  E -> 15\n"
        f"  L -> 31\n"
        f"  L -> 31\n"
        f"  O -> 34\n"
        f"  Result: {encrypted}"
    )
