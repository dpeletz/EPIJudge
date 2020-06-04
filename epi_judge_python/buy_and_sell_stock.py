from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    min_price = float("inf")
    max_prof = float("-inf")

    for i in range(len(prices)):

        if prices[i] < min_price: min_price = prices[i]
        if prices[i] - min_price > max_prof: max_prof = prices[i] - min_price

    return max_prof

    # if len(prices) == 1: return 0.0
    # l, r = 0, 1
    # diffs = []
    #
    # while r < len(prices):
    #     diffs.append(prices[r] - prices[l])
    #     l, r = l + 1, r + 1
    #
    # l, r = 0, 1
    #
    # while l < len(prices) - 2:
    #     r = l + 1
    #     while r < len(prices) - 1:
    #         diffs.append(sum(diffs[l:r + 1]))
    #         r += 1
    #     l += 1
    #
    # md = max(diffs)
    # return 0.0 if md <= 0 else md


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
