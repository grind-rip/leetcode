"""
159. Longest Substring with At Most Two Distinct Characters

https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters

NOTES
  * Use a sliding window.

This one is pretty easy. As with other substring problems, we can use a hash
map to track the frequency of characters in the current substring. Since,
however, we are only concerned with at most two characters, we can just use two
variables. Similar to 'Longest Substring Without Repeating Characters', we
maintain the index of the last occurrence of each character in order to adjust
the sliding window if the substring becomes invalid. In addition, I've added a
solution that generalizes to 'k' distinct characters.
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # c1 and c2 hold the index of the last occurrence of a character.
        left, right, c1, c2, maximum_size = 0, 0, 0, 0, 0

        while right < len(s):
            # NOTE: s[c1] != s[c2] handles the case where `s` starts with
            # repeating characters
            if s[right] not in [s[c1], s[c2]] and s[c1] != s[c2]:
                # Move `left` to the character after the next index.
                if c1 < c2:
                    left, c1, c2 = c1 + 1, c2, right
                else:
                    left, c2, c1 = c2 + 1, c1, right
            # Update the index of `c1` and `c2`, the last occurrence of each
            # character.
            elif s[right] == s[c1]:
                c1 = right
            else:
                c2 = right

            maximum_size = max(maximum_size, right - left + 1)
            right += 1

        return maximum_size


class GeneralSolution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left, right, maximum_size = 0, 0, 0

        # Maintain a mapping of character -> index of last occurrence.
        d: dict[str, int] = {}

        while right < len(s):
            d[s[right]] = right

            # If the map ever contains more than two keys, then the substring
            # contains more than two distinct characters.
            if len(d) > 2:
                # Move `left` to the character after the next index.
                next_index = min(d.values())
                left = next_index + 1
                # Remove the character from the hash map.
                del d[s[next_index]]

            maximum_size = max(maximum_size, right - left + 1)
            right += 1

        return maximum_size
