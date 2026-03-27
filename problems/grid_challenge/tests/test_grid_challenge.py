"""
Unit tests for the Grid Challenge problem.

Uses Arrange-Act-Assert pattern with 100% branch coverage.
"""

import unittest
from grid_challenge import grid_challenge


class TestGridChallenge(unittest.TestCase):
    """Test cases for grid_challenge function."""

    # ========== Valid and Invalid Grid Cases ==========

    def test_valid_grid_example_1(self):
        """Test a valid grid that becomes sorted after row sorting."""
        # Arrange
        grid = ['bac', 'dbc', 'fhg']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    def test_invalid_grid_example_1(self):
        """Test an invalid grid where columns cannot be sorted."""
        # Arrange
        grid = ['zyx', 'abc']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'NO')

    def test_valid_grid_already_sorted_rows(self):
        """Test a grid where rows are already sorted."""
        # Arrange
        grid = ['abc', 'def', 'ghi']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    def test_invalid_grid_columns_conflict(self):
        """Test a grid where sorting rows causes column conflicts."""
        # Arrange
        grid = ['zb', 'az']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'NO')

    # ========== Single Row and Single Column Cases ==========

    def test_single_row(self):
        """Test a grid with only one row."""
        # Arrange
        grid = ['zyx']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    def test_single_row_unsorted(self):
        """Test a single unsorted row (should always return YES)."""
        # Arrange
        grid = ['dcba']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    def test_single_column(self):
        """Test a grid with only one column (single character rows)."""
        # Arrange
        grid = ['a', 'b', 'c']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    def test_single_column_unsorted(self):
        """Test a single column that is not sorted."""
        # Arrange
        grid = ['c', 'a', 'b']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'NO')

    def test_single_element(self):
        """Test a 1x1 grid."""
        # Arrange
        grid = ['a']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    # ========== Already Sorted Grids ==========

    def test_sorted_2x2_grid(self):
        """Test a 2x2 grid that is already sorted."""
        # Arrange
        grid = ['ab', 'cd']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    def test_sorted_3x3_grid(self):
        """Test a 3x3 grid that is already sorted."""
        # Arrange
        grid = ['aaa', 'aaa', 'aaa']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    def test_sorted_diagonal_ascending(self):
        """Test a grid sorted diagonally."""
        # Arrange
        grid = ['aef', 'bgh', 'cij']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    # ========== Edge Cases with Duplicates ==========

    def test_all_same_character(self):
        """Test a grid with all same characters."""
        # Arrange
        grid = ['aaa', 'aaa', 'aaa']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    def test_grid_with_duplicate_rows(self):
        """Test a grid with duplicate rows."""
        # Arrange
        grid = ['abc', 'abc', 'abc']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    def test_duplicate_characters_in_row(self):
        """Test rows with duplicate characters."""
        # Arrange
        grid = ['aab', 'bcc', 'dde']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    def test_duplicate_characters_causing_failure(self):
        """Test duplicate characters that prevent sorting."""
        # Arrange
        grid = ['baa', 'ab', 'aa']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'NO')

    # ========== Larger Grids ==========

    def test_large_valid_grid(self):
        """Test a larger valid grid."""
        # Arrange
        grid = [
            'bac',
            'dbc',
            'fhg'
        ]

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    def test_large_invalid_grid(self):
        """Test a larger invalid grid."""
        # Arrange
        grid = [
            'zzz',
            'aaa',
            'bbb'
        ]

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'NO')

    # ========== Column Comparison Edge Cases ==========

    def test_first_column_fails(self):
        """Test grid where first column comparison fails."""
        # Arrange
        grid = ['zb', 'aa']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'NO')

    def test_middle_column_fails(self):
        """Test grid where middle column comparison fails."""
        # Arrange
        grid = ['adc', 'aeb', 'aft']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'NO')

    def test_last_column_fails(self):
        """Test grid where last column comparison fails."""
        # Arrange
        grid = ['aac', 'abb']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'NO')

    # ========== Branch Coverage Cases ==========

    def test_passes_first_comparison_fails_later(self):
        """Test that passes first row comparison but fails on subsequent rows."""
        # Arrange
        grid = ['cab', 'abc', 'bba']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'NO')

    def test_multiple_passes_before_failure(self):
        """Test multiple column comparisons passing before one fails."""
        # Arrange
        grid = ['aaaz', 'aaay', 'aaax']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'NO')

    def test_all_comparisons_pass(self):
        """Test all comparisons pass with various characters."""
        # Arrange
        grid = ['aef', 'beg', 'cfh']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    # ========== Row Sorting Verification ==========

    def test_unsorted_rows_become_sorted(self):
        """Test that unsorted rows are properly sorted before column check."""
        # Arrange
        grid = ['cba', 'fed', 'ihg']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    def test_partial_row_sorting(self):
        """Test rows that are partially sorted."""
        # Arrange
        grid = ['bac', 'edf', 'ihg']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'YES')

    def test_row_sorting_reveals_problem(self):
        """Test that row sorting reveals column issues."""
        # Arrange
        grid = ['zyx', 'abc']

        # Act
        result = grid_challenge(grid)

        # Assert
        self.assertEqual(result, 'NO')


if __name__ == '__main__':
    unittest.main()
