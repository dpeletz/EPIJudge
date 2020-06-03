from test_framework import generic_test


def power(x: float, y: int) -> float:
    result, exp = 1.0, y

    if y < 0:
        exp, x = -exp, 1.0/x

    while exp:
        if exp & 1:
            result *= x
        x, exp = x * x, exp >> 1
    return result

if __name__ == '__main__':
    exit(generic_test.generic_test_main('power_x_y.py', 'power_x_y.tsv',
                                        power))
