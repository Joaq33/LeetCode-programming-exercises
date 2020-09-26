# Done
from collections import Counter


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for item in t:
            if t.count(item) > s.count(item):
                return item

    def findTheDifference2(self, s: str, t: str) -> str:
        return (Counter(t) - Counter(s)).popitem()[0]


obj = Solution()

s = "a"
t = "aa"
assert (ret := obj.findTheDifference(s, t)) == "a", ret
