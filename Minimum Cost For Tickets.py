# Done
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        def memoize(f):
            memo = {}

            def helper(x):
                if x not in memo:
                    memo[x] = f(x)
                return memo[x]

            return helper

        first, last = days[0], days[-1]
        days = set(days)

        @memoize
        def rec(from_day: int):
            if from_day > last:
                return 0
            if from_day not in days:
                return min(rec(from_day + 1),
                           rec(from_day + 1) + costs[0],
                           rec(from_day + 7) + costs[1],
                           rec(from_day + 30) + costs[2])
            else:
                return min(rec(from_day + 1) + costs[0],
                           rec(from_day + 7) + costs[1],
                           rec(from_day + 30) + costs[2])

        return rec(first)


obj = Solution()
days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
print(obj.mincostTickets(days, costs))
