"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the
primes below two million.
"""
import math
from support import is_prime


def summation_of_primes():
    sum_of_primes = 2
    count = 3

    while count < 2000000:
        if is_prime(count):
            sum_of_primes += count
        count += 2

    return sum_of_primes


print(summation_of_primes())
