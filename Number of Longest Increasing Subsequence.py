# Done
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int: #copied
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = []  # dp[i]: the length of LIS ends with nums[i]
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp) if dp else 0


obj = Solution()

nums = [1, 2, 4, 3, 5]
assert (ret := obj.findNumberOfLIS(nums)) == 2, ret
