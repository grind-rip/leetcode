"""
53. Maximum Subarray

https://leetcode.com/problems/maximum-subarray

This problem in O(n) runtime complexity and O(1) space complexity using
Kadane's algorithm.

The key insight is that at each position, you only need to decide whether to:
  1. Start a new subarray at the current position (if previous sum is negative)
  2. Continue the existing subarray by adding the current number

This is an example of the application of dynamic programming, since the problem
possesses the optimal substructure property: an optimal solution can be
constructed from optimal solutions of its subproblems.
"""

import sys


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_sum, max_sum = 0, -sys.maxsize
        for x in nums:
            current_sum = max(current_sum + x, x)
            max_sum = max(max_sum, current_sum)
        return max_sum


class TabularizationSolution:
    """
    This solution uses explicit tabularization of the maxmium subarray for i.
    The optimal subproblem, the maximum subarray for i, is the maximum sum of
    the subarray for A[i - 1] plus A[i], or A[i]. From this, the maxmium
    subarray of the array is the maximum sum for all i.

    We find that this is simply an expansion of Kadane's algorithm, where
    'current_sum' is dp[i - 1] + nums[i]. Since, we only care about the
    currently calculated sum when determining the solution to the subproblem,
    we do not need any previous values.
    """
    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize dp array. The first element is nums[0], since the maximum
        # subarray of an array with length 1 is the array itself.
        dp: list[int] = [0] * len(nums)
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            max_sum = max(max_sum, dp[i])
        return max_sum
