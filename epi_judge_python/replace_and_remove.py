import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    write_idx, a_count = 0, 0

    # iterate through size chars
    for i in range(size):
        # if the char isn't a "b", then set write_idx element to be i element and increment write_idx
        if s[i] != "b":
            s[write_idx] = s[i]
            # when the char is a "b", write_idx does not get incremented, which means that the "b" will be overwritten
            write_idx += 1
        # if the char is "a", then increment a_count
        if s[i] == "a":
            a_count += 1
    # set cur_idx to be 1 less than write_idx (where a b is)
    cur_idx = write_idx - 1
    # increment write_idx by the number of "a" chars in the string - 1
    write_idx += a_count - 1
    # set final_size to be one more than write_idx
    final_size = write_idx + 1

    # iterate through s backwards
    while cur_idx >= 0:
        # if s[cur_idx] is "a", then we set it and the element below it to be "d" and "d" and then decrement write_idx by 2
        if s[cur_idx] == "a":
            s[write_idx - 1: write_idx + 1] = "dd"
            write_idx -= 2
        # if s[cur_idx] isn't "a", then we set s[write_idx] to be s[cur_idx] (just copy the char) and decrement write_idx
        else:
            s[write_idx] = s[cur_idx]
            write_idx -= 1
        # decrement cur_idx
        cur_idx -= 1

    return final_size

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    # print(replace_and_remove(7, ["c", "c", "d", "d", "a", "a", "a", "", "", "", "", "", "", ""]))
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
