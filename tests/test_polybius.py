"""Unit tests for the Polybius cipher module."""

import unittest
import sys
import os

# Allow imports from the parent directory
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from polybius import encrypt, decrypt, encrypt_with_steps, show_square, show_mappings, example, LETTER_TO_COORD


class TestEncrypt(unittest.TestCase):
    """Tests for the encrypt function."""

    def test_hello(self) -> None:
        self.assertEqual(encrypt("HELLO"), "23 15 31 31 34")

    def test_lowercase(self) -> None:
        self.assertEqual(encrypt("hello"), "23 15 31 31 34")

    def test_mixed_case(self) -> None:
        self.assertEqual(encrypt("HeLlO"), "23 15 31 31 34")

    def test_spaces(self) -> None:
        self.assertEqual(encrypt("HI THERE"), "23 24  23 45 15 45 15")

    def test_punctuation(self) -> None:
        self.assertEqual(encrypt("HI!"), "23 24  !")

    def test_ij_combined(self) -> None:
        self.assertEqual(encrypt("I"), encrypt("J"))

    def test_empty_string(self) -> None:
        self.assertEqual(encrypt(""), "")

    def test_only_spaces(self) -> None:
        self.assertEqual(encrypt("   "), "       ")

    def test_only_punctuation(self) -> None:
        self.assertEqual(encrypt("!@#"), "! @ #")


class TestDecrypt(unittest.TestCase):
    """Tests for the decrypt function."""

    def test_hello(self) -> None:
        self.assertEqual(decrypt("23 15 31 31 34"), "HELLO")

    def test_with_spaces(self) -> None:
        self.assertEqual(decrypt("23 24  23 45 15 45 15"), "HI THERE")

    def test_with_punctuation(self) -> None:
        self.assertEqual(decrypt("23 24  !"), "HI!")

    def test_empty_string(self) -> None:
        self.assertEqual(decrypt(""), "")


class TestRoundTrip(unittest.TestCase):
    """Encrypt then decrypt should return the original text (uppercase)."""

    def test_round_trip_simple(self) -> None:
        text = "HELLO"
        self.assertEqual(decrypt(encrypt(text)), text)

    def test_round_trip_with_spaces(self) -> None:
        text = "HELLO WORLD"
        self.assertEqual(decrypt(encrypt(text)), text)

    def test_round_trip_lower(self) -> None:
        text = "hello"
        self.assertEqual(decrypt(encrypt(text)), "HELLO")

    def test_round_trip_punctuation(self) -> None:
        text = "HELLO, WORLD!"
        self.assertEqual(decrypt(encrypt(text)), text)


class TestEdgeCases(unittest.TestCase):
    """Tests for edge cases and invalid input."""

    def test_invalid_coordinates(self) -> None:
        result = decrypt("99")
        self.assertEqual(result, "?")

    def test_partial_invalid(self) -> None:
        result = decrypt("23 99 15")
        self.assertEqual(result, "H?E")

    def test_i_j_same(self) -> None:
        self.assertEqual(LETTER_TO_COORD["I"], LETTER_TO_COORD["J"])

    def test_all_letters_encryptable(self) -> None:
        for letter in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            self.assertIn(letter, LETTER_TO_COORD)

    def test_show_square_returns_string(self) -> None:
        result = show_square()
        self.assertIsInstance(result, str)
        self.assertIn("A", result)

    def test_show_mappings_returns_string(self) -> None:
        result = show_mappings()
        self.assertIsInstance(result, str)
        self.assertIn("A -> 11", result)

    def test_example_returns_string(self) -> None:
        result = example()
        self.assertIsInstance(result, str)
        self.assertIn("HELLO", result)

    def test_encrypt_with_steps_returns_string(self) -> None:
        result = encrypt_with_steps("HI")
        self.assertIsInstance(result, str)
        self.assertIn("H -> 23", result)


if __name__ == "__main__":
    unittest.main()
