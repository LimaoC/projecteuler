"""
n! means n × (n − 1) × ... × 3 × 2 × 1. For example, 10! = 10 × 9 × ... × 3 × 2
× 1 = 3628800, and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8
+ 0 + 0 = 27. Find the sum of the digits in the number 100!
"""

import math

NUMBER = math.factorial(100)
to_str = str(NUMBER)
sum_digits = 0

for i in to_str:
    sum_digits += int(i)

print(sum_digits)
