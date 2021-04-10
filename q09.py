"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2. For example, 32 + 42 = 9 + 16 = 25 = 52. There exists exactly
one Pythagorean triplet for which a + b + c = 1000. Find the product abc.
"""


def special_pythagorean_triplet():
    for a in range(1, 1001):
        for b in range(1, 1001):
            c = 1000 - a - b
            if check_pythagorean(a, b, c):
                return a * b * c
            else:
                continue


def check_pythagorean(num1, num2, num3):
    if (num1 ** 2) + (num2 ** 2) == (num3 ** 2):
        return True
    return False


print(special_pythagorean_triplet())
