from typing import List
from icecream import ic


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        time limit exceeded
        time complexity: O(n^2)
        space complexity: O(1)
        :param nums: List of integers representing the input array
        :type nums: List[int]
        :return: The maximum absolute sum of any subarray
        :rtype: int
        """
        ans = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                ans = max(abs(sum(nums[i:j])), ans)
        return ans

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        calculating in positives and in negatives separately
        time complexity: O(n)
        space complexity: O(1)
        :param nums: List of integers representing the input array
        :type nums: List[int]
        :return: The maximum absolute sum of any subarray
        :rtype: int
        """
        ansmin = ansmax = curmin = curmax = 0
        for point in nums:
            curmin += point
            curmax += point
            if curmin > 0:
                curmin = 0
            if curmax < 0:
                curmax = 0
            ansmin = min(curmin, ansmin)
            ansmax = max(curmax, ansmax)

        return max(-ansmin, ansmax)
