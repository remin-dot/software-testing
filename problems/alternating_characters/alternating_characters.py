"""
HackerRank: Alternating Characters

Determine the minimum number of character deletions required so that
no two adjacent characters in the resulting string are the same.
"""


def alternating_characters(s: str) -> int:
    """
    Calculate the minimum number of deletions needed to ensure no two
    adjacent characters in the string are identical.
    
    The approach counts consecutive identical characters. For each group
    of n consecutive identical characters, we need n-1 deletions to reduce
    them to a single character.
    
    Args:
        s: A string of lowercase English letters
        
    Returns:
        The minimum number of character deletions needed to make all
        adjacent characters different
        
    Examples:
        >>> alternating_characters("aaaa")
        3
        >>> alternating_characters("ababab")
        0
        >>> alternating_characters("aabbaa")
        2
    """
    # Handle edge cases: empty string or single character
    if not s or len(s) <= 1:
        return 0
    
    deletions = 0
    consecutive_count = 1
    
    # Iterate through the string starting from the second character
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            # Current character matches the previous one
            consecutive_count += 1
        else:
            # Current character differs from previous one
            # Add deletions needed for this group of consecutive identical chars
            deletions += consecutive_count - 1
            # Reset counter for the new character
            consecutive_count = 1
    
    # Process the last group of consecutive identical characters
    deletions += consecutive_count - 1
    
    return deletions
