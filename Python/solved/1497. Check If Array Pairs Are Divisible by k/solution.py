from typing import List
from collections import defaultdict
from icecream import ic


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        """
        time: o(n)
        space: o(k)
        """
        x = [0] * k
        for i in arr:
            x[i % k] += 1
        if x[0] % 2 != 0: return False
        for i in range(1, k):
            if x[i] != x[k - i]:
                return False
        return True
