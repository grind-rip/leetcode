"""
1768. Merge Strings Alternately

https://leetcode.com/problems/merge-strings-alternately

NOTES
  * Simple two pointer algorithm.

Slight optimization: You don't actually need the variable `i`.

  ```
  res += word1[p1] + word2[p2]
  p1 += 1
  p2 += 1
  ```
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1, p2, i = 0, 0, 0
        res = ""

        while p1 < len(word1) and p2 < len(word2):
            if i % 2 == 0:
                res += word1[p1]
                p1 += 1
            else:
                res += word2[p2]
                p2 += 1
            i += 1

        while p1 < len(word1):
            res += word1[p1]
            p1 += 1

        while p2 < len(word2):
            res += word2[p2]
            p2 += 1

        return res
