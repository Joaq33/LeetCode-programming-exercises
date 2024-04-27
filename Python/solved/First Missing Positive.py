# Done 96.31%
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        cur = 1
        s_nums = set(nums)
        while cur in s_nums:
            cur += 1
        return cur


obj = Solution()

param_nums = [7, 8, 9, 11, 12]
assert (ret := obj.firstMissingPositive(param_nums)) == 1, ret

print("Tests passed")
