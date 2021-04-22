import math


def is_prime(number: int) -> bool:
    """
    Checks if number is prime

    Parameters:
        number (int): number to be checked

    Returns:
        (bool): True if number is prime, False otherwise
    """
    for i in range(2, math.floor(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True
