"""
340. Longest Substring with At Most K Distinct Characters

https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters

NOTES
  * Use a sliding window.

A general solution to 'Longest Substring with At Most Two Distinct Characters'.
Simply substitute 'k' for '2'. Easy bag.
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, right, maximum_size = 0, 0, 0

        # Maintain a mapping of character -> index of last occurrence.
        d: dict[str, int] = {}

        while right < len(s):
            d[s[right]] = right

            # If the map ever contains more than 'k' keys, then the substring
            # contains more than 'k' distinct characters.
            if len(d) > k:
                # Move `left` to the character after the next index.
                next_index = min(d.values())
                left = next_index + 1
                # Remove the character from the hash map.
                del d[s[next_index]]

            maximum_size = max(maximum_size, right - left + 1)
            right += 1

        return maximum_size
