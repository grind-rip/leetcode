"""
121. Best Time to Buy and Sell Stock

https://leetcode.com/problems/best-time-to-buy-and-sell-stock

NOTES
  * Use a sliding window. 'Start' is the current minimum price. 'End' is the
    current price.
"""
import sys
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price, max_profit = sys.maxsize, 0
        for p in prices:
            if p < min_price:
                min_price = p
            elif p - min_price > max_profit:
                max_profit = p - min_price
        return max_profit


# Though the following solution is optimized such that `max()` is only called
# when the index of the current price is equal to the index of the current max,
# its worse case runtime is still O(n^2) (runs n(n-1)/2 times).
class OptimizedNaiveSolution:
    def maxProfit(self, prices: List[int]) -> int:
        max_price: List[int] = [0, 0]  # index, value
        max_profit = 0
        for i, p in enumerate(prices):
            if p >= max_price[0]:
                max_price[1] = max(prices[i:])
            if max_price[1] - p > max_profit:
                max_profit = max_price[1] - p
        return max_profit


# This is fundamentally a brute force solution, as `max()` must iterate over
# the list `n` times.
class NaiveSolution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i, p in enumerate(prices):
            max_price = max(prices[i:])
            if max_price - p > max_profit:
                max_profit = max_price - p
        return max_profit
