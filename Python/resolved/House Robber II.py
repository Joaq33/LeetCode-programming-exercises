# Done
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return sum(nums)
        arr = [0] * (n+1)
        for i in range(2, n+1):
            arr[i] = max(arr[i-1], arr[i-2] + nums[i-2])
        preans = arr[i]

        arr = [0] * (n+1)
        for i in range(2, n+1):
            arr[i] = max(arr[i-1], arr[i-2] + nums[i-1])
        return max(preans, arr[i])

        # # include first but exclude last
        # F = [0 for _ in xrange(n-1+2)]
        # for i in xrange(2, n+1):
        #     F[i] = max(F[i-1], F[i-2]+nums[i-2])
        # ret = F[-1]
        #
        # # exclude first but include last
        # F = [0 for _ in xrange(n-1+2)]
        # for i in xrange(2, n+1):
        #     F[i] = max(F[i-1], F[i-2]+nums[i-1])
        #
        # ret = max(ret, F[-1])
        # return ret



obj = Solution()

nums = [2, 3, 2]
assert (ret := obj.rob(nums)) == 3, ret

print("Tests passed.")
