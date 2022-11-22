"""
Group Anagrams

given an array of string, group the anagrams together. you can return the answer in any order

ate, eat and tea are anagrams

example
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Input: strs = [""]
Output: [[""]]

Input: strs = ["a"]
Output: [["a"]]
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = [[stre] for stre in strs]
        lout = len(out)
        for i in range(0, lout):
            j = i + 1
            while j < lout:
                if self.same(out[i], out[j]):
                    out[i].extend(out[j])
                    out.pop(j)
                    lout = len(out)
                else:
                    j += 1
        return out

    def same(self, l1, l2):
        inter1 = [c for c in l1[0] if c in l2[0]]
        inter2 = [c for c in l2[0] if c in l1[0]]
        return len(inter1) == len(inter2) == len(l1[0]) == len(l2[0])


if __name__ == '__main__':
    s = Solution()
    r = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(r)
