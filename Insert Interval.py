# Done (slow)
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        isStarted = False
        isFound = False
        ans = []
        toinsert = []
        for interval in intervals:
            if not isStarted:
                if interval[1] >= newInterval[0]:
                    isStarted = True
                    if interval[0] <= newInterval[0]:
                        toinsert += [interval[0]]
                    else:
                        toinsert +=[newInterval[0]]
                elif interval[1] >= newInterval[1]:
                    isFound = True
                    isStarted = True
                    if interval[0] > newInterval[0]:
                        if newInterval[0]==newInterval[1]:
                            ans.append(newInterval)
                        else:
                            ans.append([newInterval[0]] + [interval[1]])
                            continue
                    else:
                        ans.append(newInterval)
                else:
                    ans.append(interval)
            if isFound:
                ans.append(interval)
                continue
            if isStarted:
                if interval[0] > newInterval[1]:
                    toinsert += [newInterval[1]]
                    ans.append(toinsert)
                    isFound = True
                    ans.append(interval)
                elif interval[1] >= newInterval[1]:
                    toinsert += [interval[1]]
                    ans.append(toinsert)
                    isFound = True
                    continue

        if not isFound:
            if isStarted:
                ans.append(toinsert + [newInterval[1]])

            else:
                ans.append(newInterval)
        return ans


obj = Solution()
intervals = [[1,3], [6, 9]]
newInterval = [3, 5]
intervals = [[1,5]]
newInterval = [0,6]
# intervals = [[1,5]]
# newInterval = [0,0]
# intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
# newIntervals = [4,8]
print(obj.insert(intervals, newInterval))
