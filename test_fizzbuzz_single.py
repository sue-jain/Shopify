
import pytest
from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("input_val, expected_val", [
    (1, "1"),
    (2, "2"),
    (3, "Fizz"),
    (4, "4"),
    (5, "Buzz"),
    (6, "Fizz"),
    (10, "Buzz"),
    (15, "FizzBuzz"),
    (30, "FizzBuzz"),
])
def test_fizzbuzz_single(input_val, expected_val):
    """A single, parameterized test for the fizzbuzz function."""
    assert fizzbuzz(input_val) == expected_val
