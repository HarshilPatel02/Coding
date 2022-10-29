class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine_list = [i for i in magazine]

        for i in ransomNote:
            if i in magazine_list:
                magazine_list.remove(i)
            else:
                return False

        return True
