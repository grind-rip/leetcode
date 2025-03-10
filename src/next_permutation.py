"""
31. Next Permutation

https://leetcode.com/problems/next-permutation

NOTES
  * Use a special algorithm. You just need to know how to do this one.

Definitions
-----------
A permutation of an array of integers is an arrangement of its members into a
sequence or linear order.

For example, all permutations of the array [1, 2, 3] are:

  [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]

The next permutation of an array of integers is the next lexicographically
greater permutation of its integers. If the arrangement for the next possible
permutation does not exist, the next permutation is the first (lowest)
permutation.

NOTE: A list of length n has n! permutations, so enumerating all possible
permutations has O(n!) time complexity.

Algorithm
---------
First, observe that for a sequence that is in descending order, no next larger
permutation is possible.

  [5, 4, 3, 2, 1]

So, the next permutation is the reverse of the final permutation.

  [1, 2, 3, 4, 5]

Next, let's take a look at the permutation before the final permutation:

  [5, 4, 3, 1, 2]

To get the final permutation we swap 1 and 2. In fact 1 and 2 are the first
pair of successive numbers which satisfy the condition a[i] > a[i-1]. This is
another key insight:

  >Given a starting permutation of `a`, the first pair of two successive
   numbers a[i] and a[i−1], which satisfy the condition a[i] > a[i−1] found by
   traversing the array from the right, demarcate the start of the next
   permutation. We can assert that a[i...n-1] are in descending order.

In order to get the next permutation, we need to replace a[i-1] with the next
larger number in a[i...n-1]. Said another way, we need to find the smallest
value a[i...n-1] that is larger than a[i-1]. We will call this value a[j].
Swapping these values, a[i-1] and a[j], puts the correct value at index i - 1.

Next, the sequence a[i...n-1] needs to be rearranged into the lowest possible
permutation, which is formed by putting its values in ascending order. However,
since we have already asserted that a[i...n-1] are in descending order, we just
have to reverse the sequence (an O(n) operation).
"""


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        1. Find the pivot: Scan from right to left to find the first index i−1
           such that nums[i−1] < nums[i].

        2. Swap with a just‐larger element: From the right again, find the
           first index j where nums[j] > nums[i−1]. Swap nums[i−1] and nums[j].

        3. Reverse the suffix: Finally, reverse the subarray nums[i...n−1].
        """
        n = len(nums)
        if n <= 1:
            return None

        i = n - 1

        # Find `i` which satisfies the condition nums[i−1] < nums[i].
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1

        # Find the first value in nums[i...n-1], where nums[j] > nums[i-1].
        if i > 0:
            j = n - 1
            while nums[j] <= nums[i - 1]:
                j -= 1
            # Swap nums[i-1] and nums[j].
            nums[i - 1], nums[j] = nums[j], nums[i - 1]

        # Reverse nums[i...n-1].
        k = n - 1
        while i < k:
            nums[i], nums[k] = nums[k], nums[i]
            i += 1
            k -= 1

        return None
