from typing import List
from icecream import ic


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        time limit exceeded
        dp approach
        time complexity: o(n^2)
        space complexity: o(n^2)
        :param prices:
        :return:
        """

        def dp(cur_prices, is_positioned, cur_money=None):
            if len(cur_prices) == 1:
                # ic(cur_prices, cur_prices[0] - cur_money)
                if not is_positioned:
                    return 0
                return cur_prices[0]

            if not is_positioned:
                return max(- cur_prices[0] + dp(cur_prices[1:], True, cur_money=cur_prices[0]),  # take value
                           dp(cur_prices[1:], False))  # not take it

            # if cur_money >= cur_prices[0]:

            tmp = dp(cur_prices[1:], True, cur_money)
            if cur_money >= cur_prices[0]:
                return tmp
            return max(cur_prices[0] + dp(cur_prices[1:], False),  # close position
                       tmp  # not close it
                       )

        return dp(prices, False, 0)

    def maxProfit(self, prices: List[int]) -> int:
        """
        time_complexity: o(n)
        space_complexity: o(1)
        using reference to make diffs while iterating one time
        :param prices:
        :return:
        """
        n = len(prices)
        buy_price = float('inf')
        profit = 0
        for i in range(n):
            if prices[i] <= buy_price:
                buy_price = prices[i]
            else:
                profit = profit + prices[i] - buy_price
                buy_price = prices[i]
        return profit
