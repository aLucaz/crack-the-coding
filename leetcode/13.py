"""
Roman To Integer

I             1 ->
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.


III -> 1 (next in V, X) + 1 + 1 = 3
LVIII -> 50 + 5 + 1 + 1 + 1 = 58
MCMXCIV -> 1000 + 100 + 1000 + 10 + 100 + 1 + 5 = 2216 mal


complexity: On
space: On
"""


class Solution:
    values = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    subs = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}

    def romanToInt(self, s: str) -> int:
        res_list = []
        for i, c in enumerate(s):
            val = self.values.get(c)
            if i < len(s) - 1:
                opp = self.getOpp(c, s[i + 1])
                res_list.append(val * opp)
            else:
                res_list.append(val)
        return sum(res_list)

    def getOpp(self, c, c_next):
        opps = self.subs.get(c)
        if opps is not None:
            if c_next in opps:
                return -1
        return 1


if __name__ == '__main__':
    s = Solution()
    r = s.romanToInt("MCMXCIV")
    print(r)
