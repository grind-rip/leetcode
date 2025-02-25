"""
3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters

NOTES
  * Use a sliding window.

A subarray is a contiguous, non-empty sequence of elements within an array.
Here, we just apply the canonical subarray/substring solution using a sliding
window. Additionally, I've added a slightly more efficient solution that jumps
the left pointer to the index after the last occurrence of the duplicate
character.
"""

from collections import Counter


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, maximum_size = 0, 0, 0

        # Maintain a mapping of character -> index of last occurrence.
        d: dict[str, int] = {}

        while right < len(s):
            # Whenever we find a duplicate character, left is updated to the
            # index after the last occurrence of that character.
            if s[right] in d and d[s[right]] >= left:
                left = d[s[right]] + 1
            d[s[right]] = right
            maximum_size = max(maximum_size, right - left + 1)
            right += 1

        return maximum_size


class CanonicalSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, right, maximum_size = 0, 0, 0

        # Maintain a mapping of character -> frequency.
        counter: Counter[str] = Counter()

        while right < len(s):
            counter[s[right]] += 1
            # Invariant: left <= right and substring has duplicate.
            while left <= right and counter[s[right]] > 1:
                counter[s[left]] -= 1
                left += 1
            maximum_size = max(maximum_size, right - left + 1)
            right += 1

        return maximum_size
