
def fizzbuzz(n):
    """
    This function takes an integer and returns a string according to the FizzBuzz rules.
    """
    if n % 15 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    if n % 5 == 0:
        return "Buzz"
    return str(n)
