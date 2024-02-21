"""
300. Longest Increasing Subsequence

https://leetcode.com/problems/longest-increasing-subsequence

NOTES

My initial thought is this is a 1D dynamic programming problem, since the
problem can be built up from its subproblems.

As an initial approach, let's find the base cases:

  1. If nums = [], return 0
  2. If nums has the length 1, return 1

Next, we look that a simplified example:

  3. If nums = [1, 2], (i + 1) > 1, therefore return 1 + 1
  4. If nums = [1, 3, 2, 4], return 1 + lis([3, 2, 4]) (which is 2)

Realizing a Dynamic Programming Problem
---------------------------------------

This problem has two important attributes that let us know it should be solved
by dynamic programming. First, the question is asking for the maximum or
minimum of something. Second, we have to make decisions that may depend on
previously made decisions, which is very typical of a problem involving
subsequences.

A Framework to Solve Dynamic Programming Problems
-------------------------------------------------

Typically, dynamic programming problems can be solved with three main
components. If you're new to dynamic programming, this might be hard to
understand, but it is extremely valuable to learn, since most dynamic
programming problems can be solved this way.

First, we need some function or array that represents the answer to the problem
from a given state. For many solutions on LeetCode, you will see this
function/array named "dp". For this problem, let's say that we have an array
dp. As previously stated, this array needs to represent the answer to the
problem for a given state, so let's say that dp[i] represents the length of the
longest increasing subsequence that ends with the ith element. The "state" is
one-dimensional since it can be represented with only one variable–the index i.

Second, we need a way to transition between states, such as dp[5] and dp[7].
This is called a recurrence relation and can sometimes be tricky to figure out.
Let's say we know dp[0], dp[1], and dp[2]. How can we find dp[3] given this
information? Well, since dp[2] represents the length of the longest increasing
subsequence that ends with nums[2], if nums[3] > nums[2], then we can simply
take the subsequence ending at i = 2 and append nums[3] to it, increasing the
length by 1. The same can be said for nums[0] and nums[1] if nums[3] is larger.
Of course, we should try to maximize dp[3], so we need to check all 3.
Formally, the recurrence relation is: dp[i] = max(dp[j] + 1) for all j where
nums[j] < nums[i] and j < i.

The third component is the simplest: we need a base case. For this problem, we
can initialize every element of dp to 1, since every element on its own is
technically an increasing subsequence.

NOTE: I got close when trying to solve this with recursion and memoization,
however my solutions failed the following test case:

  [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12]

ChatGippity could not solve it either, so this can be a future problem to
return to...
"""

import sys
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp: List[int] = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class MemoizationSolution:
    """
    Similar to the top-down approach of the recursive solution, but uses
    memoization to store previous calculations.

    NOTE: This solution fails the following test case:

      [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12] -> 5 == 3
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        # Initialize the memoization table. Each index in the table is the
        # calculated longest increasing subsequence up to and including the
        # current index.
        memo: List[int] = [1] * len(nums)

        def lis(nums: List[int], m: int, memo) -> int:
            if len(nums) == 1:
                return 1 if nums[0] > m else 0
            # Calculate the result of each decision:
            #
            #   1. nums[i] is included in the subsequence
            #   2. nums[i] is *not* included in the subsequence
            i = len(memo) - len(nums)
            if memo[i] > 1:
                return memo[i]
            if nums[0] > m:
                memo[i] = max(1 + lis(nums[1:], nums[0], memo), lis(nums[1:], m, memo))
            else:
                memo[i] = lis(nums[1:], m, memo)
            return memo[i]

        # NOTE: -10^4 <= nums[i] <= 10^4
        return lis(nums, -sys.maxsize, memo)


class RecursiveSolution:
    """
    NOTE: This solution exceeds the time limit.

    NOTE: This solution fails the following test case:

      [3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12] -> 6 == 3
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        def lis(nums: List[int], m: int) -> int:
            if len(nums) == 1:
                return 1 if nums[0] > m else 0

            # Calculate the result of each decision:
            #
            #   1. nums[i] is included in the subsequence
            #   2. nums[i] is *not* included in the subsequence
            if nums[0] > m:
                return max(1 + lis(nums[1:], nums[0]), lis(nums[1:], m))
            else:
                return lis(nums[1:], m)

        # NOTE: -10^4 <= nums[i] <= 10^4
        return lis(nums, -sys.maxsize)
