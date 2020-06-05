from test_framework import generic_test
from test_framework.test_failure import TestFailure


def int_to_string(x: int) -> str:
    digits, s, m = "0123456789", "", 1
    if x == 0: return digits[x]

    if x < 0:
        s, x = s + "-", -1 * x
    elif x > 0:
        s = s + "+"

    while m <= x: m *= 10

    m //= 10

    while m >= 1:
        val = x // m
        s, x, m = s + digits[val], x - (m * val), m // 10

    return s


def string_to_int(s: str) -> int:
    digits, sum, sign = "0123456789", 0, 1

    if s[0] == "-":
        sign, s = -1, s[1:]
    if s[0] == "+":
        s = s[1:]

    m = 10 ** (len(s) - 1)

    for i in s:
        sum += m * digits.index(i)
        m = m // 10

    return sign * sum


def wrapper(x, s):
    if int(int_to_string(x)) != x:
        raise TestFailure('Int to string conversion failed')
    if string_to_int(s) != x:
        raise TestFailure('String to int conversion failed')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('string_integer_interconversion.py',
                                       'string_integer_interconversion.tsv',
                                       wrapper))