"""

Given a string return the longest palidrome substring

Approach #1 recursion

P(babad) -> Max(P(baba), P(abad)))
P(baba) -> Max(P(bab), P(aba)))
P(abad) -> Max(P(aba), P(bad)))

Efficiency On^2
Space On^2

Approach #2 dynamic programmming

P(i, j) = P(i+1, j-1) and Si == Sj

j - i + 1 == 2 and Si == Sj => true

example
string -> cfafs
[
#  0 1 2 3 4
0 [1 0 0 0 0],
1 [0 1 0 0 0],
2 [0 0 1 0 0],
3 [0 0 0 1 0],
4 [0 0 0 0 1],
]

result
[
#  0 1 2 3 4
0 [1 1 0 0 0]
1 [0 1 1 1 0]
2 [0 0 1 1 0]
3 [0 0 0 1 1]
4 [0 0 0 0 1]
]

for j 1 -> len (all string)
    for i  0 -> j-1 (only upper slide)

"""


class Solution:

    # this is based on the solution given by leetcode
    def longestPalindromeSecondApproach(self, s_input: str):
        size = len(s_input)
        p = [[False] * size for _ in range(size)]
        for i in range(size):
            p[i][i] = True
        longest = s_input[0]
        for j in range(0, size):
            for i in range(0, j):
                n_elems = j - i + 1
                if s_input[i] == s_input[j]:
                    if p[i + 1][j - 1] or n_elems == 2:
                        p[i][j] = True
                        # updating longest
                        if n_elems > len(longest):
                            start = i
                            end = j + 1
                            longest = s_input[start:end]
        return "".join(longest)

    def longestPalindromeFirstApproach(self, s_input: str) -> str:
        if len(s_input) == 1 or s_input == s_input[::-1]:
            return s_input
        left = self.longestPalindromeFirstApproach(s_input[:-1])
        left_len = len(left)
        right = self.longestPalindromeFirstApproach(s_input[1:])
        right_len = len(right)
        return left if left_len > right_len else right

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]

    # this is the best solutions i found, this is NOT my approach [TODO: analize mentall process to do this]
    def longestPalindrome(self, s: str) -> str:
        if self.isPalindrome(s):
            return s
        max_length = 1
        start = 0
        for i in range(1, len(s)):
            one_more_letter_word = s[i-max_length:i+1]
            two_more_letter_word = s[i-max_length-1:i+1]

            if self.isPalindrome(two_more_letter_word) and i-max_length-1 >= 0:
                start = i - max_length - 1
                max_length += 2
            elif self.isPalindrome(one_more_letter_word):
                start = i - max_length
                max_length += 1
        return s[start:start+max_length]

if __name__ == '__main__':
    s = Solution().longestPalindrome("babad")
    print(s)
