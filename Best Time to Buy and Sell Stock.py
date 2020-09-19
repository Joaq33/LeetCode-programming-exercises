# Done
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        minim = prices[0]
        ans = 0
        for i in range(1, len(prices)):
            if prices[i] < minim:
                minim = prices[i]
            dif = prices[i] - minim
            if dif > ans:
                ans = dif
        return ans


obj = Solution()
prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
# prices = [1,2]
print(obj.maxProfit(prices))
