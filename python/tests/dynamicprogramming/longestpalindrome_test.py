from src.dynamicprogramming.longestpalindrome import LongestPalindrome

class TestLongestPalindrome:
    def test_case_5(self):
        obj = LongestPalindrome()
        assert obj.longestPalindrome('bb') == 2

    def test_case_30(self):
        obj = LongestPalindrome()
        assert obj.longestPalindrome('bananas') == 5
