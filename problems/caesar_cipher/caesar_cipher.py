"""Caesar Cipher implementation.

This module provides functionality to shift alphabet characters in a string
by a fixed amount (the cipher key), while preserving case and leaving
non-alphabetic characters unchanged.
"""


def caesar_cipher(s: str, k: int) -> str:
    """Shift each alphabetic character in the string by k positions.
    
    Arguments:
        s: The input string to encode with the Caesar cipher.
        k: The shift amount. Can be any integer, including values > 26.
           Positive values shift forward, negative values shift backward.
    
    Returns:
        The cipher text with each alphabetic character shifted by k positions.
        Uppercase letters remain uppercase, lowercase letters remain lowercase.
        Non-alphabetic characters are unchanged.
        The shift wraps around the alphabet (e.g., 'z' shifted by 1 becomes 'a').
    
    Examples:
        >>> caesar_cipher('abc', 1)
        'bcd'
        >>> caesar_cipher('xyz', 1)
        'yza'
        >>> caesar_cipher('Hello World!', 5)
        'Mjqqt Btwqi!'
        >>> caesar_cipher('abc', 26)
        'abc'
        >>> caesar_cipher('abc', 27)
        'bcd'
    """
    result = []
    
    # Normalize k to be within 0-25 range
    k = k % 26
    
    for char in s:
        if char.isalpha():
            # Determine the base (65 for uppercase, 97 for lowercase)
            base = ord('A') if char.isupper() else ord('a')
            # Convert char to 0-25, apply shift, wrap around, convert back
            shifted = (ord(char) - base + k) % 26
            result.append(chr(base + shifted))
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    
    return ''.join(result)
