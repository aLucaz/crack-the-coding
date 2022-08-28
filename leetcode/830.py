"""
In a string S of lowercase letters, these letters form consecutive groups of the same character.
For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
The final answer should be in lexicographic order.

Note:  1 <= S.length <= 1000

O(n)
"""


class Solution:
    def large_group_positions(self, S: str):
        start = 0
        end = 0
        output = []
        size = len(S)
        while True:
            if end == size - 1:
                output = self.evaluate(output, start, end, True)
                break
            if S[start] == S[end]:
                end = end + 1
            if S[start] != S[end]:
                output = self.evaluate(output, start, end, False)
                start = end
        return output

    @staticmethod
    def evaluate(output, start, end, last):
        if last:
            if end - start >= 2:
                output.append([start, end])
        else:
            if end - start >= 3:
                output.append([start, end - 1])
        return output


if __name__ == '__main__':
    print(Solution().large_group_positions("aaaaa"))
