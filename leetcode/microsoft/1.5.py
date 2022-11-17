"""

Given a string return the longest palidrome substring

b -> true
ba -> false
bab -> true
baba -> false
babad -> false
abad -> false
bad -> false
ad -> false
d -> true

P(babad) -> Max(P(baba), P(abad)))
P(baba) -> Max(P(bab), P(aba)))
P(abad) -> Max(P(aba), P(bad)))

On^2

"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or self.isPalindrome(s):
            return s
        left = self.longestPalindrome(s[:-1])
        left_len = len(left)
        right = self.longestPalindrome(s[1:])
        right_len = len(right)
        return left if left_len > right_len else right


if __name__ == '__main__':
    s = Solution().longestPalindrome("babad")
    print(s)
