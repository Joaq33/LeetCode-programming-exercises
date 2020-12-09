from typing import List
from collections import defaultdict


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        complements = defaultdict(int)
        ans = 0
        for i in time:
            remain = i % 60
            if remain == 0 and i != 0:
                ans += complements[60]
                complements[60] += 1
                continue
            dif = 60 - remain
            ans += complements[dif]
            complements[remain] += 1
        return ans


obj = Solution()

time = [30, 20, 150, 100, 40]
assert 3 == (ret := obj.numPairsDivisibleBy60(time)), ret

time = [60, 60, 60]
assert 3 == (ret := obj.numPairsDivisibleBy60(time)), ret

print("Tests passed.")
