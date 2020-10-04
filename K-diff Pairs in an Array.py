# Done
from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c_nums = Counter(nums)
        if k == 0:
            return sum(1 for number in c_nums if c_nums[number] > 1)
        ans = 0
        for item in c_nums:
            if item + k in c_nums:
                ans += 1
        return ans


obj = Solution()

nums = [3, 1, 4, 1, 5]
k = 2
assert (ret := obj.findPairs(nums, k)) == 2, ret

nums = [1, 2, 3, 4, 5]
k = 1
assert (ret := obj.findPairs(nums, k)) == 4, ret

print("Tests passed.")
