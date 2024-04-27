# Done
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        tracking = None
        completed = False
        while i < len(nums):
            cur = nums[i]
            if tracking == cur:
                if completed:
                    del nums[i]
                    continue
                else:
                    completed = True
                    i += 1
            else:
                tracking = cur
                completed = False
                i += 1
        return len(nums)


obj = Solution()

nums = [1, 1, 1, 2, 2, 3]
assert 5 == (ret := obj.removeDuplicates(nums)), ret
assert [1, 1, 2, 2, 3] == nums, nums

print("Tests passed.")
