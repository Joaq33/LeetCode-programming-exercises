# Done
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]


obj = Solution()

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

obj.rotate(nums, k)
assert nums == [5, 6, 7, 1, 2, 3, 4], nums

print("Tests passed.")
