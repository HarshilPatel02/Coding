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
