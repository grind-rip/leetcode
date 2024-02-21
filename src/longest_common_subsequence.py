"""
1143. Longest Common Subsequence

https://leetcode.com/problems/longest-common-subsequence

NOTES
  * Use dynamic programming (2D) or recursion.

  * A common subsequence is a sequence of letters that appears in both strings.
    Not every letter in the strings has to be used, but letters cannot be
    rearranged. In essence, a subsequence of a string 's' is a string we get by
    deleting some letters in 's'.

  * The most obvious approach would be to iterate through each subsequence of
    the first string and check whether or not it is also a subsequence of the
    second string. This, however, will require exponential time to run. The
    number of subsequences in a string is up to 2^L, where L is the length of
    the string.

  * There are a couple of strategies we use to design a tractable
    (non-exponential) algorithm for an optimization problem:

      1. Identifying a greedy algorithm
      2. Dynamic programming

  * There is no guarantee that either is possible. Additionally, greedy
    algorithms are strictly less common than dynamic programming algorithms and
    are often more difficult to identify. However, if a greedy algorithm
    exists, then it will almost always be better than a dynamic programming
    one. You should, therefore, at least give some thought to the potential
    existence of a greedy algorithm before jumping straight into dynamic
    programming.

  * Recall that there are two different techniques we can use to implement a
    dynamic programming solution; memoization and tabulation.

      * Memoization is where we add caching to a function (that has no side
        effects). In dynamic programming, it is typically used on recursive
        functions for a top-down solution that starts with the initial problem
        and then recursively calls itself to solve smaller problems.

      * Tabulation uses a table to keep track of subproblem results and works
        in a bottom-up manner: solving the smallest subproblems before the
        large ones, in an iterative manner. Often, people use the words
        "tabulation" and "dynamic programming" interchangeably.
"""

from typing import List


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

    Remembering back to the memoization solution, there were two cases.

      1. The first letter of both strings are the same.
      2. The first letter of both strings are *not* the same.
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Initializing the table to 0 allows us to calculate the current
        # subproblem from previous subproblems.
        #
        #     a b c d e -    i →
        #   a 0 0 0 0 0 0  j
        #   c 0 0 0 0 0 0  ↓
        #   e 0 0 0 0 0 0
        #   - 0 0 0 0 0 0
        #
        #     a b c d e -    i →
        #   a 3 2 2 1 1 0  j
        #   c 2 2 2 1 1 0  ↓
        #   e 1 1 1 1 1 0
        #   - 0 0 0 0 0 0
        #
        # where a,a is (0,0) and e,e is (5,3) (for i,j).
        col, row = len(text1) + 1, len(text2) + 1
        dp: List[List[int]] = [[0 for _ in range(col)] for _ in range(row)]

        # Iterate over the table in reverse (first by column, then by row).
        for i in reversed(range(len(text2))):
            for j in reversed(range(len(text1))):
                # 1. The first letter of both strings are the same.
                if text1[j] == text2[i]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                # 2. The first letter of both strings are *not* the same.
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        # NOTE: Uncomment to print the result of the table.
        # for r in dp:
        #     print(r)
        return dp[0][0]


class MemoizationSolution:
    """
    Some subproblems may be visited multiple times. As such, we should memoize
    the results of `lcs()` calls so that the answers of previously computed
    subproblems can immediately be returned without the need for
    re-computation.
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Initializing the memoization table to -1 allows us to determine
        # whether or not the value has been calculated.
        #
        #     a b c d e    i →
        #   a . . . . .  j
        #   c . . . . .  ↓
        #   e . . . . .
        #
        # where a,a is (0,0) and e,e is (5,3) (for i,j).
        col, row = len(text1), len(text2)
        memo: List[List[int]] = [[-1 for _ in range(col)] for _ in range(row)]

        def lcs(s1: str, s2: str, memo: List[List[int]]) -> int:
            col, row = len(memo[0]), len(memo)
            if s1 == "" or s2 == "":
                return 0
            # Check whether we've already solved the given subproblem.
            i, j = row - len(s2), col - len(s1)
            if memo[i][j] != -1:
                return memo[i][j]
            if s1[0] == s2[0]:
                memo[i][j] = 1 + lcs(s1[1:], s2[1:], memo)
            else:
                memo[i][j] = max(lcs(s1[0:], s2[1:], memo), lcs(s1[1:], s2[0:], memo))
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

    This solution is O(M x N), where where `M` is the length of the first
    string and `N` is the length of the second string.

    NOTE: This solution exceeds the time limit.
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def lcs(s1: str, s2: str) -> int:
            if s1 == "" or s2 == "":
                return 0
            if s1[0] == s2[0]:
                return 1 + lcs(s1[1:], s2[1:])
            return max(lcs(s1[0:], s2[1:]), lcs(s1[1:], s2[0:]))

        return lcs(text1, text2)
