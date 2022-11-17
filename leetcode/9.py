class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        n = len(x_str) - 1
        x_str_rev = ''
        for i in range(n, -1, -1):
            x_str_rev = x_str_rev + x_str[i]
        print(n, x_str, x_str_rev)
        return x_str == x_str_rev


if __name__ == '__main__':
    print(Solution().isPalindrome(1234321))
