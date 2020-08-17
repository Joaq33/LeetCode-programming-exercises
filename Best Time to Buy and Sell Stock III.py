class Solution:
    def maxProfit(self, prices) -> int:
        # ans = []

        def rec(newprices, segundo):
            if len(newprices) < 2:
                return 0
            posibles=[0]
            for index, price in enumerate(newprices[1:]):
                if price<newprices[0]:
                    temp = newprices[0] - price
                    if segundo==False:
                        temp2 = rec(newprices[index + 1:], True)
                        temp+=temp2
                    posibles.append(temp)
            maximo=max(posibles)
            return maximo

        temp=[0]
        for item in range(len(prices)):
            temp+=[rec(prices[item:], False)]

        print("temp",temp,max(temp))
        print(prices)


coso = Solution()
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(coso.maxProfit(prices))
