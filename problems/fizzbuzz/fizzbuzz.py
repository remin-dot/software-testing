"""FizzBuzz module.

Provides a single function `fizzbuzz(x: int) -> str`.
"""


def fizzbuzz(x: int) -> str:
    """Return the FizzBuzz value for `x`.

    Rules:
    - If `x` is divisible by both 3 and 5 return "FizzBuzz".
    - If `x` is divisible by 3 return "Fizz".
    - If `x` is divisible by 5 return "Buzz".
    - Otherwise return the string representation of `x`.

    Args:
        x: Integer value to evaluate. Can be negative or zero.

    Returns:
        A string according to the rules above.
    """
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    if x % 3 == 0:
        return "Fizz"
    if x % 5 == 0:
        return "Buzz"
    return str(x)
