class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        temp = s

        for i in range(length, 1, -1):
            ini = 0

            while ini + i <= length:

                s = temp[ini:ini + i]

                rev_s = s[::-1]

                if s.startswith(rev_s):
                    return rev_s
                ini += 1

        return s[0]


objt = Solution()
print(objt.longestPalindrome("absdfddsdf"))
