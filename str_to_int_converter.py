
def str_to_int(input_str):
    """
    Converts a numeric string to an integer without using the built-in int() function.

    Args:
        input_str (str): The numeric string to convert.

    Returns:
        int: The integer representation of the string.

    Raises:
        TypeError: If the input is not a string.
        ValueError: If the string is empty or contains non-numeric characters
                    (other than an optional leading '-' or '+').
    """
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string.")

    if not input_str:
        raise ValueError("Input string cannot be empty.")

    result = 0
    sign = 1
    start_index = 0

    # Handle sign
    if input_str[0] == '-':
        sign = -1
        start_index = 1
    elif input_str[0] == '+':
        start_index = 1

    # Check if there are only sign characters after handling sign
    if start_index == len(input_str):
        raise ValueError("Input string contains only a sign character.")

    # Convert digits
    for i in range(start_index, len(input_str)):
        char = input_str[i]
        if '0' <= char <= '9':
            digit = ord(char) - ord('0')
            result = result * 10 + digit
        else:
            raise ValueError("Input string contains non-numeric characters.")

    return result * sign
