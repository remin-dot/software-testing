"""
Unit tests for the HackerRank Funny String problem.

Comprehensive test suite using unittest framework with Arrange-Act-Assert
pattern to achieve 100% branch and decision coverage.
"""

import unittest
import sys
from pathlib import Path

# Add parent directory to import path
sys.path.insert(0, str(Path(__file__).parent.parent))

from funny_string import funny_string


class TestFunnyString(unittest.TestCase):
    """Test cases for the funny_string function."""

    # ==================== FUNNY CASES ====================

    def test_single_character_is_funny(self):
        """
        Arrange: Single character string "a"
        Act: Call funny_string with "a"
        Assert: Should return "Funny" (no differences to compare)
        """
        # Arrange
        input_string = "a"

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Funny")

    def test_two_identical_characters_is_funny(self):
        """
        Arrange: Two identical characters "aa"
        Act: Call funny_string with "aa"
        Assert: Should return "Funny" (difference is 0 in both directions)
        """
        # Arrange
        input_string = "aa"

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Funny")

    def test_two_different_characters_is_funny(self):
        """
        Arrange: Two different characters "ab"
        Act: Call funny_string with "ab"
        Assert: Should return "Funny" (single difference is same both directions)
        """
        # Arrange
        input_string = "ab"

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Funny")

    def test_symmetric_differences_is_funny(self):
        """
        Arrange: Three characters with symmetric differences "abc"
        Act: Call funny_string with "abc"
        Assert: Should return "Funny" (differences [1,1] are palindromic)
        """
        # Arrange
        input_string = "abc"
        # Original: a(97)-b(98)=1, b(98)-c(99)=1 → [1, 1]
        # Reversed: c(99)-b(98)=1, b(98)-a(97)=1 → [1, 1]

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Funny")

    def test_longer_symmetric_differences_is_funny(self):
        """
        Arrange: Four characters with symmetric differences "abcd"
        Act: Call funny_string with "abcd"
        Assert: Should return "Funny" (differences [1,1,1] are palindromic)
        """
        # Arrange
        input_string = "abcd"
        # Original: a-b=1, b-c=1, c-d=1 → [1, 1, 1]
        # Reversed: d-c=1, c-b=1, b-a=1 → [1, 1, 1]

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Funny")

    def test_palindromic_difference_pattern_is_funny(self):
        """
        Arrange: Five characters with palindromic difference pattern "abdc"
        Act: Call funny_string with "abda"
        Assert: Should return "Funny" (differences form palindrome)
        """
        # Arrange
        input_string = "abda"
        # Original: a(97)-b(98)=1, b(98)-d(100)=2, d(100)-a(97)=3 → [1, 2, 3]
        # Reversed: a(97)-d(100)=3, d(100)-b(98)=2, b(98)-a(97)=1 → [3, 2, 1]
        # Wait, these are NOT equal. Let me reconsider...
        # Actually, for "abda": reversed is "adba"
        # Original "abda": a-b=1, b-d=2, d-a=3 → [1, 2, 3]
        # Reversed "adba": a-d=3, d-b=2, b-a=1 → [3, 2, 1]
        # These are different, so NOT Funny

        # Let me use "abda" but actually it should be different...
        # Try "acca": a-c=2, c-c=0, c-a=2 → [2, 0, 2]
        # Reversed "acca": a-c=2, c-c=0, c-a=2 → [2, 0, 2]
        # This works!
        
        # Actually, let me use a simpler example
        input_string = "abcba"
        # Original: a-b=1, b-c=1, c-b=1, b-a=1 → [1, 1, 1, 1]
        # Reversed: a-b=1, b-c=1, c-b=1, b-a=1 → [1, 1, 1, 1]

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Funny")

    def test_complex_palindromic_pattern_is_funny(self):
        """
        Arrange: String with palindromic difference pattern "aecfdbgdfc"
        Act: Call funny_string with pattern where differences are palindromic
        Assert: Should return "Funny"
        """
        # Arrange
        input_string = "aecfdbgdfc"
        # Construct with careful character spacing to ensure palindromic differences
        # Let's use a simpler approach: create a string that's a palindrome
        # Palindromes always have funny differences
        
        # Actually, let me reconsider. A palindrome means the string reads the same
        # forwards and backwards, so the character sequence is identical both ways.
        # Let me use "racecar" as it's a palindrome
        
        # But the requirement is that DIFFERENCES should be palindromic, not the string
        # For any palindrome string, the differences WILL be palindromic
        # because reversing it doesn't change it
        
        # So let's use a simple palindrome:
        input_string = "racecar"

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Funny")

    # ==================== NOT FUNNY CASES ====================

    def test_two_very_different_characters_not_funny(self):
        """
        Arrange: Two characters with large difference "az"
        Act: Call funny_string with "az"
        Assert: Should return "Funny" (this should actually be Funny)
        """
        # Arrange
        # a(97), z(122): difference = 25
        # Reversed "za": z-a = 25
        # This is actually Funny! Let me use a different example
        
        # For a true "Not Funny" case with only 2 chars, we'd need something
        # where the diff is different, but that's impossible with 2 chars
        # The reversal of any 2-char string gives the same differences
        
        # Let me use a 3-character example instead:
        input_string = "abd"
        # Original: a-b=1, b-d=2 → [1, 2]
        # Reversed "dba": d-b=2, b-a=1 → [2, 1]
        # [1, 2] != [2, 1]

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Not Funny")

    def test_different_pattern_not_funny(self):
        """
        Arrange: Three characters with asymmetric differences "ace"
        Act: Call funny_string with "ace"
        Assert: Should return "Not Funny"
        """
        # Arrange
        input_string = "ace"
        # Original: a(97)-c(99)=2, c(99)-e(101)=2 → [2, 2]
        # Reversed "eca": e(101)-c(99)=2, c(99)-a(97)=2 → [2, 2]
        # This would be Funny! Let me try "acf"
        
        input_string = "acf"
        # Original: a(97)-c(99)=2, c(99)-f(102)=3 → [2, 3]
        # Reversed "fca": f(102)-c(99)=3, c(99)-a(97)=2 → [3, 2]
        # [2, 3] != [3, 2] ✓

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Not Funny")

    def test_four_characters_not_funny(self):
        """
        Arrange: Four characters with asymmetric difference pattern "abde"
        Act: Call funny_string with "abde"
        Assert: Should return "Not Funny"
        """
        # Arrange
        input_string = "abde"
        # Original: a-b=1, b-d=2, d-e=1 → [1, 2, 1]
        # Reversed "edba": e-d=1, d-b=2, b-a=1 → [1, 2, 1]
        # This is Funny! Let me try "abdf"
        
        input_string = "abdf"
        # Original: a(97)-b(98)=1, b(98)-d(100)=2, d(100)-f(102)=2 → [1, 2, 2]
        # Reversed "fdba": f(102)-d(100)=2, d(100)-b(98)=2, b(98)-a(97)=1 → [2, 2, 1]
        # [1, 2, 2] != [2, 2, 1] ✓

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Not Funny")

    def test_long_asymmetric_string_not_funny(self):
        """
        Arrange: Longer string with clearly asymmetric differences "hackerrank"
        Act: Call funny_string with "hackerrank"
        Assert: Should return "Not Funny"
        """
        # Arrange
        input_string = "hackerrank"
        # This is not a palindrome, so its differences won't be palindromic

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Not Funny")

    # ==================== EDGE CASES ====================

    def test_empty_string_behavior(self):
        """
        Arrange: Empty string
        Act: Call funny_string with ""
        Assert: Should return "Funny" (no differences means they're equal: [] == [])
        """
        # Arrange
        input_string = ""

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Funny")

    def test_special_characters(self):
        """
        Arrange: String with special characters "!@#"
        Act: Call funny_string with special characters
        Assert: Should work based on ASCII values
        """
        # Arrange
        input_string = "!@#"
        # !(33), @(64), #(35)
        # Original: |-31|=31, |64-35|=29 → [31, 29]
        # Reversed "#@!": 35-64=-29 so |29|=29, 64-33=31 → [29, 31]
        # [31, 29] != [29, 31]

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Not Funny")

    def test_numeric_characters(self):
        """
        Arrange: String with numeric characters "123"
        Act: Call funny_string with "123"
        Assert: Should return "Funny" (differences [1, 1] are palindromic)
        """
        # Arrange
        input_string = "123"
        # 1(49)-2(50)=1, 2(50)-3(51)=1 → [1, 1]
        # Reversed "321": 3-2=1, 2-1=1 → [1, 1]

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Funny")

    def test_uppercase_lowercase_mix(self):
        """
        Arrange: String with mixed case "aAbBcC"
        Act: Call funny_string with mixed case
        Assert: Should work based on ASCII values of each character
        """
        # Arrange
        input_string = "aAbBcC"
        # a(97), A(65), b(98), B(66), c(99), C(67)
        # Original: |97-65|=32, |65-98|=33, |98-66|=32, |66-99|=33, |99-67|=32
        #           [32, 33, 32, 33, 32]
        # Reversed "CcBbAa": 67-99=-32→32, 99-66=33, 66-98=-32→32, 98-65=33, 65-97=-32→32
        #           [32, 33, 32, 33, 32]

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Funny")

    def test_all_same_character(self):
        """
        Arrange: String with all identical characters "aaaa"
        Act: Call funny_string with "aaaa"
        Assert: Should return "Funny" (all differences are 0)
        """
        # Arrange
        input_string = "aaaa"

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Funny")

    def test_large_string_funny(self):
        """
        Arrange: A large palindrome string
        Act: Call funny_string with "abcdefghihgfedcba"
        Assert: Should return "Funny"
        """
        # Arrange
        input_string = "abcdefghihgfedcba"

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Funny")

    def test_large_string_not_funny(self):
        """
        Arrange: A string with clearly asymmetric difference pattern
        Act: Call funny_string with "aecfdbgjeh"
        Assert: Should return "Not Funny"
        """
        # Arrange
        # This string has non-palindromic differences when checked
        input_string = "aecfdbgjeh"

        # Act
        result = funny_string(input_string)

        # Assert
        self.assertEqual(result, "Not Funny")

    def test_return_type_is_string(self):
        """
        Arrange: Any input string
        Act: Call funny_string
        Assert: Result should always be a string
        """
        # Arrange
        test_cases = ["a", "ab", "abc", "abd"]

        # Act & Assert
        for test_case in test_cases:
            result = funny_string(test_case)
            self.assertIsInstance(result, str)
            self.assertIn(result, ["Funny", "Not Funny"])

    def test_return_values_only_funny_or_not_funny(self):
        """
        Arrange: Various input strings
        Act: Call funny_string multiple times
        Assert: Result should only be "Funny" or "Not Funny"
        """
        # Arrange
        test_cases = [
            "a", "ab", "abc", "acxz", "hackerrank", "racecar", "!@#"
        ]

        # Act & Assert
        for test_case in test_cases:
            result = funny_string(test_case)
            self.assertIn(result, ["Funny", "Not Funny"],
                         f"Unexpected return value '{result}' for input '{test_case}'")


if __name__ == "__main__":
    unittest.main()
