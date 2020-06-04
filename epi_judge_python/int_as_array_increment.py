from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    overflow = 0
    for i in range(len(A) - 1, -1, -1):
        if i == len(A) - 1: A[i] += 1
        A[i] = A[i] + overflow
        if A[i] >= 10:
            A[i] -= 10
            overflow = 1
            print(i)
        else:
            overflow = 0
    if overflow:
        A[0] = 1
        A.append(0)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
