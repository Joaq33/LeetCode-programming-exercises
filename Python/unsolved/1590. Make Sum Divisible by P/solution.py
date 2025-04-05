from typing import List
from icecream import ic


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        target = sum(nums) % p

        if target == 0:
            return 0
        ic(target)
        presum = {0: -1}
        total = 0
        res = len(nums)
        for i in range(len(nums)):
            total += nums[i]
            mod = (total - target) % p
            if mod in presum:
                res = min(res, i - presum[mod])
            presum[total % p] = i
            ic(i,presum, total)

        return res if res != len(nums) else -1

    # def minSubarray(self, nums: List[int], p: int) -> int:
    #     total_sum = sum(nums)
    #     ic(total_sum)
    #     if total_sum % p == 0:
    #         return 0
    #
    #     for window_len in range(1, len(nums) ):
    #         ic(window_len, len(nums) - window_len + 1)
    #         for cur_pos in range(0, len(nums) - window_len + 1):
    #             cur_window = nums[cur_pos:cur_pos + window_len]
    #             sub_sum = sum(cur_window)
    #
    #             ic(cur_window, sub_sum)
    #             if (total_sum - sub_sum) % p == 0:
    #                 return window_len
    #
    #     return -1
