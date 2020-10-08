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


obj = Solution()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
assert (ret := obj.search(nums, target)) == 4, ret

print("Tests passed.")
