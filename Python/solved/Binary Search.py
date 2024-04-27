# Done
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # @profile
        def bs(left, right):
            if right - left == 0:
                return -1
            print(left + ((right - left) >> 1))
            print(left + ((right - left) // 2))
            pivot = left + (right - left) // 2
            cur = nums[pivot]

            if cur == target:
                return pivot
            if target < cur:
                return bs(left, pivot)
            else:
                return bs(pivot + 1, right)

        return bs(0, len(nums))
    def search2(self, nums: List[int], target: int) -> int:
        """
        The best answer in the page
        :param nums:
        :param target:
        :return:
        """
        left, right = 0, len(nums)-1
        while left <= right:
            pivot = (left + right)//2
            if target == nums[pivot]:
                return pivot
            if target > nums[pivot]:
                left = pivot+1
            else:
                right = pivot-1
        return -1


obj = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
assert (ret := obj.search(nums, target)) == 4, ret

print("Tests passed.")
