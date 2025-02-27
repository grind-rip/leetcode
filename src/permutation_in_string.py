"""
567. Permutation in String

https://leetcode.com/problems/permutation-in-string

NOTES
  * Use a sliding window.

I tried to get fancy with this one and use bitwise operations. This failed.
Just use a hash map or, better still, an array of size 26 (one index for each
character).
"""

from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left, right = 0, len(s1)

        # Create a mapping of character -> frequency. Here, it is advantageous
        # to use an instance of Counter, however an ordinary dict would work
        # just as well.
        s1_counter: Counter[str] = Counter(s1)
        s2_counter: Counter[str] = Counter(s2[: len(s1)])

        while right < len(s2):
            if s1_counter == s2_counter:
                return True
            s2_counter[s2[right]] += 1
            right += 1
            s2_counter[s2[left]] -= 1
            left += 1

        # Add final equality check.
        return s1_counter == s2_counter


class ArraySolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def offset(c: str) -> int:
            return ord(c) - ord("a")

        left, right = 0, len(s1)

        # Use an array of size 26. NOTE: In order to offset a character so that
        # it is between 0 and 25, use:
        #
        #   ord(c) - ord('a')
        s1_counter: list[int] = [0] * 26
        s2_counter: list[int] = [0] * 26

        for i in range(len(s1)):
            s1_counter[offset(s1[i])] += 1

        for i in range(len(s1)):
            s2_counter[offset(s2[i])] += 1

        while right < len(s2):
            if s1_counter == s2_counter:
                return True
            s2_counter[offset(s2[right])] += 1
            right += 1
            s2_counter[offset(s2[left])] -= 1
            left += 1

        # Add final equality check.
        return s1_counter == s2_counter
