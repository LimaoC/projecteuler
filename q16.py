"""2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26. What is
the sum of the digits of the number 2^1000?
"""
def main():
    num = 2 ** 1000
    sum_of_digits = 0
    num_to_str = str(num)
    num_to_list = list(num_to_str)

    for i in num_to_list:
        sum_of_digits += int(i)

    return sum_of_digits


print(main())
