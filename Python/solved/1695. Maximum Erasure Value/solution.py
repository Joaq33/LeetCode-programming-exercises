from typing import List
from icecream import ic


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        """
        sliding window approach
        time complexity: o(n)
        space complexity: o(n)
        :param nums:
        :return:
        """
        print(nums, nums[0])
        track = {nums[0]}
        ans = cur = nums[0]
        ic(ans, track)
        left = 0
        right = 1
        while right < len(nums):
            while nums[right] in track:
                track.remove(nums[left])
                cur -= nums[left]
                left += 1
            track.add(nums[right])
            cur += nums[right]
            ans = max(ans, cur)
            ic(ans, track)
            right += 1
        return ans