"""
Unit tests for the cat_and_mouse module.

This test suite implements comprehensive test coverage for the cat_and_mouse function
using the unittest framework and the Arrange-Act-Assert (AAA) pattern.

Test coverage includes:
- Cat A wins (closer to mouse)
- Cat B wins (closer to mouse)
- Mouse C wins (equal distance)
- Boundary value testing (min and max values)
- Various position combinations
"""

import sys
import os
from pathlib import Path

# Add parent directory to path so we can import cat_mouse
sys.path.insert(0, str(Path(__file__).parent.parent))

import unittest
from cat_mouse import cat_and_mouse


class TestCatAndMouse(unittest.TestCase):
    """Test suite for the cat_and_mouse function."""

    # ========== Cat A Wins Test Cases ==========
    def test_cat_a_wins_basic(self):
        """Test: Cat A is closer than Cat B to the mouse."""
        # Arrange
        cat_a = 1
        cat_b = 4
        mouse = 2

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat A")

    def test_cat_a_wins_reversed_positions(self):
        """Test: Cat A wins with mouse between cats (Cat A right side)."""
        # Arrange
        cat_a = 2
        cat_b = 1
        mouse = 3

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat A")

    def test_cat_a_wins_mouse_left(self):
        """Test: Cat A wins with mouse to the left of both cats."""
        # Arrange
        cat_a = 8
        cat_b = 10
        mouse = 2

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat A")

    def test_cat_a_wins_much_closer(self):
        """Test: Cat A wins with significant distance difference."""
        # Arrange
        cat_a = 5
        cat_b = 50
        mouse = 10

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat A")

    def test_cat_a_wins_boundary_low(self):
        """Test: Cat A wins at lower boundary (z=1)."""
        # Arrange
        cat_a = 2
        cat_b = 5
        mouse = 1

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat A")

    def test_cat_a_wins_boundary_high(self):
        """Test: Cat A wins at upper boundary (z=100)."""
        # Arrange
        cat_a = 99
        cat_b = 95
        mouse = 100

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat A")

    def test_cat_a_at_mouse_position(self):
        """Test: Cat A wins when Cat A is at mouse position (distance=0)."""
        # Arrange
        cat_a = 50
        cat_b = 60
        mouse = 50

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat A")

    # ========== Cat B Wins Test Cases ==========
    def test_cat_b_wins_basic(self):
        """Test: Cat B is closer than Cat A to the mouse."""
        # Arrange
        cat_a = 4
        cat_b = 1
        mouse = 2

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat B")

    def test_cat_b_wins_reversed_positions(self):
        """Test: Cat B wins with mouse between cats (Cat B right side)."""
        # Arrange
        cat_a = 1
        cat_b = 2
        mouse = 3

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat B")

    def test_cat_b_wins_mouse_right(self):
        """Test: Cat B wins with mouse to the right of both cats."""
        # Arrange
        cat_a = 10
        cat_b = 8
        mouse = 2

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat B")

    def test_cat_b_wins_much_closer(self):
        """Test: Cat B wins with significant distance difference."""
        # Arrange
        cat_a = 50
        cat_b = 5
        mouse = 10

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat B")

    def test_cat_b_wins_boundary_low(self):
        """Test: Cat B wins at lower boundary (z=1)."""
        # Arrange
        cat_a = 5
        cat_b = 2
        mouse = 1

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat B")

    def test_cat_b_wins_boundary_high(self):
        """Test: Cat B wins at upper boundary (z=100)."""
        # Arrange
        cat_a = 95
        cat_b = 99
        mouse = 100

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat B")

    def test_cat_b_at_mouse_position(self):
        """Test: Cat B wins when Cat B is at mouse position (distance=0)."""
        # Arrange
        cat_a = 60
        cat_b = 50
        mouse = 50

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat B")

    # ========== Mouse C Wins Test Cases (Equal Distance) ==========
    def test_mouse_wins_symmetric_positions(self):
        """Test: Mouse wins when both cats are equidistant (symmetric)."""
        # Arrange
        cat_a = 2
        cat_b = 4
        mouse = 3

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Mouse C")

    def test_mouse_wins_cats_equidistant_right(self):
        """Test: Mouse wins with equidistant cats on the right."""
        # Arrange
        cat_a = 7
        cat_b = 9
        mouse = 8

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Mouse C")

    def test_mouse_wins_cats_equidistant_left(self):
        """Test: Mouse wins with equidistant cats on the left."""
        # Arrange
        cat_a = 1
        cat_b = 3
        mouse = 2

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Mouse C")

    def test_mouse_wins_all_same_position(self):
        """Test: Mouse wins when all are at the same position (distance=0)."""
        # Arrange
        cat_a = 50
        cat_b = 50
        mouse = 50

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Mouse C")

    def test_mouse_wins_boundary_at_min(self):
        """Test: Mouse wins with equal distance at boundary (z=1)."""
        # Arrange
        cat_a = 3
        cat_b = 3
        mouse = 1

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Mouse C")

    def test_mouse_wins_boundary_at_max(self):
        """Test: Mouse wins with equal distance at boundary (z=100)."""
        # Arrange
        cat_a = 98
        cat_b = 98
        mouse = 100

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Mouse C")

    def test_mouse_wins_offset_equidistant(self):
        """Test: Mouse wins with cats at different positions but equal distance to mouse."""
        # Arrange
        cat_a = 10
        cat_b = 30
        mouse = 20

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Mouse C")

    def test_mouse_wins_large_distance_equal(self):
        """Test: Mouse wins with equal large distances."""
        # Arrange
        cat_a = 1
        cat_b = 51
        mouse = 26

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Mouse C")

    # ========== Additional Edge Cases and Boundary Tests ==========
    def test_cat_a_boundary_min_positions(self):
        """Test: Cat A wins at minimum boundary values."""
        # Arrange
        cat_a = 1
        cat_b = 2
        mouse = 1

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat A")

    def test_cat_b_boundary_max_positions(self):
        """Test: Cat B wins at maximum boundary values."""
        # Arrange
        cat_a = 100
        cat_b = 98
        mouse = 97

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat B")

    def test_cat_a_large_difference(self):
        """Test: Cat A wins with maximum distance difference."""
        # Arrange
        cat_a = 50
        cat_b = 100
        mouse = 51

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat A")

    def test_cat_b_large_difference(self):
        """Test: Cat B wins with maximum distance difference."""
        # Arrange
        cat_a = 100
        cat_b = 50
        mouse = 49

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat B")

    def test_mid_range_cat_a_wins(self):
        """Test: Cat A wins in mid-range positions."""
        # Arrange
        cat_a = 40
        cat_b = 61
        mouse = 50

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat A")

    def test_mid_range_cat_b_wins(self):
        """Test: Cat B wins in mid-range positions."""
        # Arrange
        cat_a = 61
        cat_b = 40
        mouse = 50

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat B")

    def test_cat_a_wins_off_by_one(self):
        """Test: Cat A wins with off-by-one distance difference."""
        # Arrange
        cat_a = 10
        cat_b = 13
        mouse = 11

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat A")

    def test_cat_b_wins_off_by_one(self):
        """Test: Cat B wins with off-by-one distance difference."""
        # Arrange
        cat_a = 13
        cat_b = 10
        mouse = 11

        # Act
        result = cat_and_mouse(cat_a, cat_b, mouse)

        # Assert
        self.assertEqual(result, "Cat B")


if __name__ == "__main__":
    unittest.main()
