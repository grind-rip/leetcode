"""
20. Valid Parentheses

https://leetcode.com/problems/valid-parentheses

NOTES
  * Use a stack.

This is a fun one. Using a stack and a hash map for bracket pair lookups, open
brackets are pushed onto the stack. For each closed bracket, pop from the stack
and compare.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # A string with an odd number of characters cannot be valid.
        if len(s) % 2 != 0:
            return False

        # Use a hash map for bracket pair lookups.
        m: dict[str, str] = {"(": ")", "{": "}", "[": "]"}
        stack = []

        # For each character `c` in `s`, if `c` is an open bracket (i.e., it is
        # a key in `m`), push it onto the stack. If `c` is a closed bracket,
        # pop a value from the stack. The value should be the corresponding
        # open bracket of the bracket pair.
        for c in s:
            if c in m:
                stack.append(c)
            elif len(stack) == 0 or m[stack.pop()] != c:
                return False

        return len(stack) == 0
