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
