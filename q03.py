"""
The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime
factor of the number 600851475143?
"""


def largest_prime_factor(num):
    """
    Quick & efficient way to find factors is to keep dividing the number by its
    lowest divisor. The loop will terminate when the number cannot be divided
    by any more divisors (i.e. it is the largest prime factor)
    """
    divisor = 2

    while divisor < num:
        if num % divisor == 0:
            num /= divisor
        else:
            divisor += 1

    return num


print(largest_prime_factor(600851475143))
