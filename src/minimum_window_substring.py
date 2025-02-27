"""
76. Minimum Window Substring

https://leetcode.com/problems/minimum-window-substring

NOTES
  * Use a sliding window.

Not sure why this is categorized as "hard". Maybe I've just done so many of
these problems, the solution is intuitive. Frequency map, sliding window, boom,
done.

Spoke too soon... Spent over thirty minutes with the tricky logic around
remaining characters. The key is to only decrement/increment `remaining` if the
count is greater than 0. This ensures the substring possesses all required
characters without erroneously counting extra occurrences of characters already
satisfied in the substring.
"""

import sys
from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left, right, start, end, minimum_size = 0, 0, 0, 0, sys.maxsize

        # Create a frequency map. Additionally, keep track of the count of
        # remaining characters needed for the substring to be valid (i.e.,
        # every character in `t` is included in the substring).
        counter: Counter[str] = Counter(t)
        remaining = len(t)

        while right < len(s):
            if s[right] in counter:
                #  Only decrement `remaining` if count is greater than 0.
                if counter[s[right]] > 0:
                    remaining -= 1
                counter[s[right]] -= 1
            while left <= right and remaining == 0:
                current_size = right - left + 1
                if current_size < minimum_size:
                    minimum_size = current_size
                    start, end = left, right
                if s[left] in counter:
                    counter[s[left]] += 1
                    #  Only increment `remaining` if count is greater than 0.
                    if counter[s[left]] > 0:
                        remaining += 1
                left += 1
            right += 1

        return s[start : end + 1] if minimum_size < sys.maxsize else ""
