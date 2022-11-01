class Solution:
    def firstUniqChar(self, s: str) -> int:
        uni_dict = {}

        for i in s:
            if i in uni_dict.keys():
                uni_dict[i] += 1
            else:
                uni_dict[i] = 1

        for i in uni_dict:
            if uni_dict[i] == 1:
                return s.index(i)

        return -1


# Success
# Details
# Runtime: 54 ms, faster than 51.40% of Python3 online submissions for First Letter to Appear Twice.
# Memory Usage: 13.9 MB, less than 50.76% of Python3 online submissions for First Letter to Appear Twice.
