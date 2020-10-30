# Done
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 0
        begin, end = 0, len(seats) - 1
        if seats[0] == 0:
            begin = 1
            while seats[begin] == 0:
                begin += 1
            ans = begin - 1
        if seats[end] == 0:
            end -= 1
            while seats[end] == 0:
                end -= 1
            ans = max(ans, len(seats) - 1 - end - 1)
        if end - begin > 1 or ans < (end - begin - 3) // 2:
            tmp = 0
            for n in range(begin, end +1):
                if seats[n] == 0:
                    tmp += 1
                elif tmp > 0:
                    ans = max(ans, (tmp - 1) // 2)
                    tmp = 0

        return ans + 1


obj = Solution()

seats = [1, 1, 0, 0, 0, 1, 0]
assert (ret := obj.maxDistToClosest(seats)) == 2, ret

seats = [0, 1]
assert (ret := obj.maxDistToClosest(seats)) == 1, ret

seats = [1, 0, 0, 0, 1, 0, 1]
assert (ret := obj.maxDistToClosest(seats)) == 2, ret

seats = [1, 0, 0, 0]
assert (ret := obj.maxDistToClosest(seats)) == 3, ret

seats = [1, 0, 0, 0, 1, 0, 1]
assert (ret := obj.maxDistToClosest(seats)) == 2, ret

print("Tests passed.")
