
import pytest
from recursive_multiplication import recursive_multiply

def test_positive_integers():
    assert recursive_multiply(5, 3) == 15
    assert recursive_multiply(7, 0) == 0
    assert recursive_multiply(0, 10) == 0
    assert recursive_multiply(1, 1) == 1
    assert recursive_multiply(10, 5) == 50

def test_large_numbers():
    assert recursive_multiply(100, 20) == 2000
    assert recursive_multiply(20, 100) == 2000

def test_invalid_input_negative():
    with pytest.raises(ValueError, match="Both x and y must be non-negative integers."):
        recursive_multiply(-5, 3)
    with pytest.raises(ValueError, match="Both x and y must be non-negative integers."):
        recursive_multiply(5, -3)
    with pytest.raises(ValueError, match="Both x and y must be non-negative integers."):
        recursive_multiply(-5, -3)

def test_invalid_input_non_integer():
    with pytest.raises(ValueError, match="Both x and y must be non-negative integers."):
        recursive_multiply(5.5, 3)
    with pytest.raises(ValueError, match="Both x and y must be non-negative integers."):
        recursive_multiply(5, 3.0)
    with pytest.raises(ValueError, match="Both x and y must be non-negative integers."):
        recursive_multiply("a", 3)

