# Done
from typing import List

from numpy import array, ceil, sum


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:  # copied
        nums = array(nums)
        left, right = 1, max(nums)
        while left + 1 < right:
            mid = (left + right) // 2
            sum_ = sum(ceil(nums / mid))
            if sum_ > threshold:
                left = mid
            else:
                right = mid
        sum_ = sum(ceil(nums / left))

        return left if sum_ <= threshold else right


obj = Solution()

nums = [1, 2, 5, 9]
threshold = 6
assert 5 == (ret := obj.smallestDivisor(nums, threshold)), ret

print("Tests passed.")
