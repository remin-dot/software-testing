import sys
from pathlib import Path

# Add parent directory to path to allow importing staircase module
sys.path.insert(0, str(Path(__file__).parent.parent))

import unittest
from staircase import staircase


class TestStaircase(unittest.TestCase):
    def test_valid_cases_table(self):
        cases = [
            (1, "#", "#"),
            (2, "*", " " * 1 + "*" + "\n" + "**"),
            (4, "#", "\n".join([
                " " * 3 + "#",
                " " * 2 + "##",
                " " * 1 + "###",
                "####",
            ])),
            (3, "ab", "\n".join([
                " " * 2 + "ab",
                " " * 1 + "abab",
                "ababab",
            ])),
        ]

        for n, pattern, expected in cases:
            with self.subTest(n=n, pattern=pattern):
                # Arrange
                # Act
                result = staircase(n, pattern)
                # Assert
                self.assertEqual(result, expected)

    def test_max_n_30(self):
        # Arrange
        n = 30
        pattern = "*"
        # Act
        result = staircase(n, pattern)
        # Assert
        lines = result.splitlines()
        self.assertEqual(len(lines), 30)
        self.assertEqual(lines[-1], "*" * 30)
        self.assertEqual(lines[0], " " * 29 + "*")

    def test_invalid_cases_table(self):
        cases = [
            (0, "#", ValueError),
            (-1, "#", ValueError),
            (31, "#", ValueError),
            (2.5, "#", TypeError),
            (2, 5, TypeError),
            (2, "", ValueError),
        ]

        for n, pattern, exc in cases:
            with self.subTest(n=n, pattern=pattern):
                # Arrange / Act / Assert
                with self.assertRaises(exc):
                    staircase(n, pattern)


if __name__ == "__main__":
    unittest.main()
