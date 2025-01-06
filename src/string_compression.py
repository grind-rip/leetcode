"""
443. String Compression

https://leetcode.com/problems/string-compression

NOTES
  * This is an example of run-length encoding (RLE), a form of lossless data
    compression in which runs of data (consecutive occurrences of the same data
    value) are stored as a single occurrence of that data value and a count of
    its consecutive occurrences, rather than as the original run.

An important caveat of this problem is the following:

  >You must write an algorithm that uses only constant extra space.

This means that regardless of the size of 'chars', the solution must use the
same amount of memory, i.e., you cannot use a new string or array.

So, given this constraint, we can assume that the original array 'chars' must
be used to store the solution, the encoded string. Given that the array of the
encoded string will contain at most 'n' elements, this is tractable.

The solution is pretty straight-forward and can be solved in linear runtime
complexity, O(n), and constant space complexity, O(1).

We start with two pointers:
  * `wp`: write pointer, which points to the current position in `chars` to
     write.
  * `cc`: current character, which points to the current character for which to
     count consecutive occurrences.

Starting from index 1 of the array of characters (we can skip the 0th index
and simply set count to 1), we check if chars[i] is equal to chars[cc]:

  0   1   2   3   4   5   6
["a","a","b","b","c","c","c"]  count = 1
  ^   ^
  wp
  cc
      i

If they are equal, increment the count by 1 (count += 1) and increment i:

  0   1   2   3   4   5   6
["a","a","b","b","c","c","c"]  count = 2
  ^       ^
  wp
  cc
          i

If they are not equal, first write the previous encoding:
  * If count is greater than 1, write the current character and the string
    representation of count.
  * Else (if count is equal to 1), write the current character.
Increment the write pointer to the next position in the character string to
write.
Increment the current character pointer to the next non-matching character

  0   1   2   3   4   5   6
["a","2","b","b","c","c","c"]  count = 1
          ^
          wp
          cc
          i


  0   1   2   3   4   5   6
["a","2","b","b","c","c","c"]  count = 2
          ^   ^
          wp
          cc
              i

  0   1   2   3   4   5   6
["a","2","b","2","c","c","c"]  count = 1
                  ^
                  wp
                  cc
                  i

  0   1   2   3   4   5   6
["a","2","b","2","c","c","c"]  count = 2
                  ^   ^
                  wp
                  cc
                      i

  0   1   2   3   4   5   6
["a","2","b","2","c","c","c"]  count = 3
                  ^       ^
                  wp
                  cc
                          i

Finally, handle the final group of consecutive repeating characters and
truncate the character array at wp + 1. We can remove the last element in the
array (a constant time operation) until the write pointer is reached.
"""


class Solution:
    def compress(self, chars: list[str]) -> int:
        # Initialize a write pointer (wp), a current character pointer (cc),
        # and count (number of repeating characters). count is initialized to
        # 1, since logically, we cannot have a group of 0 consecutive repeating
        # characters.
        wp, cc, count = 0, 0, 1

        # Iterate over the character array. If the ith character in the array
        # is the same as the current character, increment count. Otherwise,
        # overwrite the array using the write pointer.
        for i in range(1, len(chars)):
            if chars[cc] == chars[i]:
                count += 1
            else:
                chars[wp] = chars[cc]
                wp += 1
                if count > 1:
                    for x, c in enumerate(str(count)):
                        chars[wp] = c
                        wp += 1
                # Reset count to 1. Move current character pointer to i (the
                # next non-repeating character).
                count = 1
                cc = i

        # Handle the final group of consecutive repeating characters.
        chars[wp] = chars[cc]
        wp += 1
        if count > 1:
            for i, c in enumerate(str(count)):
                chars[wp] = c
                wp += 1

        # Modify the input array by removing elements up to and including the
        # final position of the write pointer.
        #
        # NOTE: Removal from the end of an array does not require characters to
        # be shifted, and can therefore be done in constant time.
        #
        # NOTE: You cannot create a slice of the input array, as this creates a
        # new list in memory.
        right = len(chars) - 1
        while right >= wp:
            chars.pop()
            right -= 1

        return len(chars)


class SimplifiedSolution:
    """
    The following solution simplifies the original solution:
      * Removes the need for a separate cc (current character) pointer by
        comparing the current character (i) to the previous character (i-1).
      * Eliminates duplicate code for handling the final group by extending the
        loop range.
      * Makes the cleanup loop more straightforward.
    The algorithm still maintains O(n) time complexity and O(1) space
    complexity, but is more concise.
    """
    def compress(self, chars: list[str]) -> int:
        # Initialize a write pointer (wp) and count (number of repeating
        # characters). count is initialized to 1, since logically, we cannot
        # have a group of 0 consecutive repeating characters.
        wp, count = 0, 1

        # Iterate over the character array. If the ith character in the array
        # is the same as the (i-1)th character, increment count. Otherwise,
        # overwrite the array using the write pointer. For the final iteration,
        # (i = len(chars)), handle the final group of consecutive repeating
        # characters.
        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                count += 1
            elif count:
                chars[wp] = chars[i - 1]
                wp += 1
                if count > 1:
                    for digit in str(count):
                        chars[wp] = digit
                        wp += 1
                count = 1

        # Modify the input array by removing elements up to and including the
        # final position of the write pointer.
        #
        # NOTE: Removal from the end of an array does not require characters to
        # be shifted, and can therefore be done in constant time.
        #
        # NOTE: You cannot create a slice of the input array, as this creates a
        # new list in memory.
        while len(chars) > wp:
            chars.pop()

        return wp
