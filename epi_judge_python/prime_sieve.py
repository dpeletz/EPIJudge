from typing import List

from test_framework import generic_test
import math

# Given n, return all primes up to and including n.
def generate_primes(n: int) -> List[int]:

    def is_prime(input, prev):
        for i in prev:
            if input % i == 0: return False
            if i >= math.sqrt(input): return True
        return True


    if n <= 1: return []
    if n == 2: return [2]

    r_dict = {2: [2], 3: [2, 3], 4: [2, 3], 5: [2, 3, 5]}
    if n in r_dict: return r_dict[n]

    ignore = set()
    for x in range(n // 2):
        ignore.add(2 * x)


    for i in range(6, n+1):
        r_dict[i] = r_dict[i-1]
        if i not in ignore:
            if is_prime(i, r_dict[i]): r_dict[i].append(i)
            else: ignore.add(i * y for y in range(n // i) )

    return r_dict[n]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('prime_sieve.py', 'prime_sieve.tsv',
                                       generate_primes))
