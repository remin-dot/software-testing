"""
Unit tests for the Alternating Characters module.

Tests are organized using the Arrange-Act-Assert (AAA) pattern and
achieve 100% branch coverage of the alternating_characters function.
"""

import unittest
from alternating_characters import alternating_characters


class TestAlternatingCharacters(unittest.TestCase):
    """Test cases for the alternating_characters function."""
    
    # Edge Cases
    def test_empty_string(self):
        """Test with empty string - no deletions needed."""
        # Arrange
        input_string = ""
        expected = 0
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_single_character(self):
        """Test with single character - no deletions needed."""
        # Arrange
        input_string = "a"
        expected = 0
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    # No Deletion Needed Cases
    def test_alternating_pattern_two_chars(self):
        """Test with alternating pattern - no deletions."""
        # Arrange
        input_string = "ab"
        expected = 0
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_alternating_pattern_longer(self):
        """Test with longer alternating pattern - no deletions."""
        # Arrange
        input_string = "ababab"
        expected = 0
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_alternating_pattern_complex(self):
        """Test with complex alternating pattern - no deletions."""
        # Arrange
        input_string = "abcabc"
        expected = 0
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    # All Identical Characters
    def test_two_identical_characters(self):
        """Test with two identical characters - 1 deletion."""
        # Arrange
        input_string = "aa"
        expected = 1
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_all_identical_three(self):
        """Test with three identical characters - 2 deletions."""
        # Arrange
        input_string = "aaa"
        expected = 2
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_all_identical_four(self):
        """Test with four identical characters - 3 deletions."""
        # Arrange
        input_string = "aaaa"
        expected = 3
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_all_identical_long(self):
        """Test with many identical characters - 9 deletions."""
        # Arrange
        input_string = "aaaaaaaaaa"  # 10 'a's
        expected = 9
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    # Mixed Repeating Patterns
    def test_two_groups_identical(self):
        """Test with two groups of identical characters."""
        # Arrange
        input_string = "aabb"
        expected = 2  # 1 deletion for 'aa', 1 deletion for 'bb'
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_mixed_pattern_aabbaa(self):
        """Test with pattern aabbaa - 3 deletions."""
        # Arrange
        input_string = "aabbaa"
        expected = 3  # 1 from first 'aa', 1 from 'bb', 1 from last 'aa'
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_mixed_pattern_aabbaabb(self):
        """Test with pattern aabbaabb - 4 deletions."""
        # Arrange
        input_string = "aabbaabb"
        expected = 4  # 4 groups of pairs, 1 deletion each
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_three_groups(self):
        """Test with three groups of consecutive characters."""
        # Arrange
        input_string = "aaabbbccc"
        expected = 6  # 2 + 2 + 2 = 6 deletions
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    # Complex Cases
    def test_single_then_pair(self):
        """Test with single char followed by pair."""
        # Arrange
        input_string = "abb"
        expected = 1  # 1 deletion for 'bb'
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_pair_then_single(self):
        """Test with pair followed by single char."""
        # Arrange
        input_string = "aab"
        expected = 1  # 1 deletion for 'aa'
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_long_sequence_mixed(self):
        """Test with longer mixed sequence."""
        # Arrange
        input_string = "aaabbb"
        expected = 4  # 2 deletions for 'aaa', 2 deletions for 'bbb'
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_long_sequence_very_long(self):
        """Test with very long sequence."""
        # Arrange
        input_string = "aaaaabbbbb"
        expected = 8  # 4 deletions for 'aaaaa', 4 deletions for 'bbbbb'
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_alternating_with_groups(self):
        """Test with alternating groups of different sizes."""
        # Arrange
        input_string = "aaabbbaaa"
        expected = 6  # 2 + 2 + 2 = 6
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_single_chars_separated_by_pairs(self):
        """Test pattern with alternating singles and pairs."""
        # Arrange
        input_string = "abbacc"
        expected = 2  # 1 deletion for 'bb', 1 deletion for 'cc'
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)
    
    def test_complex_real_world_pattern(self):
        """Test with a complex real-world-like pattern."""
        # Arrange
        input_string = "aaabbaabbbaaa"
        expected = 8  # 2 + 1 + 1 + 2 + 2 = 8
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, expected)


class TestAlternatingCharactersBranchCoverage(unittest.TestCase):
    """
    Specific tests targeting each code branch for 100% coverage.
    """
    
    def test_branch_empty_string(self):
        """Branch: not s (empty string condition)."""
        # Arrange
        input_string = ""
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, 0)
    
    def test_branch_single_char(self):
        """Branch: len(s) <= 1 (single character condition)."""
        # Arrange
        input_string = "x"
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, 0)
    
    def test_branch_if_equal_consecutive(self):
        """Branch: if s[i] == s[i-1] (increment counter)."""
        # Arrange
        input_string = "aaa"  # Triggers the if branch multiple times
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, 2)
    
    def test_branch_else_different_char(self):
        """Branch: else condition (different character, calculate deletions)."""
        # Arrange
        input_string = "aab"  # Triggers else when transitioning from 'a' to 'b'
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, 1)
    
    def test_branch_final_group_processing(self):
        """Branch: final group processing after loop."""
        # Arrange
        input_string = "abb"  # Loop ends on last char being part of 'bb'
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, 1)
    
    def test_branch_multiple_transitions(self):
        """Branch: multiple transitions between if and else."""
        # Arrange
        input_string = "aabbcc"  # Multiple transitions
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, 3)
    
    def test_branch_no_consecutive_identical(self):
        """Branch: loop processes all chars but else is always triggered."""
        # Arrange
        input_string = "abcde"  # Every char is different
        
        # Act
        result = alternating_characters(input_string)
        
        # Assert
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
