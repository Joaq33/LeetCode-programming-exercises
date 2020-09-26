# Done (beat 100% of submissions times)
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries or duration == 0:
            return 0
        ans = 0
        last_tick = timeSeries[0]
        for attack in timeSeries[1:]:
            dif = attack - last_tick
            ans += duration if dif >= duration else dif
            last_tick = attack
        return ans + duration


obj = Solution()

timeSeries = [1, 4]
duration = 2
assert (ret := obj.findPoisonedDuration(timeSeries, duration)) == 4, ret

timeSeries = [1, 2]
duration = 2
assert (ret := obj.findPoisonedDuration(timeSeries, duration)) == 3, ret

timeSeries = []
duration = 2
assert (ret := obj.findPoisonedDuration(timeSeries, duration)) == 0, ret

print("Tests passed")
