"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".
    Otherwise, we define that this word doesn't use capitals in a right way.

    O(n)
"""


class Solution:
    @staticmethod
    def detect_capital_use(word: str) -> bool:
        checker_capital = True
        cont = 1
        if word.islower():
            checker_capital = True
        elif not word.isupper():
            for letter in word:
                if not letter.isupper() and cont == 1:
                    checker_capital = False
                    break
                if letter.isupper() and cont != 1:
                    checker_capital = False
                    break
                cont += 1
        return checker_capital


if __name__ == "__main__":
    print(Solution.detect_capital_use("Bebecita"))
    print(Solution.detect_capital_use("BebeLinY"))
    print(Solution.detect_capital_use("bebelin"))
