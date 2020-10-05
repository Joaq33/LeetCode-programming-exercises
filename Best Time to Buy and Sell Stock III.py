# Works but inefficient
class Solution:
    def maxProfit(self, prices) -> int:

        def rec(new_prices, second):
            if len(new_prices) < 2:
                return 0
            posibles = [0]
            for index, price in enumerate(new_prices[1:]):
                if new_prices[0] >= price:
                    continue
                temp = price - new_prices[0]

                if second == False:
                    if index + 2 == len(new_prices):
                        posibles.append(temp)
                        continue
                    for i in range(index + 2, len(new_prices) - 1):
                        temp2 = rec(new_prices[i:], True)
                        posibles.append(temp + temp2)
                posibles.append(temp)
            return max(posibles)

        ans = [0]
        for item in range(len(prices) - 1):
            ans += [rec(prices[item:], False)]
        return max(ans)


coso = Solution()
prices = [3, 3, 5, 0, 0, 3, 1, 4]
# prices = [1, 2, 3, 4, 5]

# prices=[1,2,3,4,5]
print(coso.maxProfit(prices))
