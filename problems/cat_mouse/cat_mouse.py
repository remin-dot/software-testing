"""
Cat and Mouse game module.

This module implements a function to determine which cat reaches the mouse first
based on their positions on a number line.
"""


def cat_and_mouse(x, y, z):
    """
    Determine which cat reaches the mouse first.

    Given positions of two cats (A and B) and a mouse (C) on a number line,
    this function calculates which cat is closer and returns the result.

    Args:
        x (int): Position of Cat A. Constraint: 1 ≤ x ≤ 100
        y (int): Position of Cat B. Constraint: 1 ≤ y ≤ 100
        z (int): Position of Mouse C. Constraint: 1 ≤ z ≤ 100

    Returns:
        str: One of the following:
            - "Cat A" if Cat A is closer to the mouse
            - "Cat B" if Cat B is closer to the mouse
            - "Mouse C" if both cats are equidistant from the mouse

    Examples:
        >>> cat_and_mouse(1, 2, 3)
        'Cat A'
        >>> cat_and_mouse(5, 5, 5)
        'Mouse C'
        >>> cat_and_mouse(10, 1, 5)
        'Cat B'
    """
    distance_a = abs(x - z)
    distance_b = abs(y - z)

    if distance_a < distance_b:
        return "Cat A"
    elif distance_b < distance_a:
        return "Cat B"
    else:
        return "Mouse C"
