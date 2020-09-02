# Done
from typing import List


class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        A = sorted(A, reverse=True)

        def f_search(notused, filter, last):
            if not len(filter):
                return str(A[next(iter(notused))])
            for item in notused:
                print(A[item])
                if A[item] < filter[0] or last:
                    rec = f_search(notused - {item}, filter[1:], A[item] != 2 and len(filter) == 3)
                    if rec:
                        if len(rec) == 1:
                            return ":" + str(A[item]) + rec
                        return str(A[item]) + rec

        ans = f_search({0, 1, 2, 3}, [3, 4, 6], False)
        return ans if ans else ""


obj = Solution()
A = [1, 2, 0, 6]
A = [2, 0, 1, 0]
# A = [2, 0, 6, 6]
# A = [5, 5, 5, 5]
print(obj.largestTimeFromDigits(A))
