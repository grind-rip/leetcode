"""
238. Product of Array Except Self

https://leetcode.com/problems/product-of-array-except-self

NOTES

Given the following constraint,

  >You must write an algorithm that runs in O(n) time and without using the
   division operation.

where `n` represents the number of elements in the input array, we can only
iterate through the list once (or some constant number of times (ex. 3) as we
shall see in the solution).

Examples:

  [1, 1] -> [1, 1]
  [1, 2] -> [2, 1]
  [1, 2, 3] -> [6, 3, 2]
  [1, 2, 3, 4] -> [24, 12, 8, 6]
  [1, 2, 3, 4, 5] -> [120, 60, 40, 30, 24]

Scratch:

    i →

  j  [1, 2, 3, 4, 5] -> 120
  ↓  [1, 1, 3, 4, 5] ->  60
     [1, 2, 1, 4, 5] ->  40
     [1, 2, 3, 1, 5] ->  30
     [1, 2, 3, 4, 1] ->  24

     <- 120 ---------> L(j+1),i+1 / i,j * i+1,j
     <---- 60 -------> L(j+1),i+1 / i,j * i+1,j
     <------ 40 -----> Find the product to the left and right (L and R)
     <-------- 30 ---> R(j-1),i-1 / i,j * i-1,j
     <---------- 24 -> R(j-1),i-1 / i,j * i-1,j

     <- 120 ---------> 0 product(nums) / i * i-1
     <---- 60 -------> 1 prev / i * i-1
     <------ 40 -----> 2 prev / i * i-1
     <-------- 30 ---> 3 prev / i * i-1
     <---------- 24 -> 4 prev / i * i-1

  I was *close* on this one in that I reasoned correctly that the original
  array needed to be segmented into left and right parts, but failed to realize
  that I could not use the division operation ('/').

  The correct solution involves initializing two empty arrays, L and R where
  for a given index i, L[i] would contain the product of all the numbers to the
  left of i and R[i] would contain the product of all the numbers to the right
  of i. Using L and R, the product of index i can be easily calculated as:

    L[i] * R[i]
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        L, R, res = [0] * length, [0] * length, [0] * length

        # L[i] is the product of all the elements to the left of i.
        #
        #   L[i] = L[i−1] ∗ nums[i−1]
        #
        # NOTE: For i = 0, there are no elements to the left of i, therefore
        # L[0] = 1.
        L[0] = 1
        for i in range(1, length):
            L[i] = L[i - 1] * nums[i - 1]

        # R[i] is the product of all the elements to the right of i.
        #
        #   R[i] = R[i+1] ∗ nums[i+1]
        #
        # NOTE: For i = length-1, there are no elements to the right of i,
        # therefore R[length -1] = 1.
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = R[i + 1] * nums[i + 1]

        # Construct answer array.
        for i in range(length):
            res[i] = L[i] * R[i]
        return res
