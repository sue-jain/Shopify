Build a simple REST endpoint (NodeJS/Express) with a GET and POST methodBuild a simple REST endpoint (NodeJS/Express) with a GET and POST method
import pytest
from fizzbuzz import fizzbuzz

def test_returns_number_as_string():
    """Test that a non-Fizz, non-Buzz number is returned as a string."""
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"

def test_returns_fizz_for_multiples_of_three():
    """Test that "Fizz" is returned for multiples of 3."""
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"

def test_returns_buzz_for_multiples_of_five():
    """Test that "Buzz" is returned for multiples of 5."""
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"

def test_returns_fizzbuzz_for_multiples_of_fifteen():
    """Test that "FizzBuzz" is returned for multiples of 15."""
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
