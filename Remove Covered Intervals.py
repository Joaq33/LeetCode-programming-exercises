# Done
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        print(sorted(intervals, key=lambda x: x[0]*10**6-x[1]))
        s_inter = sorted(intervals, key=lambda x: (x[0], -x[1]), reverse=True)
        ans = len(intervals)
        for item in range(ans - 1):
            for item2 in range(item + 1, len(intervals)):
                if s_inter[item2][0] <= s_inter[item][0]:
                    if s_inter[item2][1] >= s_inter[item][1]:
                        ans -= 1
                        break
                else:
                    break
        return ans


obj = Solution()

intervals = [[34335, 39239], [15875, 91969], [29673, 66453], [53548, 69161], [40618, 93111]]
assert (ret := obj.removeCoveredIntervals(intervals)) == 2, ret

intervals = [[1, 2], [1, 4], [3, 4]]
assert (ret := obj.removeCoveredIntervals(intervals)) == 1, ret

intervals = [[1, 4], [3, 6], [2, 8]]
assert (ret := obj.removeCoveredIntervals(intervals)) == 2, ret

intervals = [[1, 4], [2, 3]]
assert (ret := obj.removeCoveredIntervals(intervals)) == 1, ret

intervals = [[0, 10], [5, 12]]
assert (ret := obj.removeCoveredIntervals(intervals)) == 2, ret

intervals = [[3, 10], [4, 10], [5, 11]]
assert (ret := obj.removeCoveredIntervals(intervals)) == 2, ret

print("Tests passed.")
