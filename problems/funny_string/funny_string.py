"""
HackerRank Funny String Problem Module

A string is considered "Funny" if the absolute differences between adjacent 
ASCII values in the original string match those in the reversed string.
"""


def funny_string(s: str) -> str:
    """
    Determine if a string is "Funny" or "Not Funny".

    A string is "Funny" if the sequence of absolute differences between 
    adjacent ASCII character values is identical in both the original and 
    reversed string.

    Algorithm:
    1. Calculate ASCII differences between adjacent characters in original string
    2. Calculate ASCII differences between adjacent characters in reversed string
    3. Compare both difference sequences
    4. Return "Funny" if equal, "Not Funny" otherwise

    Args:
        s: The input string to check (should be non-empty).

    Returns:
        str: "Funny" if the difference sequences match, "Not Funny" otherwise.

    Examples:
        >>> funny_string("acxz")
        'Not Funny'
        >>> funny_string("abc")
        'Funny'
        >>> funny_string("a")
        'Funny'
    """
    # Compute differences between adjacent characters in original string
    original_diffs = []
    for i in range(len(s) - 1):
        diff = abs(ord(s[i]) - ord(s[i + 1]))
        original_diffs.append(diff)

    # Compute differences between adjacent characters in reversed string
    reversed_s = s[::-1]
    reversed_diffs = []
    for i in range(len(reversed_s) - 1):
        diff = abs(ord(reversed_s[i]) - ord(reversed_s[i + 1]))
        reversed_diffs.append(diff)

    # Compare the two difference lists
    if original_diffs == reversed_diffs:
        return "Funny"
    else:
        return "Not Funny"
