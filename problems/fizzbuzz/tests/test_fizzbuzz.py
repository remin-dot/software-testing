"""Unit tests for the `fizzbuzz` function.

Tests use Arrange–Act–Assert structure and cover all branches.
"""
import unittest
import os
import sys

# Ensure repository root is on sys.path when running this test file directly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    def test_divisible_by_3_only(self):
        # Arrange
        x = 9
        # Act
        result = fizzbuzz(x)
        # Assert
        self.assertEqual(result, "Fizz")

    def test_divisible_by_5_only(self):
        # Arrange
        x = 10
        # Act
        result = fizzbuzz(x)
        # Assert
        self.assertEqual(result, "Buzz")

    def test_divisible_by_both_3_and_5(self):
        # Arrange
        x = 30
        # Act
        result = fizzbuzz(x)
        # Assert
        self.assertEqual(result, "FizzBuzz")

    def test_not_divisible_by_3_or_5(self):
        # Arrange
        x = 7
        # Act
        result = fizzbuzz(x)
        # Assert
        self.assertEqual(result, "7")

    def test_zero_returns_fizzbuzz(self):
        # Arrange
        x = 0
        # Act
        result = fizzbuzz(x)
        # Assert
        self.assertEqual(result, "FizzBuzz")

    def test_negative_values(self):
        # Arrange
        cases = {
            -3: "Fizz",
            -5: "Buzz",
            -15: "FizzBuzz",
            -2: "-2",
        }
        # Act / Assert
        for x, expected in cases.items():
            with self.subTest(x=x):
                result = fizzbuzz(x)
                self.assertEqual(result, expected)

    def test_boundary_values(self):
        # Arrange
        cases = {
            1: "1",
            -1: "-1",
            2: "2",
            3: "Fizz",
            5: "Buzz",
            15: "FizzBuzz",
        }
        # Act / Assert
        for x, expected in cases.items():
            with self.subTest(x=x):
                result = fizzbuzz(x)
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
