"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder. What is the smallest positive number that is
evenly divisible by all of the numbers from 1 to 20?

LCM(x, y) = x * y / GCD(x, y) -> 1 * 20 / GCD(1, 20)
LCM(k1, k2, ..., kn) = LCM(...(LCM(LCM(k1, k2), k3)...), kn)
"""

import math


def smallest_multiple():
    num = 1

    for i in range(1, 21):
        num *= i // math.gcd(i, num)

    return num


print(smallest_multiple())
