#option 2 incomplete
class Solution:
    def maxProfit(self, prices) -> int:
        for division in range(1,len(prices)):
            print(division,prices[:division+1],prices[division+1:])
            print(max(prices[:division+1]))
        pass


coso = Solution()
prices = [3, 3, 5, 0, 0, 3, 1, 4]
prices=[1,2,3,4,5]

# prices=[1,2,3,4,5]
print(coso.maxProfit(prices))
