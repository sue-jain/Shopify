
def recursive_multiply(x, y):
    """
    Calculates the product of two positive integers x and y using recursion
    without using the multiplication operator (*).

    Args:
        x (int): The first positive integer.
        y (int): The second positive integer.

    Returns:
        int: The product of x and y.

    Raises:
        ValueError: If x or y are not positive integers.
    """
    if not isinstance(x, int) or not isinstance(y, int) or x < 0 or y < 0:
        raise ValueError("Both x and y must be non-negative integers.")

    # Base case: if y is 0, the product is 0
    if y == 0:
        return 0
    # Recursive step: add x to the product of x and (y-1)
    else:
        return x + recursive_multiply(x, y - 1)
