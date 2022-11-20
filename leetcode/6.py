"""
 Zig Zag Conversion

example 1:

Input: s = "PAYPALISHIRING", numRows = 3

P   A   H   N
A P L S I I G
Y   I   R

Output: "PAHNAPLSIIGYIR"

example 2:

Input: s = "PAYPALISHIRING", numRows = 4

P     I    N
A   L S  I G
Y A   H R
P     I

Output: "PINALSIGYAHRPI"


On

"""


class Solution:

    def convert(self, input_str: str, n_rows: int) -> str:
        levels = [""] * n_rows
        level = 0
        forward = True
        for input_char in input_str:
            levels[level] += input_char

            if level == n_rows - 1:
                forward = False
            elif not forward and level == 0:
                forward = True

            if forward:
                level += 1
            else:
                level -= 1

        return "".join(levels)


if __name__ == '__main__':
    s = Solution()
    response = s.convert("PAYPALISHIRING", 3)
    print(response)
