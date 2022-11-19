"""
Longest Substring Without Repeating Character

abcabcedbb -> abc -> 3
{a} m=1
{a, b} m=2
{a, b, c} m=3
{b, c, a} m=3
{c, a, b} m=3
{a, b, c} m=3
{a, b, c, e} m=4
{a, b, c, e, d} m= 5
{b, c, e, d}
{c, e, d}
{c, e, d, b} m=4
{}

"""


class Solution:

    def customLengthOfLongestSubstring(self, s: str) -> int:
        m = -1
        substring = []
        i = 0
        while i < len(s):
            if s[i] not in substring:
                substring.append(s[i])
            else:
                m = max(m, len(substring))
                substring.pop(0)
                i -= 1
            i += 1
        m = max(m, len(substring))
        return m

    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        l = set()
        m = 0
        i = 0
        j = 0
        while i < len(s):
            if s[i] not in l:
                l.add(s[i])
                i += 1
            else:
                m = max(m, len(l))
                l.remove(s[j])
                j += 1
        m = max(m, len(l))
        return m


if __name__ == '__main__':
    s = Solution()
    res = s.lengthOfLongestSubstring("abcabcbb")
    print(res)
    res2 = s.customLengthOfLongestSubstring("abcabcbb")
    print(res2)
