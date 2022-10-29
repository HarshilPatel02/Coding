class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        t_list = [x for x in t]
        s_list = [x for x in s]
        t_list.sort()
        s_list.sort()
#         for i in s:
#             if i in t_list:
#                 t_list.remove(i)
#             else:
#                 return False

#         return True

        if t_list == s_list:
            return True
        else:
            return False

#        Runtime: 54 ms, faster than 90.55% of Python3 online submissions for Valid Anagram.
# Memory Usage: 15.1 MB, less than 11.75% of Python3 online submissions for Valid Anagram.
