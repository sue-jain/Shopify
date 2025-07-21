
import pytest
from is_unique_string import is_unique

def test_unique_characters():
    assert is_unique("abcdefg") == True
    assert is_unique("abc def") == True
    assert is_unique("aBcDeFg") == True  # Case-insensitive
    assert is_unique(" ") == True
    assert is_unique("a") == True
    assert is_unique("") == True  # Empty string has unique characters

def test_non_unique_characters():
    assert is_unique("hello") == False
    assert is_unique("apple") == False
    assert is_unique("programming") == False
    assert is_unique("a b c a") == False  # Duplicate space
    assert is_unique("Aa") == False  # Case-insensitive duplicate

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a string."):
        is_unique(123)
    with pytest.raises(TypeError, match="Input must be a string."):
        is_unique(None)
    with pytest.raises(TypeError, match="Input must be a string."):
        is_unique(["a", "b"])

def test_invalid_input_characters():
    with pytest.raises(ValueError, match="Input string must contain only alphabets or spaces."):
        is_unique("abc123")
    with pytest.raises(ValueError, match="Input string must contain only alphabets or spaces."):
        is_unique("abc!")
    with pytest.raises(ValueError, match="Input string must contain only alphabets or spaces."):
        is_unique("abc-")

