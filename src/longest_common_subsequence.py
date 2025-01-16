"""
1143. Longest Common Subsequence

https://leetcode.com/problems/longest-common-subsequence

NOTES
  * Use dynamic programming (2D) or recursion.

A common subsequence is a sequence of letters that appears in both strings. Not
every letter in the string has to be used, but letters cannot be rearranged. In
essence, a subsequence of a string 's' is a string we get by deleting some
letters in 's'.

The most obvious approach would be to iterate through each subsequence of the
first string and check whether or not it is also a subsequence of the second
string. This, however, will require exponential time to run. The number of
subsequences in a string is up to 2^L, where L is the length of the string.

There are a couple of strategies we can use to design a tractable
(non-exponential) algorithm for an optimization problem:

  1. Identifying a greedy algorithm
  2. Dynamic programming

There is no guarantee that either is possible. Additionally, greedy algorithms
are strictly less common than dynamic programming algorithms and are often more
difficult to identify. However, if a greedy algorithm exists, then it will
almost always be better than a dynamic programming one. You should, therefore,
at least give some thought to the potential existence of a greedy algorithm
before jumping straight into dynamic programming.

Recall that there are two different techniques we can use to implement a
dynamic programming solution: tabulation and memoization.

  * Tabulation uses a table to keep track of subproblem results and works in a
    bottom-up manner: solving the smallest subproblems before the large ones,
    in an iterative manner. Often, people use the words "tabulation" and
    "dynamic programming" interchangeably.

  * Memoization is where we add caching to a function (that has no side
    effects). In dynamic programming, it is typically used on recursive
    functions for a top-down solution that starts with the initial problem and
    then recursively calls itself to solve smaller problems. Memoization is
    useful when a problem has overlapping subproblems.
"""


class Solution:
    """
    Observe that the subproblems have a natural "size" ordering; the largest
    subproblem is the one we start with, and the smallest subproblems are the
    ones with just one letter left in each word. The answer for each subproblem
    depends on the answers to some of the smaller subproblems.

    Remembering too that each subproblem is represented as a pair of indexes,
    and that there are text1.length() * text2.length() such possible
    subproblems, we can iterate through the subproblems, starting from the
    smallest ones, and storing the answer for each. When we get to the larger
    subproblems, the smaller ones that they depend on will already have been
    solved. The best way to do this is to use a 2D array.

    There are two cases when considering the optimal solution of the
    subproblem:

      1. The first letter of both strings are the same.
      2. The first letter of both strings are not the same.
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Given two strings, `text1` and `text2`, compute the length of their
        Longest Common Subsequence (LCS).
        """
        # Create an m×n matrix initialized to 0s, where m is the number of rows
        # (|text1| + 1) and n is the number of columns (|text2| + 1).
        #
        # dp[0...m, 0] and dp[0, 0...n] are set to 0. This represents our base
        # case:
        #
        #   If either sequence is empty, the LCS length is 0.
        m, n = len(text1) + 1, len(text2) + 1
        dp: list[list[int]] = [[0 for j in range(n)] for i in range(m)]

        # Fill the remaining matrix for all remaining prefixes. For each
        # position dp[i][j], we calculate:
        #
        #   If text1[i-1] == text2[j-1], dp[i][j] = 1 + dp[i-1][j-1]
        #
        # This means we include the current matching character and add 1 to the
        # previous LCS length.
        #
        #   Else, dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        #
        # This means we take the maximum LCS length when excluding either the
        # current character from sequence `text1` or sequence `text2`.
        for i in range(1, m):
            for j in range(1, n):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],  # Exclude the character at position i in `text1`
                        dp[i][j - 1],  # Exclude the character at position j in `text2`
                    )
        # NOTE: dp[m - 1][n - 1] is equivalent to dp[i][j].
        return dp[m - 1][n - 1]


