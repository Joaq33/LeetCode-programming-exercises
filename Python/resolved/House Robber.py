# Done (Slow)
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        num_l = len(nums)
        if len(nums) == 1:
            return nums[0]

        def memoize(f):
            memo = {}
            def helper(x):
                if x not in memo:
                    memo[x] = f(x)
                return memo[x]
            return helper

        @memoize
        def dfs(i_nums):
            lar = num_l - i_nums
            if lar == 1:
                return nums[i_nums]
            if lar == 0:
                print()
            temp = [0]
            for index in range(i_nums + 2, num_l):
                temp.append(dfs(index))
            return nums[i_nums] + max(temp)

        odd = dfs(0)
        even = dfs(1)
        return max(odd, even)


obj = Solution()
nums = [1, 2, 3, 1]
print(obj.rob(nums))
