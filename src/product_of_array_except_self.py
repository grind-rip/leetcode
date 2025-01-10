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

I was *close* on this one in that I reasoned correctly that the original array
needed to be segmented into left and right parts, but failed to realize that I
could not use the division operation.

The correct solution involves initializing two empty arrays, L and R where for
a given index i, L[i] contains the product of all the numbers to the left of i
and R[i] contains the product of all the numbers to the right of i. Using L and
R, the product of index i can be easily calculated as:

  L[i] * R[i]

This technique is called *precomputation*. The precomputation technique
involves processing the array once (or a constant number of times) at the
beginning to create auxiliary data structures (like prefix sums, suffix arrays,
or frequency maps) that can help optimize subsequent operations or queries.

This approach still has O(n) time complexity, since O(3*n) is still linear (
one iteration to construct L, one iteration to construct the R, and one
iteration to construct the answer using L and R).
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        L, R, res = [0] * length, [0] * length, [0] * length

        # L[i] is the product of all the elements to the left of i.
        #
        #   L[i] = L[i−1] * nums[i−1]
        #
        # NOTE: For i = 0, there are no elements to the left of i, therefore
        # L[0] = 1.
        L[0] = 1
        for i in range(1, length):
            L[i] = L[i - 1] * nums[i - 1]

        # R[i] is the product of all the elements to the right of i.
        #
        #   R[i] = R[i+1] * nums[i+1]
        #
        # NOTE: For i = length-1, there are no elements to the right of i,
        # therefore R[length - 1] = 1.
        R[length - 1] = 1
        for i in reversed(range(length - 1)):
            R[i] = R[i + 1] * nums[i + 1]

        # Construct answer array.
        for i in range(length):
            res[i] = L[i] * R[i]
        return res


class ConstantSpaceSolution:
    """
    Instead of constructing an L and R array, the answer array is constructed
    on the fly, since we only ever care about the previously calculated product
    to the left or right of i. This solution is a little less intuitive than
    constructing the L and R array and is only ever needed if you are asked to
    generate the answer array in O(1) extra space complexity.
    """

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        res = [1] * length

        # Start with L = 1, since there are no elements to the left of nums[0].
        # The product of elements to the left of res[i] is the product of
        # L, the previous product of the array of elements to the left of i,
        # and the leftmost element (nums[i - 1]). This can also be simplified
        # to res[i] = res[i - 1] * nums[i - 1].
        L = 1
        for i in range(1, length):
            res[i] = L * nums[i - 1]
            L *= nums[i - 1]

        # Start with R = 1, since there are no elements to the right of
        # res[length - 1]. The product of elements to the right of res[i] is
        # the product of R, the previous product of the array of elements to
        # the right of i, and the current element in the answer array (res[i]).
        # It should be noted that the ith element of the answer array is used
        # here, not the ith element of the input array (nums).
        R = 1
        for i in reversed(range(length)):
            res[i] = R * res[i]
            R *= nums[i]

        return res