class AlternativeSolution:
    """
    Typically, the length of the Longest Common Subsequence (LCS) is given by
    the value of dp[i][j], however, we can also solve the problem in reverse.
    This results in the solution being located at dp[0][0]. Though slightly
    less intuitive, this allows us to use the same indices for the string and
    matrix.
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Given two strings, `text1` and `text2`, compute the length of their
        Longest Common Subsequence (LCS) using a reverse iteration approach.
        """
        # Initializing the table to 0 allows us to calculate the current
        # subproblem from previous subproblems.
        #
        #     a c e -    j →
        #   a 0 0 0 0  i
        #   b 0 0 0 0  ↓
        #   c 0 0 0 0
        #   d 0 0 0 0
        #   e 0 0 0 0
        #   - 0 0 0 0
        #
        #     a c e -    j →
        #   a 3 2 1 0  i
        #   b 2 2 1 0  ↓
        #   c 2 2 1 0
        #   d 1 1 1 0
        #   e 1 1 1 0
        #   - 0 0 0 0
        m, n = len(text1) + 1, len(text2) + 1
        dp: list[list[int]] = [[0 for j in range(n)] for i in range(m)]

        # Iterate over the table in reverse (first by column, then by row).
        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                # 1. The first letter of both strings are the same.
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                # 2. The first letter of both strings are *not* the same.
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]


class MemoizationSolution:
    """
    Some subproblems may be visited multiple times. As such, we should memoize
    the results of `lcs()` calls so that the answers of previously computed
    subproblems can immediately be returned without the need for
    re-computation.
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Given two strings, `text1` and `text2`, compute the length of their
        Longest Common Subsequence (LCS) using memoization.
        """
        # Initializing the memoization table to -1 allows us to determine
        # whether or not the value has been calculated.
        #
        #     a c e    j →
        #   a . . .  i
        #   b . . .  ↓
        #   c . . .
        #   d . . .
        #   e . . .
        m, n = len(text1), len(text2)
        memo: list[list[int]] = [[-1 for j in range(n)] for i in range(m)]

        def lcs(s1: str, s2: str, memo: list[list[int]]) -> int:
            if not s1 or not s2:
                return 0
            # Calculate current position in memo table
            i, j = len(memo) - len(s1), len(memo[0]) - len(s2)
            # Check whether we've already solved the given subproblem.
            if memo[i][j] != -1:
                return memo[i][j]
            if s1[0] == s2[0]:
                memo[i][j] = 1 + lcs(s1[1:], s2[1:], memo)
            else:
                memo[i][j] = max(lcs(s1[1:], s2, memo), lcs(s1, s2[1:], memo))
            return memo[i][j]

        return lcs(text1, text2, memo)


class RecursiveSolution:
    """
    For problems like this, it is helpful to first break the problem down into
    its smallest subproblems and build up a solution from there.

    For example:

      Given two strings "abcde" (text1) and "ace" (text2), we can first break
      the problem down into the following base cases:

        1. If text1 = "" and text2 = "", return 0
        2. If text1 = "a" and text2 = "", return 0
        3. If text1 = "" and text2 = "a", return 0

      Next, we build upon the base cases with simplified cases for the general
      case:

        1. If text1 = "a" and text2 = "a", return 1
        2. If text1 = "ab" and text2 = "ac", return 1 + lcs("b", "c")
        3. If text1 = "bc" and text2 = "ac", return
           max(lcs("bc", "c"), lcs("c", "ac"))

      The third case is the most tricky to intuit, however, we are simply
      determining the longest subsquence using the next character in both
      strings.

      Finally, we formalize the above cases in code.

    This solution is O(2^(M + N)), where `M` is the length of the first string
    and `N` is the length of the second string.

    NOTE: Though *technically* correct, this solution exceeds the time limit,
    since it does not account for overlapping subproblems.
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Given two strings, `text1` and `text2`, compute the length of their
        Longest Common Subsequence (LCS) using pure recursion.
        """
        def lcs(s1: str, s2: str) -> int:
            if not s1 or not s2:
                return 0
            if s1[0] == s2[0]:
                return 1 + lcs(s1[1:], s2[1:])
            return max(lcs(s1[1:], s2), lcs(s1, s2[1:]))

        return lcs(text1, text2)
