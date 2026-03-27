"""
HackerRank Grid Challenge Solution.

This module determines if a grid can be transformed into a sorted matrix
by sorting each row alphabetically while maintaining column order.
"""


def grid_challenge(grid: list[str]) -> str:
    """
    Determine if a grid can have all columns sorted after sorting each row.

    Algorithm:
    1. Sort each row alphabetically
    2. Check if each column is sorted in ascending order (top to bottom)
    3. Return "YES" if all columns are sorted, "NO" otherwise

    Args:
        grid: A list of strings where each string represents a row of characters.
              Each row has the same length.

    Returns:
        "YES" if all columns are sorted after sorting each row.
        "NO" otherwise.

    Example:
        >>> grid_challenge(['ebacd', 'fomka', 'abcde', 'ghijk'])
        'YES'

        >>> grid_challenge(['abc', 'lmp', 'qrt'])
        'NO'
    """
    # Sort each row alphabetically
    sorted_grid = [sorted(row) for row in grid]

    # Check if each column is sorted
    num_rows = len(sorted_grid)
    num_cols = len(sorted_grid[0]) if num_rows > 0 else 0

    for col in range(num_cols):
        for row in range(num_rows - 1):
            # Compare current character with character below it
            if sorted_grid[row][col] > sorted_grid[row + 1][col]:
                return "NO"

    return "YES"
