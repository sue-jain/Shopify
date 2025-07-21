def integer_square_root(k):
    """
    Returns the largest integer whose square is less than or equal to k using binary search.
    Args:
        k (int): A non-negative integer
    Returns:
        int: The integer square root of k
    """
    if k < 0:
        raise ValueError("Input must be a non-negative integer.")
    if k == 0 or k == 1:
        return k
    left, right = 0, k
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= k:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    return ans

# Test cases
if __name__ == "__main__":
    test_cases = [
        (0, 0),
        (1, 1),
        (4, 2),
        (8, 2),
        (9, 3),
        (15, 3),
        (16, 4),
        (17, 4),
        (100, 10),
        (101, 10),
        (2147395599, 46339),  # Large number
        (2**32, 65536),
    ]
    print("Testing integer_square_root:")
    for k, expected in test_cases:
        result = integer_square_root(k)
        print(f"integer_square_root({k}) = {result} (Expected: {expected})", "✓" if result == expected else "✗") 