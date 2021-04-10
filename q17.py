"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total. If all the numbers
from 1 to 1000 (one thousand) inclusive were written out in words, how many
letters would be used? NOTE: Do not count spaces or hyphens. For example, 342
(three hundred and forty-two) contains 23 letters and 115 (one hundred and
fifteen) contains 20 letters. The use of "and" when writing out numbers is in
compliance with British usage.
"""

ONES = ["", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]
AND = "and"
HUNDRED = "hundred"


def to_words(n):
    if n < 20:
        return ONES[n]
    elif n < 100:
        return TENS[n // 10] + (ONES[n % 10] if (n % 10 != 0) else "")
    elif n < 1000:
        return ONES[n // 100] + HUNDRED + \
            ((AND + to_words(n % 100)) if (n % 100 != 0) else "")
    else:
        return "onethousand"


def main():
    return sum(len(to_words(i)) for i in range(1, 1001))


print(main())
