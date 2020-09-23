# Done
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        changes = dict()
        sum_cost = 0
        sum_gas = 0
        probs = []
        last_passed = False

        for n in range(len(cost)):
            cur = gas[n] - cost[n]
            if cur >= 0:
                if not last_passed:
                    probs.append(n)
                    last_passed = True
            else:
                last_passed = False
            sum_cost += cost[n]
            sum_gas += gas[n]
            changes[n] = cur
        if sum_cost > sum_gas:
            return -1
        for car in probs[:-1]:
            tank = 0
            for item in range(car, len(gas)):
                tank += changes[item]
                if tank < 0:
                    break
            else:
                for item in range(0, car):
                    tank += changes[item]
                    if tank < 0:
                        break
                else:
                    return car
        return probs[-1]


obj = Solution()

gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]
assert (ret := obj.canCompleteCircuit(gas, cost)) == 3, ret

gas = [5, 1, 2, 3, 4]
cost = [4, 4, 1, 5, 1]
assert (ret := obj.canCompleteCircuit(gas, cost)) == 4, ret

print("Tests passed")
