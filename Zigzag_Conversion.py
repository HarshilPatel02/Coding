class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1 or len(s) <= numRows:
            return s
        elif numRows == 2:
            first, second = '', ''
            for i in range(0, len(s), 2):
                first += s[i]
                if i + 1 < len(s):
                    second += s[i+1]
            return first + second

        final_list = [s[x] for x in range(numRows)]
        for i in range(numRows, len(s), 2*numRows-2):
            for j in range(numRows-2):
                if i + j < len(s):
                    final_list[numRows-2-j] += s[i + j]
                else:
                    return "".join(final_list)
            for j in range(numRows):
                if i + j + numRows - 2 < len(s):
                    final_list[j] += s[i + j + numRows - 2]
                else:
                    return "".join(final_list)
        return "".join(final_list)
