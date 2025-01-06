"""
242. Valid Anagram

https://leetcode.com/problems/valid-anagram

NOTES
  * An anagram is a word or phrase formed by rearranging the letters of a
    different word or phrase, typically using all the original letters exactly
    once.

My original thought was to sum the integer values of the characters. This would
provide a "fingerprint" for the anagram. Given that an anagram is formed by
using all the original letters exactly once, two strings with the same
"fingerprint" should be anagrams.

After some consideration, I realized this will not work. For example:

  Let's say we have the following mapping:
    * a = 1
    * b = 2
    * c = 3
    * d = 4
    * e = 5

  The following combinations would have a "fingerprint" of 5:
    * ad = 5
    * bc = 5

  These are obviously not anagrams.

As a second approach, we can probably use our old friend: hash map. We first
iterate through the first string, accounting for each character in dict `d`.
Next, we iterate through the second string decrementing each occurrence of the
given character in `d`. If a character (key) has value 0, we delete it from the
dict. If `s` and `t` are anagrams, the dict should be empty.

This solution is O(m + n), where `m` is the length of the first string and `n`
is the length of the second string.

NOTE: We can also use a simple frequency counter.

Using an array
--------------
To examine if `t` is a rearrangement of `s`, we can count occurrences of each
letter in the two strings and compare them. We could use a hash map to count
the frequency of each letter, however, since both `s` and `t` only contain
letters from a-z, a simple array of size 26 will suffice.

We do not need two counters (or two loops), since we can increment the count
for each letter in `s` and decrement the count for each letter in `t`, and then
check if the count for every character is zero.

This is an example of using the index of an array as the key in a hash map.

Follow up: What if the inputs contain Unicode characters? How would you adapt
your solution to such a case?

The dict or Counter solution is still applicable, since a Unicode character is
still a hashable object.
"""

from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        d: dict[str, int] = {}
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1

        for c in t:
            if c in d:
                d[c] -= 1
                if d[c] == 0:
                    del d[c]

        return False if d else True


class SimplifiedSolution:
    """
    The following solution simplifies the original solution:
      * Uses a Counter instead of a dict. The Counter class is a specialized
        dictionary subclass for counting hashable objects.
    """
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
