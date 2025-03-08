"""
5. Longest Palindromic Substring

https://leetcode.com/problems/longest-palindromic-substring

NOTES
  * Use dynamic programming (2D), expansion around centers, or Manacher's
    Algorithm.

Brute force
-----------
The total number of operations to traverse all the substrings in a string of
length n is:

                             n(n + 1)(n + 2)
                             --------------- ≃ n^3
                                    6

So, a solution that finds the longest palindromic substring by checking all
possible substrings would have O(n^3) time complexity.

Dynamic programming
-------------------
It turns out, checking whether a string is a palindrome or not is a good
candidate for dynamic programming, as it displays the two necessary
characteristics of a dynamic programming problem:

  1. Optimal substructure: A single character or pair of characters is a
     palindrome. Additionally, larger palindromes are made of smaller
     palindromes. So, if we know a string is a palindrome, we only need to
     check the characters to the left and right of the string to determine if
     the next substring is a palindrome. This is the optimal substructure for
     the problem because it only requires one check, which can be done in
     constant time.

  2. Overlapping subproblems: To check if a substring is a palindrome, we must
     also check if the smaller substrings that make up the string are also
     palindromes. Since this inevitably will result in checking the same
     substring more than once, we can store the result of the check and reuse
     it for larger substrings.

First, we define our state, dp[i,j], where the palindromicity of the substring
s[i,j] is stored: 0 for false, 1 for true.

NOTE: A 2D array is used to represent both odd and even length palindromes,
where i and j represent the beginning and end of each substring.

Next, we define our base cases. There are essentially two base cases:

  1. Single-letter substrings are palindromes.
  2. Double-letter substrings of the same character are palindromes.

Programmatically, this results in the following:

  dp[i][i] = 1
  dp[i][i+1] = 1, if s[i] == s[i+1], otherwise 0.

Finally, we define the optimal substructure:

  >A palindrome can be expanded if s[i-1] and s[j+1] are equal. Therefore, a
   substring is a palindrome if the beginning and end characters are equal
   and the inner substring is also a palindrome.

This can be represented by the following recurrence relation:

  dp[i][j] = 1, if dp[i+1][j-1] == 1 ∧ s[i] == s[j], otherwise 0.

Since we start with the shortest substrings and iterate toward the longest
substrings, every time we find a new palindrome, it must be the longest one we
have seen so far. This removes an additional check against the current longest
palindromic substring.

Expansion around centers
------------------------
An improvement to the brute force approach involves expansion around each
potential palindrome's center, which brings the time complexity down to O(n^2)
(2*n-1 centers * n/2 comparisons).

Manacher's Algorithm builds from this trivial algorithm that is based on the
fact that a palindrome can be expanded if s[0] and s[n-1] are equal. The
expansion around centers algorithm is slow, however, requiring O(n^2) time
complexity.

Manacher's Algorithm
--------------------
We observe that palindromes with a common center form a contiguous chain, that
is, if we have a palindrome of length n centered at i, we also have palindromes
of length n-2, n-4, and so on also centered at i. Storing this information
allows us to make assertions about the possible length of other palindromic
substrings in the string. For example, given the string "abacaba", we observe
that the longest palindrome is centered at "c". Since, by definition, all
characters after "c" must be equal to all characters before "c", characters
within the radius of the palindrome centered at "c" must have at least the same
palindromic radius (i.e., the same longest palindrome) as the characters before
"c". Characters before "c" are commonly referred to as "mirrored" centers.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Uses dynamic programming (2D) with O(n^2) time and space complexity.
        """
        if not s:
            return ""

        start, end = 0, 0

        # Create an n x n matrix initialized to 0s.
        #
        #     a  b  a     j →
        #  a [0, 0, 0]  i        where, dp[0][0] = "a"
        #  b [-, 0, 0]  ↓               dp[1][1] = "b"
        #  a [-, -, 0]                  dp[2][2] = "a"
        #
        # NOTE: i and j are the beginning and end of the substring, therefore j
        # must be greater than or equal to i. For example, dp[2][0] does not
        # make sense.
        n = len(s)
        dp: list[list[int]] = [[0 for j in range(n)] for i in range(n)]

        # Set dp[i,i] to 1, accounting for the base case assertion that each
        # character is itself a palindrome.
        for i in range(n):
            dp[i][i] = 1

        # Set dp[i,i+1] to 1, if s[i] is equal to s[i+1], accounting for the
        # base case assertion that each pair of characters is a palindrome if
        # they are equal.
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                start, end = i, i + 1

        # Set dp[i,j] to 1, if s[i+1...j-1] is a palindrome (dp[i+1][j-1] == 1)
        # and s[i] is equal to s[j]. This is our recurrence relation, which
        # leverages the solutions to previous calculations.
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if dp[i + 1][j - 1] == 1 and s[i] == s[j]:
                    dp[i][j] = 1
                    start, end = i, j

        return s[start : end + 1]


