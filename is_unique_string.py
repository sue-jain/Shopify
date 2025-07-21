
def is_unique(input_str):
    """
    Determines if a string has all unique characters (case-insensitive, including spaces).

    Args:
        input_str (str): The input string containing only alphabets or spaces.

    Returns:
        bool: True if all characters are unique, False otherwise.
    """
    if not isinstance(input_str, str):
        raise TypeError("Input must be a string.")

    # Use a set to store characters encountered so far
    seen_characters = set()

    # Convert the string to lowercase to handle case-insensitivity
    processed_str = input_str.lower()

    for char in processed_str:
        # Check if the character is an alphabet or a space
        if not ('a' <= char <= 'z' or char == ' '):
            raise ValueError("Input string must contain only alphabets or spaces.")

        if char in seen_characters:
            return False  # Duplicate character found
        seen_characters.add(char)

    return True  # No duplicates found
