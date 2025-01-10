"""
125. Valid Palindrome

https://leetcode.com/problems/valid-palindrome

NOTES
  * Use two pointers. Use the ASCII table and the `ord()` function to convert
    characters to their ASCII values.

  * You can also just use `isalnum()` and `lower()`, which checks that the
    character is non-alphanumeric and converts the character to lowercase,
    respectively.

A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters, it reads the
same forward and backward.
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Given the constraint:

          * `s` consists only of printable ASCII characters

        and the requirement:

          >...after converting all uppercase letters into lowercase letters and
           removing all non-alphanumeric characters...

        We can use the ASCII table to convert uppercase characters to lowercase
        and skip any non-alphanumeric characters.

          * 0-9 = 48-57
          * A-Z = 65-90
          * a-z = 97-122

        Offset (A -> a) = 32
        """
        ASCII_0 = 48
        ASCII_9 = 57
        ASCII_A = 65
        ASCII_Z = 90
        ASCII_a = 97
        ASCII_z = 122
        OFFSET = 32

        if len(s) == 0:
            return True

        p0, p1 = 0, len(s) - 1
        while p0 < p1:
            c0, c1 = ord(s[p0]), ord(s[p1])
            if (ASCII_0 <= c0 <= ASCII_9) or (ASCII_A <= c0 <= ASCII_Z) or (ASCII_a <= c0 <= ASCII_z):
                if ASCII_A <= c0 <= ASCII_Z:
                    c0 = c0 + OFFSET
            else:
                p0 = p0 + 1
                continue
            if (ASCII_0 <= c1 <= ASCII_9) or (ASCII_A <= c1 <= ASCII_Z) or (ASCII_a <= c1 <= ASCII_z):
                if ASCII_A <= c1 <= ASCII_Z:
                    c1 = c1 + OFFSET
            else:
                p1 = p1 - 1
                continue
            if c0 != c1:
                return False
            p0, p1 = p0 + 1, p1 - 1
        return True


class SimplifiedSolution:
    def isPalindrome(self, s: str) -> bool:
        """
        You don't need to be fancy with this one. Just use two pointers and
        some additional logic for handling non-alphanumeric characters.
        """
        if len(s) == 0:
            return True

        left, right = 0, len(s) - 1

        while left < right:
            # If a character is non-alphanumeric, skip it.
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
