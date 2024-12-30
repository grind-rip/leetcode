"""
70. Climbing Stairs

https://leetcode.com/problems/climbing-stairs

NOTES
  * Use dynamic programming and/or memoization.

If the problem can be broken down into subproblems, and if it contains the
optimal substructure property (i.e., its optimal solution can be constructed
efficiently from optimal solutions of its subproblems), it can be efficiently
solved using dynamic programming.
"""


class Solution:
    """
    The brute force solution would be to try every step combination, however,
    we can use dynamic programming and/or memoization to simplify the problem
    by "remembering" how many different combinations it took to reach the
    (i−1)th and (i−2)th step.

    The total number of ways to reach the ith step is equal to sum of ways of
    reaching the (i−1)th step and ways of reaching the (i−2)th step.
    """

    def climbStairs(self, n: int) -> int:
        dp: list[int] = [0, 1, 2]
        for i in range(3, n + 1):
            dp.append(dp[i - 1] + dp[i - 2])
        return dp[n]


class MemoizationSolution:
    """
    Memoization is an optimization technique used primarily in recursive
    algorithms. It involves storing the results of expensive function calls and
    returning the cached result when the same inputs occur again.

    This solution uses a top-down approach. Instead of solving each subproblem
    from scratch, we store the results of subproblems in a hash table and
    retrieve them when needed.
    """

    def climbStairs(self, n: int) -> int:
        memo: list[int] = [0] * n

        def _climbStairs(i: int, n: int, memo: list[int]) -> int:
            """
            Where 'i' is the current step, 'n' is the target step, and 'memo'
            is a hash table of previous calculations.
            """
            # If 'i' (current step) is greater than 'n' (the target step), we
            # have overshot our target step and therefore the function returns
            # 0, as the combination is not a valid path.
            if i > n:
                return 0
            # If 'i' (current step) is equal to 'n' (the target step), we have
            # reached our target step and therefore the function returns 1, as
            # the combination is a valid path.
            if i == n:
                return 1
            # If memo[i] has been calculated (i.e., not 0), reuse its value.
            if memo[i] > 0:
                return memo[i]
            memo[i] = _climbStairs(i + 1, n, memo) + _climbStairs(i + 2, n, memo)
            return memo[i]

        return _climbStairs(0, n, memo)


class BruteForceSolution:
    """
    The brute force solution calculates all the distinct ways to climb to the
    top by summing the ways to get to each step using either 1 or 2 steps.

    It should be noted that the time complexity of this solution is O(2^n),
    where 'n' is the number of steps.
    """

    def climbStairs(self, n: int) -> int:
        def _climbStairs(i: int, n: int) -> int:
            if i > n:
                return 0
            if i == n:
                return 1
            return _climbStairs(i + 1, n) + _climbStairs(i + 2, n)

        return _climbStairs(0, n)
