def recursive_multiply(x, y):
    """
    Recursively multiply two positive integers x and y without using the * operator.
    Uses Russian Peasant Multiplication for O(log y) recursion depth.
    Args:
        x (int): First positive integer
        y (int): Second positive integer
    Returns:
        int: Product of x and y
    """
    if y == 0:
        return 0
    if y == 1:
        return x
    if y % 2 == 0:
        return recursive_multiply(x + x, y // 2)
    else:
        return x + recursive_multiply(x, y - 1)

# Unit tests
import unittest

class TestRecursiveMultiply(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(recursive_multiply(2, 3), 6)
        self.assertEqual(recursive_multiply(3, 2), 6)
        self.assertEqual(recursive_multiply(5, 5), 25)
        self.assertEqual(recursive_multiply(1, 10), 10)
        self.assertEqual(recursive_multiply(10, 1), 10)
        self.assertEqual(recursive_multiply(0, 5), 0)
        self.assertEqual(recursive_multiply(5, 0), 0)
    def test_large(self):
        self.assertEqual(recursive_multiply(7, 8), 56)
        self.assertEqual(recursive_multiply(12, 12), 144)
        self.assertEqual(recursive_multiply(100, 3), 300)
    def test_commutativity(self):
        for x in range(0, 10):
            for y in range(0, 10):
                self.assertEqual(recursive_multiply(x, y), recursive_multiply(y, x))
    def test_very_large(self):
        # Should not hit recursion limit
        self.assertEqual(recursive_multiply(123456, 100000), 123456 * 100000)

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False, verbosity=2)

"""
Time Complexity: O(log y) -- The function makes at most log2(y) recursive calls.
Memory Complexity: O(log y) -- Each recursive call adds a new frame to the call stack, so the maximum depth is log2(y).
This is much more efficient and avoids RecursionError for large y.
""" 