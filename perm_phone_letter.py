class Solution:
    def permu(self, ind, sub_string, digits, final_list, map_dict):
        if len(sub_string) == len(digits):
            final_list.append(sub_string)
            return

        for i in range(len(map_dict[digits[ind]])):
            sub_string += list(map_dict[digits[ind]])[i]
            self.permu(ind+1, sub_string, digits, final_list, map_dict)
            sub_string = sub_string[:-1]

    def letterCombinations(self, digits: str):
        map_dict = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",

        }
        final_list = []
        length = len(digits)
        if length == 1:
            final_list = [x for x in map_dict[digits]]
            return final_list

        sub_string = ''

        self.permu("", 0, sub_string, digits, final_list, map_dict)

        return final_list


print(Solution.letterCombinations("", "34"))
