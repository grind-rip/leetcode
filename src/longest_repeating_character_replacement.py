"""
424. Longest Repeating Character Replacement

https://leetcode.com/problems/longest-repeating-character-replacement

NOTES
  * Use a sliding window.

This is a hard one. The key insight is that a substring is valid (i.e., the
substring contains only one unique character after performing k replacements)
when:

  window size - frequency of most common character ≤ k

Initially, I inverted the logic, searching instead for the longest substring
with > k replacements. The correct solution is pretty straightforward *if* you
are working from the above premise. Additionally, I've added the canonical
sliding window implementation. Its form should look familiar...
"""

from collections import Counter


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, maximum_size = 0, 0, 0

        # Maintain a mapping of character -> frequency. Likewise, keep track
        # of the most common character (i.e, the maximum frequency character).
        counter: Counter[str] = Counter()
        maximum_frequency = 0

        while right < len(s):
            counter[s[right]] += 1

            # Update the maximum frequency.
            maximum_frequency = max(maximum_frequency, counter[s[right]])

            # Check to see if the current substring is valid. Remember, a
            # substring is valid if:
            #
            #   window size - frequency of most common character ≤ k
            #
            # If the window is invalid, increment left, which invariably will
            # result in a valid substring.
            if (right - left + 1) - maximum_frequency > k:
                counter[s[left]] -= 1
                left += 1

            maximum_size = max(maximum_size, right - left + 1)
            right += 1

        return maximum_size


class CanonicalSolution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right, maximum_size = 0, 0, 0

        # Maintain a mapping of character -> frequency.
        counter: Counter[str] = Counter()
        maximum_frequency = 0

        while right < len(s):
            counter[s[right]] += 1
            maximum_frequency = max(maximum_frequency, counter[s[right]])
            # Invariant: left <= right and substring is invalid.
            while left <= right and (right - left + 1) - maximum_frequency > k:
                counter[s[left]] -= 1
                left += 1
            maximum_size = max(maximum_size, right - left + 1)
            right += 1

        return maximum_size
