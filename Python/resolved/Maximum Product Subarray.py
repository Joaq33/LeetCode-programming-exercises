# Done (too slow)
import math
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        quantityofneg = 0
        newlist = []
        for item in nums:
            if item == 1:
                ans = 1
            elif item == -1:
                quantityofneg += 1
            else:
                if quantityofneg == 1:
                    newlist.append(-1)
                    quantityofneg = 0
                elif quantityofneg > 1:
                    newlist.extend([-1, -1])
                    quantityofneg = 0
                newlist.append(item)
        if quantityofneg == 1:
            newlist.append(-1)
        elif quantityofneg > 1:
            newlist.extend([-1, -1])

        nums = newlist
        n = len(nums)
        for largo in range(1, n + 1):
            for pos in range(n - largo + 1):
                temp = math.prod(nums[pos:pos + largo])
                if ans < temp:
                    ans = temp
        return ans


obj = Solution()
nums = [2, -1, -1, 2, 0, -3, 3]
print(obj.maxProduct(nums))
