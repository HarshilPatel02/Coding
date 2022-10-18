class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)

        rev_s = s[::-1]

        if s.startswith(rev_s[:length//2 - 1]):
            return s
        else:
            return False


objt = Solution()
print(objt.longestPalindrome("abbab"))
