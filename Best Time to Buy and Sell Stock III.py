class Solution:
    def maxProfit(self, prices) -> int:
        ans = []

        def rec(newprices, segundo):
            nonlocal ans
            posibles=[]
            if len(newprices) < 2:
                return 0
            for index, price in enumerate(newprices[1:]):
                print(newprices)
                temp = newprices[0] - price
                temp2 = rec(newprices[index + 1:], True)
                temp+=temp2
                posibles.append(temp)
            return max(posibles)

        rec(prices, False)
        print(prices, ans)


coso = Solution()
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(coso.maxProfit(prices))
