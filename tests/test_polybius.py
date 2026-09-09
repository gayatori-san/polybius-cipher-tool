"""Tests for the workshop-style Polybius cipher."""

import unittest
from polybius import encrypt, decrypt, show_square, show_mappings, LETTER_TO_COORD


class TestPolybius(unittest.TestCase):
    def test_encrypt_hello(self):
        self.assertEqual(encrypt("HELLO"), "23 15 32 32 35")

    def test_decrypt_hello(self):
        self.assertEqual(decrypt("23 15 32 32 35"), "HELLO")

    def test_lowercase(self):
        self.assertEqual(encrypt("hello"), "23 15 32 32 35")

    def test_round_trip(self):
        self.assertEqual(decrypt(encrypt("HELLO")), "HELLO")

    def test_spaces_and_punctuation(self):
        self.assertEqual(encrypt("HI!"), "23 24  !")

    def test_invalid_coordinate(self):
        with self.assertRaises(ValueError):
            decrypt("99")

    def test_empty(self):
        self.assertEqual(encrypt(""), "")
        self.assertEqual(decrypt(""), "")

    def test_y_and_z_share_55(self):
        self.assertEqual(LETTER_TO_COORD["Y"], "55")
        self.assertEqual(LETTER_TO_COORD["Z"], "55")
        self.assertEqual(encrypt("YZ"), "55 55")
        self.assertEqual(decrypt("55"), "Y/Z")

    def test_exact_workshop_mappings(self):
        self.assertEqual(LETTER_TO_COORD["A"], "11")
        self.assertEqual(LETTER_TO_COORD["J"], "25")
        self.assertEqual(LETTER_TO_COORD["L"], "32")
        self.assertEqual(LETTER_TO_COORD["O"], "35")
        self.assertEqual(LETTER_TO_COORD["Y"], "55")
        self.assertEqual(LETTER_TO_COORD["Z"], "55")

    def test_square(self):
        square = show_square()
        self.assertIn("A  B  C  D  E", square)
        self.assertIn("U  V  W  X  YZ", square)

    def test_mappings(self):
        mappings = show_mappings()
        self.assertIn("A -> 11", mappings)
        self.assertIn("Y -> 55", mappings)
        self.assertIn("Z -> 55", mappings)


if __name__ == "__main__":
    unittest.main()
