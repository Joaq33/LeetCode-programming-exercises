# Done
from typing import List
from collections import defaultdict

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        cambios = defaultdict(int)
        first = 100
        last = 0
        for trip in trips:
            if first > trip[1]:
                first = trip[1]
            if last < trip[2]:
                last = trip[2]
            cambios[trip[1]] += trip[0]
            cambios[trip[2]] -= trip[0]
        cur = 0
        for i in range(first, last+1):
            cur += cambios[i]
            if cur > capacity:
                return False
        return True

if __name__ == '__main__':
    obj = Solution()

    trips = [[2, 1, 5], [3, 3, 7]]
    capacity = 4
    assert (ret := obj.carPooling(trips, capacity)) == False, ret

    print("Tests passed")
