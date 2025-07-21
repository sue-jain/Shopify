import pytest
from str_to_int_converter import str_to_int

def test_positive_numbers():
    assert str_to_int("0") == 0
    assert str_to_int("1") == 1
    assert str_to_int("123") == 123
    assert str_to_int("98765") == 98765
    assert str_to_int("+123") == 123
    assert str_to_int("+0") == 0

def test_negative_numbers():
    assert str_to_int("-1") == -1
    assert str_to_int("-123") == -123
    assert str_to_int("-98765") == -98765

def test_large_numbers():
    assert str_to_int("12345678901234567890") == 12345678901234567890
    assert str_to_int("-98765432109876543210") == -98765432109876543210

def test_invalid_input_type():
    with pytest.raises(TypeError, match="Input must be a string."):
        str_to_int(123)
    with pytest.raises(TypeError, match="Input must be a string."):
        str_to_int(None)
    with pytest.raises(TypeError, match="Input must be a string."):
        str_to_int(["1", "2"])

def test_empty_string():
    with pytest.raises(ValueError, match="Input string cannot be empty."):
        str_to_int("")

def test_non_numeric_characters():
    with pytest.raises(ValueError, match="Input string contains non-numeric characters."):
        str_to_int("123a")
    with pytest.raises(ValueError, match="Input string contains non-numeric characters."):
        str_to_int("abc")
    with pytest.raises(ValueError, match="Input string contains non-numeric characters."):
        str_to_int("1.23")
    with pytest.raises(ValueError, match="Input string contains non-numeric characters."):
        str_to_int("--123")
    with pytest.raises(ValueError, match="Input string contains non-numeric characters."):
        str_to_int("++123")
    with pytest.raises(ValueError, match="Input string contains non-numeric characters."):
        str_to_int("-+123")

def test_sign_only_string():
    with pytest.raises(ValueError, match="Input string contains only a sign character."):
        str_to_int("-")
    with pytest.raises(ValueError, match="Input string contains only a sign character."):
        str_to_int("+")