from test_framework import generic_test


def reverse(x: int) -> int:
    # MY VERSION:

    # mult, r_val, max_place, values = 1, 0, 1, []
    #
    # if x == 0: return x
    # if x < 0: mult, x = -mult, -x
    #
    # while max_place <= x:
    #     max_place *= 10
    #
    # max_place /= 10
    # head = max_place
    #
    # while max_place >= 1:
    #     values.append(x // max_place)
    #     x, max_place = x - ((x // max_place) * max_place), max_place / 10
    #
    # for i in values[::-1]:
    #     r_val += (head * i)
    #     head /= 10
    #
    # return int(mult * r_val)

    # CONCISE VERSION:
    result, x_remaining = 0, abs(x)

    while x_remaining:
        # multiplies result my 10 and adds modulo of x_remaining and 10
        result = result * 10 + (x_remaining % 10)
        # integer divides x_remaining by 10
        x_remaining //= 10
    return -result if x < 0 else result


if __name__ == '__main__':
    # print(reverse(15))
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
