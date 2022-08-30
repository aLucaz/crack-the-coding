"""
Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. 
It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

"""
import re 

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        if paragraph == "":
            return paragraph
        words = re.split('[!?\',;. ]+', paragraph)
        words_dict = {}
        for word in words:
            if word != "":
                lower_word = word.lower()
                if words_dict.get(lower_word) is None: 
                    words_dict[lower_word] = 1
                else:
                    words_dict[lower_word] += 1
        words_dict = {k: v for k, v in sorted(words_dict.items(), key=lambda item: item[1], reverse=True)}
        for key in words_dict.keys():
            if key not in banned:
                return key

if __name__ == '__main__':
    res = Solution().mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
    print(res)