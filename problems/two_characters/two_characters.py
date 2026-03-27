"""
HackerRank "Two Characters" Problem

Remove characters from a string so the result contains exactly two distinct
characters alternating, returning the maximum possible length.
"""


def two_characters(s: str) -> int:
    """
    Remove characters from string so result contains exactly two distinct 
    characters alternating, returning the maximum possible length.
    
    The goal is to keep only two different characters from the input string
    such that they alternate throughout (no two consecutive identical characters)
    and the length is maximized.
    
    Args:
        s: Input string containing characters to remove.
        
    Returns:
        Maximum length of valid alternating string with exactly two distinct 
        characters, or 0 if no such string exists.
        
    Examples:
        >>> two_characters("abacabad")
        4  # "abab" or "acac"
        >>> two_characters("aaa")
        0  # Only one unique character
        >>> two_characters("aaabbbcd")
        0  # No pair of characters can alternate
        >>> two_characters("abcd")
        0  # Each pair appears only once
    """
    # Edge cases: empty string or single character
    if not s or len(s) < 2:
        return 0
    
    max_length = 0
    unique_chars = set(s)
    
    # Try all possible pairs of characters
    chars_list = list(unique_chars)
    for i in range(len(chars_list)):
        for j in range(i + 1, len(chars_list)):
            char1, char2 = chars_list[i], chars_list[j]
            
            # Filter string to keep only these two characters
            filtered = ''.join(c for c in s if c in {char1, char2})
            
            # Check if filtered string is a valid alternating sequence
            if _is_alternating(filtered):
                max_length = max(max_length, len(filtered))
    
    return max_length


def _is_alternating(s: str) -> bool:
    """
    Check if string contains exactly two distinct characters alternating.
    
    A valid alternating string has:
    - Exactly two distinct characters
    - No two consecutive characters are identical
    
    Args:
        s: String to validate.
        
    Returns:
        True if string alternates between exactly two characters, False otherwise.
    """
    # Must have at least 2 characters to be alternating
    if len(s) < 2:
        return False
    
    # Must have exactly 2 distinct characters
    if len(set(s)) != 2:
        return False
    
    # Check if characters alternate (no consecutive duplicates)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    
    return True
