# https://leetcode.com/problems/longest-palindrome/description/
from collections import Counter
class LongestPalindrome:
    def longestPalindrome(self, s: str) -> int:
        characterCounts = Counter(s)

        atLeast1OddCount = False
        maxPalindromeLength = 0
        for key, value in characterCounts.items():
            if value % 2 == 0:
                maxPalindromeLength += value
            elif value % 2 == 1:
                maxPalindromeLength += value - 1
                atLeast1OddCount = True

        if atLeast1OddCount:
            maxPalindromeLength += 1

        return maxPalindromeLength