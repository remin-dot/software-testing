"""Unit tests for caesar_cipher module.

Tests follow the Arrange-Act-Assert pattern and provide 100% branch coverage.
"""

import unittest
from caesar_cipher import caesar_cipher


class TestCaesarCipher(unittest.TestCase):
    """Test cases for the caesar_cipher function."""

    # Region: Lowercase Shift Tests
    def test_lowercase_single_char_shift(self):
        """Arrange: single lowercase letter, Act: shift by 1, Assert: correct result."""
        result = caesar_cipher('a', 1)
        self.assertEqual(result, 'b')

    def test_lowercase_multiple_chars_shift(self):
        """Arrange: multiple lowercase letters, Act: shift by 1, Assert: all shifted."""
        result = caesar_cipher('abc', 1)
        self.assertEqual(result, 'bcd')

    def test_lowercase_longer_sequence_shift(self):
        """Arrange: longer lowercase sequence, Act: shift by 3, Assert: correct shift."""
        result = caesar_cipher('hello', 3)
        self.assertEqual(result, 'khoor')

    # Region: Uppercase Shift Tests
    def test_uppercase_single_char_shift(self):
        """Arrange: single uppercase letter, Act: shift by 1, Assert: correct result."""
        result = caesar_cipher('A', 1)
        self.assertEqual(result, 'B')

    def test_uppercase_multiple_chars_shift(self):
        """Arrange: multiple uppercase letters, Act: shift by 1, Assert: all shifted."""
        result = caesar_cipher('ABC', 1)
        self.assertEqual(result, 'BCD')

    def test_uppercase_longer_sequence_shift(self):
        """Arrange: longer uppercase sequence, Act: shift by 3, Assert: correct shift."""
        result = caesar_cipher('HELLO', 3)
        self.assertEqual(result, 'KHOOR')

    # Region: Wrap-around Tests
    def test_lowercase_wrap_around_single(self):
        """Arrange: 'z', Act: shift by 1, Assert: wraps to 'a'."""
        result = caesar_cipher('z', 1)
        self.assertEqual(result, 'a')

    def test_lowercase_wrap_around_multiple(self):
        """Arrange: 'xyz', Act: shift by 1, Assert: wraps correctly."""
        result = caesar_cipher('xyz', 1)
        self.assertEqual(result, 'yza')

    def test_uppercase_wrap_around_single(self):
        """Arrange: 'Z', Act: shift by 1, Assert: wraps to 'A'."""
        result = caesar_cipher('Z', 1)
        self.assertEqual(result, 'A')

    def test_uppercase_wrap_around_multiple(self):
        """Arrange: 'XYZ', Act: shift by 1, Assert: wraps correctly."""
        result = caesar_cipher('XYZ', 1)
        self.assertEqual(result, 'YZA')

    def test_wrap_around_end_of_alphabet_lowercase(self):
        """Arrange: 'abc', Act: shift by 25, Assert: wraps to 'zab'."""
        result = caesar_cipher('abc', 25)
        self.assertEqual(result, 'zab')

    def test_wrap_around_end_of_alphabet_uppercase(self):
        """Arrange: 'ABC', Act: shift by 25, Assert: wraps to 'ZAB'."""
        result = caesar_cipher('ABC', 25)
        self.assertEqual(result, 'ZAB')

    # Region: k > 26 Tests
    def test_k_greater_than_26_lowercase(self):
        """Arrange: 'abc', Act: shift by 27, Assert: equivalent to shift by 1."""
        result = caesar_cipher('abc', 27)
        self.assertEqual(result, 'bcd')

    def test_k_greater_than_26_uppercase(self):
        """Arrange: 'ABC', Act: shift by 27, Assert: equivalent to shift by 1."""
        result = caesar_cipher('ABC', 27)
        self.assertEqual(result, 'BCD')

    def test_k_much_greater_than_26(self):
        """Arrange: 'abc', Act: shift by 52, Assert: equivalent to shift by 0."""
        result = caesar_cipher('abc', 52)
        self.assertEqual(result, 'abc')

    def test_k_large_multiple_of_26(self):
        """Arrange: 'hello', Act: shift by 78, Assert: equivalent to shift by 0."""
        result = caesar_cipher('hello', 78)
        self.assertEqual(result, 'hello')

    # Region: k = 0 Tests
    def test_k_zero_lowercase(self):
        """Arrange: 'abc', Act: shift by 0, Assert: unchanged."""
        result = caesar_cipher('abc', 0)
        self.assertEqual(result, 'abc')

    def test_k_zero_uppercase(self):
        """Arrange: 'ABC', Act: shift by 0, Assert: unchanged."""
        result = caesar_cipher('ABC', 0)
        self.assertEqual(result, 'ABC')

    def test_k_zero_mixed(self):
        """Arrange: 'Hello World!', Act: shift by 0, Assert: unchanged."""
        result = caesar_cipher('Hello World!', 0)
        self.assertEqual(result, 'Hello World!')

    # Region: Non-letter Character Tests
    def test_single_digit_unchanged(self):
        """Arrange: '1', Act: apply cipher, Assert: unchanged."""
        result = caesar_cipher('1', 5)
        self.assertEqual(result, '1')

    def test_multiple_digits_unchanged(self):
        """Arrange: '123', Act: apply cipher, Assert: all unchanged."""
        result = caesar_cipher('123', 5)
        self.assertEqual(result, '123')

    def test_single_space_unchanged(self):
        """Arrange: ' ', Act: apply cipher, Assert: unchanged."""
        result = caesar_cipher(' ', 5)
        self.assertEqual(result, ' ')

    def test_multiple_spaces_unchanged(self):
        """Arrange: '   ', Act: apply cipher, Assert: all unchanged."""
        result = caesar_cipher('   ', 5)
        self.assertEqual(result, '   ')

    def test_special_characters_unchanged(self):
        """Arrange: '!@#$%', Act: apply cipher, Assert: all unchanged."""
        result = caesar_cipher('!@#$%', 5)
        self.assertEqual(result, '!@#$%')

    def test_punctuation_unchanged(self):
        """Arrange: '.,:;!?', Act: apply cipher, Assert: all unchanged."""
        result = caesar_cipher('.,:;!?', 5)
        self.assertEqual(result, '.,:;!?')

    # Region: Mixed Input Tests
    def test_mixed_case_and_letters(self):
        """Arrange: 'Hello', Act: shift by 1, Assert: case preserved."""
        result = caesar_cipher('Hello', 1)
        self.assertEqual(result, 'Ifmmp')

    def test_mixed_with_numbers(self):
        """Arrange: 'abc123def', Act: shift by 1, Assert: letters shifted, numbers unchanged."""
        result = caesar_cipher('abc123def', 1)
        self.assertEqual(result, 'bcd123efg')

    def test_mixed_with_spaces_and_punctuation(self):
        """Arrange: 'Hello, World!', Act: shift by 5, Assert: correct transformation."""
        result = caesar_cipher('Hello, World!', 5)
        self.assertEqual(result, 'Mjqqt, Btwqi!')

    def test_complex_mixed_input(self):
        """Arrange: complex string with all character types, Act: shift by 13, Assert: correct."""
        result = caesar_cipher('The quick brown fox! 123', 13)
        self.assertEqual(result, 'Gur dhvpx oebja sbk! 123')

    def test_mixed_upper_lower_wrap_around(self):
        """Arrange: 'aXyZ', Act: shift by 1, Assert: case preserved with wrapping."""
        result = caesar_cipher('aXyZ', 1)
        self.assertEqual(result, 'bYzA')

    # Region: Edge Cases and Additional Coverage
    def test_empty_string(self):
        """Arrange: empty string, Act: apply cipher, Assert: still empty."""
        result = caesar_cipher('', 5)
        self.assertEqual(result, '')

    def test_single_character_lowercase(self):
        """Arrange: 'a', Act: shift by 5, Assert: 'f'."""
        result = caesar_cipher('a', 5)
        self.assertEqual(result, 'f')

    def test_single_character_uppercase(self):
        """Arrange: 'A', Act: shift by 5, Assert: 'F'."""
        result = caesar_cipher('A', 5)
        self.assertEqual(result, 'F')

    def test_single_non_letter(self):
        """Arrange: '!', Act: apply cipher, Assert: unchanged."""
        result = caesar_cipher('!', 5)
        self.assertEqual(result, '!')

    def test_negative_shift_lowercase(self):
        """Arrange: 'bcd', Act: shift by -1, Assert: 'abc'."""
        result = caesar_cipher('bcd', -1)
        self.assertEqual(result, 'abc')

    def test_negative_shift_uppercase(self):
        """Arrange: 'BCD', Act: shift by -1, Assert: 'ABC'."""
        result = caesar_cipher('BCD', -1)
        self.assertEqual(result, 'ABC')

    def test_negative_shift_with_wrapping(self):
        """Arrange: 'abc', Act: shift by -1, Assert: wraps to 'zab'."""
        result = caesar_cipher('abc', -1)
        self.assertEqual(result, 'zab')

    def test_negative_shift_greater_than_26(self):
        """Arrange: 'abc', Act: shift by -27, Assert: equivalent to shift by -1."""
        result = caesar_cipher('abc', -27)
        self.assertEqual(result, 'zab')

    def test_full_alphabet_lowercase(self):
        """Arrange: full lowercase alphabet, Act: shift by 1, Assert: shifted alphabet."""
        result = caesar_cipher('abcdefghijklmnopqrstuvwxyz', 1)
        self.assertEqual(result, 'bcdefghijklmnopqrstuvwxyza')

    def test_full_alphabet_uppercase(self):
        """Arrange: full uppercase alphabet, Act: shift by 1, Assert: shifted alphabet."""
        result = caesar_cipher('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1)
        self.assertEqual(result, 'BCDEFGHIJKLMNOPQRSTUVWXYZA')

    def test_real_world_example_1(self):
        """Arrange: 'The quick brown fox', Act: shift by 3, Assert: 'Wkh txlfn eurzq ira'."""
        result = caesar_cipher('The quick brown fox', 3)
        self.assertEqual(result, 'Wkh txlfn eurzq ira')

    def test_real_world_example_2(self):
        """Arrange: 'secretmessage', Act: shift by 5, Assert: 'xjhwjyrjxxflj'."""
        result = caesar_cipher('secretmessage', 5)
        self.assertEqual(result, 'xjhwjyrjxxflj')


if __name__ == '__main__':
    unittest.main()
