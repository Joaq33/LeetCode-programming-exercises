# Done
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int: #copied
        if len(nums) == 0:
            return 0
        length = [1] * len(nums)
        count = [1] * len(nums)
        length[0], count[0] = 1, 1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
                    elif length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = count[j]
        max_len = max(length)
        return sum([count[i] for i in range(len(count)) if length[i] == max_len])



obj = Solution()

nums = [1, 2, 4, 3, 5]
assert (ret := obj.findNumberOfLIS(nums)) == 2, ret
