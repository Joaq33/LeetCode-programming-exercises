from functools import reduce
from typing import List
import itertools


class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for i in range(1, len(nums) + 1):
            for subset in itertools.combinations(nums, i):
                ans += reduce(lambda x, y: x ^ y, subset)

        return ans
