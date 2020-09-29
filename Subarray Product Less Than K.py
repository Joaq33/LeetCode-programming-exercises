# Done (copied)
from typing import List


class Solution:
    # @profile
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0 or k == 1:
            return 0
        ans, start, prod = 0, 0, 1
        for index, item in enumerate(nums):
            prod *= item
            while prod >= k:
                prod /= nums[start]
                start += 1
            ans += index - start + 1
        return ans

    def numSubarrayProductLessThanK2(self, nums: List[int], k: int) -> int:
        ans = 0
        lar_nums = len(nums)
        if k == 0 or k == 1:
            return 0

        def dfs(index, cur):
            nonlocal ans
            if index == lar_nums:
                return
            c = 0
            if nums[index] == 1:
                while index + c != lar_nums and nums[index + c] == 1:
                    c += 1
                ans += c
                dfs(index + c, cur)
                return

            # if nums[index] == 1:
            #     ans += 1
            #     dfs(index + 1, cur)
            #     return
            if cur * nums[index] < k:
                ans += 1
                dfs(index + 1, cur * nums[index])

        for i in range(lar_nums):
            dfs(i, 1)
        return ans

    def numSubarrayProductLessThanK3(self, nums: List[int], k: int) -> int:
        # for i in nums:
        #     if i != 1:
        #         break
        #         pass
        # else:
        #     print()
        if k == 0 or k == 1:
            return 0
        ans = 0
        lar = len(nums)
        for i in range(lar):
            tmp = i
            cur = 1
            while tmp < lar:
                cur *= nums[tmp]
                if cur < k:
                    tmp += 1
                else:
                    break
            ans += tmp - i
        return ans


obj = Solution()

nums = [10, 5, 2, 6]
k = 100
assert (ret := obj.numSubarrayProductLessThanK(nums, k)) == 8, ret

nums = [1, 2, 3]
k = 0
assert (ret := obj.numSubarrayProductLessThanK(nums, k)) == 0, ret

nums = [1, 1, 1]
k = 1
assert (ret := obj.numSubarrayProductLessThanK(nums, k)) == 0, ret

nums = [1, 1, 1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1]
k = 100
assert (ret := obj.numSubarrayProductLessThanK(nums, k)) == 153, ret

nums = [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3]
k = 19
assert (ret := obj.numSubarrayProductLessThanK(nums, k)) == 18, ret

print("Tests passed.")