class ExpansionAroundCentersSolution:
    def longestPalindrome(self, s: str) -> str:
        """
        A slow, O(n^2) algorithm that finds the longest palindromic substring
        by attempting to build a palindrome from each possible center. Odd
        length and even length palindromes are handled separately.
        """
        if not s:
            return ""

        start, end, maximum_length = 0, 0, 0

        # Check for odd length palindromes (centered at each character).
        for i in range(len(s)):
            left, right = i, i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > maximum_length:
                    maximum_length = current_length
                    start, end = left, right
                left -= 1
                right += 1

        # Check for even length palindromes (centered at each character pair).
        for i in range(len(s) - 1):
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                current_length = right - left + 1
                if current_length > maximum_length:
                    maximum_length = current_length
                    start, end = left, right
                left -= 1
                right += 1

        return s[start : end + 1]


class ManachersAlgorithmSolution:
    def longestPalindrome(self, s: str) -> str:
        """
        Manacher's Algorithm. Finds the longest palindromic substring of a
        string in linear time.
        """
        if not s:
            return ""

        # Create S' by inserting a separator character '|' between each
        # character. This allows for the consolidation of the odd and even
        # palindromic arrays into a single array. Odd palindromes are centered
        # around non-separator characters, even palindromes are centered around
        # separator characters.
        s_prime = "|" + "|".join(s) + "|"

        # A palindromic radii array is used to store the radius of the longest
        # palindrome centered on each character in S'. It is important to note
        # that `palindrome_radii` contains the radius of the palindrome, not
        # the length of the palindrome itself.
        palindrome_radii = [0] * len(s_prime)

        # NOTE: In some implementations `right` may be used instead of `radius`
        # to denote the boundary of palindrome centered at `center`.
        center, radius = 0, 0

        while center < len(s_prime):
            # Determine the longest palindrome centered at `center` starting
            # from s_prime[center - radius] and ending at
            # s_prime[center + radius]. This technique expands around a given
            # center, using the assertion that a palindrome can be expanded if
            # the start and end characters of the new substring are equal.
            while (
                center - (radius + 1) >= 0
                and center + (radius + 1) < len(s_prime)
                and s_prime[center - (radius + 1)] == s_prime[center + (radius + 1)]
            ):
                radius += 1

            # Store the radius of the longest palindrome in the array.
            palindrome_radii[center] = radius

            # The following is the algorithm's core optimization.

            # Save the center and radius of the original palindrome.
            original_center, original_radius = center, radius
            center, radius = center + 1, 0

            while center <= original_center + original_radius:
                # Calculate the "mirrored" center for the current center.
                mirrored_center = original_center - (center - original_center)
                # Calculate the maximum possible radius of the palindrome
                # centered at `center`.
                max_radius = original_center + original_radius - center

                # Case 1: Palindrome of mirrored center lies entirely within
                # the original palindrome.
                if palindrome_radii[mirrored_center] < max_radius:
                    palindrome_radii[center] = palindrome_radii[mirrored_center]
                    center += 1
                # Case 2: Palindrome of mirrored center extends beyond the
                # boundary of the original palindrome.
                elif palindrome_radii[mirrored_center] > max_radius:
                    palindrome_radii[center] = max_radius
                    center += 1
                # Case 3: Palindrome of mirrored center extends exactly up to
                # the boundary of the original palindrome.
                else:
                    radius = max_radius
                    break

        # The longest palindrome in S is formed from the center with the largest
        # radius.
        max_radius, max_center = 0, 0
        for i in range(len(palindrome_radii)):
            if palindrome_radii[i] > max_radius:
                max_radius, max_center = palindrome_radii[i], i

        # Convert back to indices in the original string.
        start, end = (max_center - max_radius) // 2, (max_center + max_radius - 1) // 2
        return s[start : end + 1]
