"""
198. House Robber

https://leetcode.com/problems/house-robber

NOTES
  * Use dynamic programming and/or memoization.

This problem should immediately signal dynamic programming. It is very similar
to the 'Climbing Stairs' problem.

Remember...

If the problem can be broken down into subproblems, and if it contains the
optimal substructure property (i.e., its optimal solution can be constructed
efficiently from optimal solutions of its subproblems), it can be efficiently
solved using dynamic programming.
"""


class Solution:
    """
    Since we cannot rob adjacent houses, we determine if the ith house should
    be robbed by calculating if the (i-2)th house and ith house would yield
    more money than the (i-1)th house (i.e., not robbing the ith house).
    """

    def rob(self, nums: list[int]) -> int:
        dp: list[int] = [0] * len(nums)

        # Initialize the array. Typically, the algorithm starts *after* some
        # initial values are calculated and boundary conditions are checked.
        if len(nums) == 1:
            return nums[0]

        dp[0] = nums[0]
        dp[1] = nums[1] if nums[1] > nums[0] else nums[0]
        max_amount = max(dp[0], dp[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
            if dp[i] > max_amount:
                max_amount = dp[i]

        return max_amount


class MemoizationSolution:
    """
    Using a top-down approach, we determine if the ith house should be robbed
    using the stored value of the maximum amount of money robbed from the
    (i-2)th and (i-1)th houses.

    Memoization follows a typical pattern:
      1. A memoization array or table is initialized.
      2. An inner function is defined that facilitates recursion and takes the
         memoization array or table as an argument.
      3. Base conditions are checked in the recursive function.
      4. A stored value is returned if it has already been calculated.
      5. The value is calculated, stored, and returned using the recursive
         function.
    """

    def rob(self, nums: list[int]) -> int:
        memo: list[int] = [-1] * len(nums)

        def _rob(i: int, nums: list[int], memo: list[int]) -> int:
            if i == 0:
                return nums[i]

            if i == 1:
                return max(nums[1], nums[0])

            # If memo[i] has been calculated (i.e., != -1), reuse its value.
            # NOTE: We cannot initialize the memoization array to 0's, since
            # the amount of 0 is a valid amount (0 <= nums[i] <= 400).
            if memo[i] != -1:
                return memo[i]

            memo[i] = max(_rob(i - 2, nums, memo) + nums[i], _rob(i - 1, nums, memo))

            return memo[i]

        return _rob(len(nums) - 1, nums, memo)
