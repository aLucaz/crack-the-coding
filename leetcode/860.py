"""


Complexity On

"""
from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        revenue = {5: 0, 10: 0, 20: 0}
        for i, b in enumerate(bills):
            turned = b - 5
            if turned == 0:
                revenue[5] += 5
                continue

            if turned == 15:
                has_turned_in_10_n_5 = (revenue[5] > 0) and (revenue[10] > 0) and (revenue[10] + revenue[5] >= turned)
                if has_turned_in_10_n_5:
                    revenue[5] -= 5
                    revenue[10] -= 10
                    revenue[b] += b
                    continue

            has_turned_in_5 = revenue[5] >= turned
            if has_turned_in_5:
                revenue[5] -= (b - 5)
                revenue[b] += b
                continue

            return False

        return True


if __name__ == '__main__':
    s = Solution()
    r1 = s.lemonadeChange([5, 5, 5, 10, 20])
    print(r1)
    r2 = s.lemonadeChange([5, 5, 10, 10, 20])
    print(r2)
    r3 = s.lemonadeChange([5, 5, 5, 10, 5, 5, 10, 20, 20, 20])
    print(r3)
    r4 = s.lemonadeChange([5, 10, 5, 20, 5, 10, 5, 20])
    print(r4)
    r5 = s.lemonadeChange([5, 5, 5, 5, 20, 20, 5, 5, 5, 5])
    print(r5)
