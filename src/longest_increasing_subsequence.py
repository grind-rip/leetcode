"""
300. Longest Increasing Subsequence

https://leetcode.com/problems/longest-increasing-subsequence

NOTES
  * Use dynamic programming (1D) or recursion.

My initial intuition was this is a dynamic programming (1D) problem, since the
problem can be built up from solutions to its subproblems. However, I was
unable to formulate the correct recurrence relation. I was, however, able to
derive the correct recursive solution.

As an initial approach, let's find the base cases:

  1. If nums is empty, return 0
  2. If nums has length 1, return 1

Next, we look that a simplified example:

  3. If nums = [1, 2],
     2 > 1, therefore LIS = 2

  4. If nums = [1, 5, 2, 4],
     5 > 1, therefore LIS([1,5]) = 2, however, LIS([1, 5, 2, 4]) = 3

How should we account for the fact that the longest increasing subsequence is
formed not by using 5, but instead by using 2 and 4? Programmatically, this
signifies a decision branch that can be resolved recursively:

  1. When nums[i] is included in the subsequence
  2. When nums[i] is not included in the subsequence

For the first case, we increment the LIS by 1 and update the current largest
element in the subsequence. For the second case, we simply ignore nums[i],
retaining the current largest element in the subsequence. We then take the
maximum of each branch of the decision tree.

    if nums[0] > m:
        return max(1 + lis(nums[1:], nums[0]), lis(nums[1:], m))
    else:
        return lis(nums[1:], m)

Realizing a Dynamic Programming Problem
---------------------------------------

This problem has two important attributes that let us know it should be solved
by dynamic programming. First, the question is asking for the maximum or
minimum of something. Second, we have to make decisions that may depend on
previously made decisions, which is very typical of a problem involving
subsequences.

As we go through the input, each "decision" we must make is simple: is it worth
it to consider this number? If we use a number, it may contribute towards an
increasing subsequence, but it may also eliminate larger elements that came
before it. For example, let's say we have nums = [5, 6, 7, 8, 1, 2, 3]. It
isn't worth using the 1, 2, or 3, since using any of them would eliminate 5, 6,
7, and 8, which form the longest increasing subsequence. We can use dynamic
programming to determine whether an element is worth using or not.

A Framework to Solve Dynamic Programming Problems
-------------------------------------------------

Typically, dynamic programming problems can be solved with three main
components. If you're new to dynamic programming, this might be hard to
understand but is extremely valuable to learn since most dynamic programming
problems can be solved this way.

First, we need some function or array that represents the answer to the problem
from a given state. Typically, since array is named "dp". For this problem,
let's say that we have an array dp. As just stated, this array needs to
represent the answer to the problem for a given state, so let's say that dp[i]
represents the length of the longest increasing subsequence that ends with the
ith element. The "state" is one-dimensional since it can be represented with
only one variable - the index i.

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
"""

import sys


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        dp: list[int] = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


class MemoizationSolution:
    """
    Similar to the recursive solution, but uses memoization to store previous
    calculations. This one is a little bit tricky, since the memoization lookup
    uses both the index and m, the current largest element in the subsequence.

    NOTE: Though *technically* correct, this solution still exceeds the time
    limit.
    """

    def lengthOfLIS(self, nums: list[int]) -> int:
        # Initialize the memoization table. Each key in the table is formed
        # using an index in nums and the current largest element in the
        # subsequence. The stored value is the current longest increasing
        # subsequence for the index.
        #
        # One effect of the using the index and current largest element for the
        # key is that it actually lets us handle overlapping subsequences
        # correctly, since we're caching results for each unique combination of
        # remaining numbers and minimum value.
        memo: dict[tuple[int, int], int] = {}

        def lis(nums: list[int], i: int, m: int) -> int:
            if i >= len(nums):
                return 0
            key = (i, m)
            if key in memo:
                return memo[key]
            # Calculate the result of each decision:
            #
            #   1. nums[i] is included in the subsequence
            #   2. nums[i] is not included in the subsequence
            #
            # nums[i] becomes the current largest element in the subsequence.
            if nums[i] > m:
                return max(lis(nums, i + 1, nums[i]) + 1, lis(nums, i + 1, m))
            else:
                res = lis(nums, i + 1, m)
            memo[key] = res
            return res

        return lis(nums, 0, -sys.maxsize)


class RecursiveSolution:
    """
    The recursive solution to Longest Increasing Subsequence uses the intuition
    that an element should be added to the subsequence if it is greater than
    the current largest element in the subsequence.

    NOTE: Though *technically* correct, this solution exceeds the time limit,
    since it does not account for overlapping subproblems.
    """

    def lengthOfLIS(self, nums: list[int]) -> int:
        def lis(nums: list[int], i: int, m: int) -> int:
            if i >= len(nums):
                return 0
            # Calculate the result of each decision:
            #
            #   1. nums[i] is included in the subsequence
            #   2. nums[i] is not included in the subsequence
            #
            # nums[i] becomes the current largest element in the subsequence.
            if nums[i] > m:
                return max(lis(nums, i + 1, nums[i]) + 1, lis(nums, i + 1, m))
            else:
                return lis(nums, i + 1, m)

        return lis(nums, 0, -sys.maxsize)
