"""
322. Coin Change

https://leetcode.com/problems/coin-change

NOTES
  * Use dynamic programming and/or memoization.

For these types of problems, you can build the solution from solutions of its
subproblems (bottom-up approach) or with recursion and memoization (top-down
approach).

Both the dynamic programming (bottom-up) and memoization (top-down) solutions
have O(S * n) time complexity where 'S' is the amount and 'n' is the number of
coins.

This problem should not be confused with the coin change problem where you need
to find the number of different ways to make up an amount using the given coins
(also known as the coin combination counting problem). This is an NP-hard
problem meaning there is no known algorithm that can solve all instances of the
problem quickly (in polynomial time), and it is believed that no such algorithm
exists.
"""

import sys


class Solution:
    """
    Using a bottom-up approach, we can reason that the minimum number of coins
    to get to F(i) is the minimum number of coins to get to F(i - cj) + 1 for
    j=0...n-1.

    Therefore, the iterative approach calculates the minimum number of coins to
    get F(i) for all i, finds the minimum, then adds 1.

    In order to conceptualize this problem, visualize an array where each index
    represents the minimum number of coins required to make up that amount. For
    example, given coins representing the denominations 1, 5, and  10, the
    array would contain the following values:

      | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
      ----------------------------------------------
      | 0 | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 | 5 |  1 |

    We can make the following observations:
      * We need an array, dp, of length amount + 1, initialize with a maximum
        value (sys.maxsize).
      * The minimum number of coins required to represent an amount (i) is the
        minimum number of coins required to get to the amount minus the
        denomination + 1 for each denomination. This is represented more
        succinctly with F(i - cj) + 1 for j=0...n-1.
      * We then arrive at a solution by building from the "bottom-up".
    """

    def coinChange(self, coins: list[int], amount: int) -> int:
        dp: list[int] = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != sys.maxsize else -1


class MemoizationSolution:
    """
    Using a top-down approach, we recursively calculate the number of coins
    using the previously calculated minimums.

    This approach can be visualize in a similar fashion to the bottom-up
    approach, but instead of building up to a solution, we recursively work
    down, calculating the solutions to subproblems with each level of
    recursion. The final solution, the first recusive call on the stack,
    benefits from the previous solutions, which are stored in an array
    (memoization).
    """

    def coinChange(self, coins: list[int], amount: int) -> int:
        memo: list[int] = [0] * (amount + 1)

        def _coinChange(coins: list[int], amount: int, memo: list[int]) -> int:
            """
            Return the minimum number of combinations of 'coins' to get to
            'amount'.
            """
            # If 'amount' is less than 0, 'amount' cannot be made up by any
            # combination of the coins.
            #
            # This is where backtracking (pruning the recursive tree) is
            # applied. The caller of the recursive function will know that the
            # following path is invalid and abort further calculations.
            if amount < 0:
                return -1
            # If 'amount' is equal to 0, 'amount' can be made up by 0 coins.
            # This represents a terminating node (leaf) of the recursive tree.
            if amount == 0:
                return 0
            if memo[amount] > 0:
                return memo[amount]
            # Set the minimum number of coins to be a max size. Ideally, this
            # would be amount / c, where c is the smallest denomination coin.
            min_num = sys.maxsize
            for coin in coins:
                res = _coinChange(coins, amount - coin, memo)
                if res != -1:
                    min_num = min(min_num, res + 1)
            memo[amount] = min_num if memo[amount] != sys.maxsize else -1
            return memo[amount] if memo[amount] != sys.maxsize else -1

        return _coinChange(coins, amount, memo)


class BruteForceSolution:
    """
    The brute force solution would be to enumerate all subsets of coin
    frequencies that satisfy the constraint (amount), compute their sums and
    return the minimum set. This would result in O(S^n) time complexity where
    'S' is the amount and 'n' is the number of coins.

    However, we can apply backtracking, so that we do not calculate the
    combinations that result in a total greater than the amount resulting in a
    O(n^S) runtime (exponential time).
    """

    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0

        def _coinChange(coins: list[int], amount: int) -> int:
            # If 'amount' is less than 0, the combination is not valid. We use
            # the return value of -1 to report to the caller that the given
            # combination is invalid. This is an application of backtracking,
            # since we do not process combinations (or paths in the recursive
            # tree) that are guaranteed to be invalid.
            if amount < 0:
                return -1
            # If 'amount' is equal to 0, the combination is valid.
            if amount == 0:
                return 0
            min_num = sys.maxsize
            for coin in coins:
                res = _coinChange(coins, amount - coin)
                if res != -1:
                    min_num = min(min_num, res + 1)
            return min_num if min_num != sys.maxsize else -1

        return _coinChange(coins, amount)
