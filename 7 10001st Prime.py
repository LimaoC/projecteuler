"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13. What is the 10 001st prime number?
"""

from support import is_prime


def the_10001st_prime():
    count = 2
    current_num = 3

    while count != 10001:
        current_num += 2

        if is_prime(current_num):
            count += 1
        else:
            continue

    return current_num


print(the_10001st_prime())
