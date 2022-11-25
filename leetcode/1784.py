"""
Given a binary string s without leading zeros,
return true if s contains AT MOST one contiguous segment of ones.
Otherwise, return false.

        not contains 01
101     -> false
110     -> true
1001    -> false
110     -> false
110001  -> false
10011   -> false
111     -> true
1       -> true
"""


class Solution:
    def checkOnesSegment(self, str_input: str) -> bool:
        return "01" not in str_input


if __name__ == '__main__':
    s = Solution()
    print(s.checkOnesSegment("111"))
