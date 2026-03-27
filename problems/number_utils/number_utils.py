"""Utilities for number checks.

This module provides a function to check whether all numbers in a list
are prime using a straightforward divisibility check from 2 to n-1.
"""
from typing import List


def _is_prime(n: int) -> bool:
    """Return True if ``n`` is a prime number.

    This uses the naive algorithm requested: test divisibility from 2
    up to ``n - 1``. By convention, numbers less than 2 are not prime.
    """
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def is_prime_list(numbers: List[int]) -> bool:
    """Return True if every number in ``numbers`` is prime.

    Behavior:
    - If any element is not prime, return False immediately.
    - If the list is empty, return True (vacuously all prime).

    The function delegates to ``_is_prime`` which applies the requested
    naive divisibility check.
    """
    for n in numbers:
        if not _is_prime(n):
            return False

    return True
