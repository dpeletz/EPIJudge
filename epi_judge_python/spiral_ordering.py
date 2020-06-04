from typing import List

from test_framework import generic_test


def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    # MY RECURSIVE SOLUTION:
    n, spiral_ordering = len(square_matrix), []

    if n == 0: return spiral_ordering

    if n == 1: return square_matrix[0]

    if n == 2:
        spiral_ordering.extend(square_matrix[0])
        spiral_ordering.extend(square_matrix[1][::-1])
        return spiral_ordering

    else:
        spiral_ordering.extend(square_matrix[0])
        row, col = 1, n - 1

        for i in range(n - 1):
            spiral_ordering.append(square_matrix[row][col])
            row += 1
        row, col = row - 1, col - 1
        for i in range(n - 1):
            spiral_ordering.append(square_matrix[row][col])
            col -= 1
        row, col = n - 2, 0
        for i in range(n - 2):
            spiral_ordering.append(square_matrix[row][col])
            row -= 1

        rows, matrix = square_matrix[1:n], []

        for i in range(len(rows) - 1): matrix.append(rows[i][1:len(rows[i]) - 1])

        spiral_ordering.extend(matrix_in_spiral_order(matrix))

        return spiral_ordering

    # BOOK SOLUTION:
    # SHIFT = ((0, 1), (1, 0), (0, -1), (-1, 0))
    # direction = x = y = 0
    # spiral_ordering = []
    #
    # for _ in range(len(square_matrix) ** 2):
    #     spiral_ordering.append(square_matrix[x][y])
    #     square_matrix[x][y] = "x"
    #     next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
    #
    #     if (next_x not in range(len(square_matrix))
    #             or next_y not in range(len(square_matrix))
    #             or square_matrix[next_x][next_y] == "x"):
    #         direction = (direction + 1) & 3
    #         next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
    #     x, y = next_x, next_y
    # return spiral_ordering


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spiral_ordering.py',
                                       'spiral_ordering.tsv',
                                       matrix_in_spiral_order))
