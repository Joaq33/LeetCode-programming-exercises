class Solution:
    def maxProfit(self, prices) -> int:
        ans = []

        def rec(newprices, segundo):
            nonlocal ans
            posibles=[0]
            if len(newprices) < 2:
                return 0
            for index, price in enumerate(newprices[1:]):
                if price<newprices[0]:
                    #saber si el precio es mayor q el q siga
                    temp = newprices[0] - price
                    temp2 = rec(newprices[index + 1:], True)
                    temp+=temp2
                    posibles.append(temp)
            maximo=max(posibles)
            if maximo<0:
                maximo=0
            return maximo

        temp=[]
        for item in range(len(prices)):
            temp+=[rec(prices[item:], False)]

        print("temp",temp)
        print(prices, ans)


coso = Solution()
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(coso.maxProfit(prices))
