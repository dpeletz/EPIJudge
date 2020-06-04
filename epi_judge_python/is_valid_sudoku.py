from typing import List

from test_framework import generic_test


# Check if a partially filled matrix has any conflicts.
def is_valid_sudoku(partial_assignment: List[List[int]]) -> bool:
    def is_valid(input):
        seen = []
        for i in input:
            if i != 0 and i not in seen:
                seen.append(i)
            elif i != 0 and i in seen:
                return False

        return True

    def get_cols(input):
        cols = []
        for j in range(9): cols.append([row[j] for row in input])
        return cols

    def get_sections(input):
        return_list = []
        return_list.extend(get_section(input[:3]))
        return_list.extend(get_section(input[3:6]))
        return_list.extend(get_section(input[6:]))
        return return_list

    def get_section(input):
        subs = [[], [], []]
        subs[0] = input[0][:3] + input[1][:3] + input[2][:3]
        subs[1] = input[0][3:6] + input[1][3:6] + input[2][3:6]
        subs[2] = input[0][6:] + input[1][6:] + input[2][6:]
        return subs

    all_rows_valid = all([is_valid(r) for r in partial_assignment])
    if not all_rows_valid: return False

    all_cols_valid = all([is_valid(c) for c in get_cols(partial_assignment)])
    if not all_cols_valid: return False

    all_sections_valid = all([is_valid(s) for s in get_sections(partial_assignment)])
    if not all_sections_valid: return False

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_sudoku.py',
                                       'is_valid_sudoku.tsv', is_valid_sudoku))
