"""Staircase pattern generator.

Provides `staircase(n, pattern)` which returns a right-aligned staircase
of height `n` using `pattern` repeated per step.
"""
from typing import List


def staircase(n: int, pattern: str) -> str:
    """
    Generate a right-aligned staircase.

    Args:
        n: Height of the staircase (1..30).
        pattern: Non-empty string used for each stair unit.

    Returns:
        Multi-line string with `n` lines forming a right-aligned staircase.

    Raises:
        TypeError: If `n` is not an int or `pattern` is not a str.
        ValueError: If `n` not in 1..30 or `pattern` is empty.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an int")
    if not isinstance(pattern, str):
        raise TypeError("pattern must be a str")
    if n <= 0 or n > 30:
        raise ValueError("n must be between 1 and 30 inclusive")
    if pattern == "":
        raise ValueError("pattern must be a non-empty string")

    lines: List[str] = []
    for i in range(1, n + 1):
        left_spaces = " " * (n - i)
        line = left_spaces + (pattern * i)
        lines.append(line)
    return "\n".join(lines)
