from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_acc = -1
        for account in accounts:
            money = sum(account)
            if money > max_acc:
                max_acc = money
        return max_acc


if __name__ == '__main__':
    res = Solution().maximumWealth([[1, 2, 3], [2, 4, 5]])
    print(res)
