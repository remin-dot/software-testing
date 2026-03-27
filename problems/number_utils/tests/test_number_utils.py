import os
import sys
import unittest

# Ensure the project root is on sys.path so the test file can be run directly.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from number_utils import is_prime_list


class TestIsPrimeList(unittest.TestCase):
    def test_all_primes(self):
        # Arrange
        numbers = [2, 3, 5, 7, 11]

        # Act
        result = is_prime_list(numbers)

        # Assert
        self.assertTrue(result)

    def test_contains_non_prime(self):
        # Arrange
        numbers = [2, 4, 5]

        # Act
        result = is_prime_list(numbers)

        # Assert
        self.assertFalse(result)

    def test_single_element_prime(self):
        # Arrange
        numbers = [13]

        # Act
        result = is_prime_list(numbers)

        # Assert
        self.assertTrue(result)

    def test_single_element_non_prime(self):
        # Arrange
        numbers = [4]

        # Act
        result = is_prime_list(numbers)

        # Assert
        self.assertFalse(result)

    def test_empty_list(self):
        # Arrange
        numbers = []

        # Act
        result = is_prime_list(numbers)

        # Assert (vacuously True)
        self.assertTrue(result)

    def test_number_one_handling(self):
        # Arrange
        numbers = [1]

        # Act
        result = is_prime_list(numbers)

        # Assert
        self.assertFalse(result)

    def test_large_prime_and_composite(self):
        # Arrange
        large_prime = 10007  # prime
        large_composite = 10007 * 2  # composite with small factor for fast exit

        # Act / Assert
        self.assertTrue(is_prime_list([large_prime]))
        self.assertFalse(is_prime_list([large_composite]))

    def test_mixed_values(self):
        # Arrange
        numbers = [3, 5, 8, 11, 13]

        # Act
        result = is_prime_list(numbers)

        # Assert
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
