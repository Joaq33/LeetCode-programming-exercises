# Done
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        dict_of_starts = {k[0]: v for v, k in enumerate(intervals)}
        ordered = sorted(dict_of_starts.keys())
        dict_ordered = {k: v for v, k in enumerate(ordered)}
        last=ordered[-1]
        ans=[]
        for interval in intervals:
            next_val=interval[1]
            while next_val not in dict_ordered:
                next_val+=1
                if next_val>last:
                    ans.append(-1)
                    break
            else:
                ans.append(dict_of_starts[next_val])
        return ans


obj = Solution()
intervals = [[1,2]]
intervals = [ [3,4], [2,3], [5,6], [1,2] ]
# intervals=[[1,2],[3,4],[2,3],[6,7],[5,6]]
# intervals=[["f"],["a"],["c"],["b"],["e"],["d"]]
print(obj.findRightInterval(intervals))
