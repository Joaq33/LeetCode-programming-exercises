# Done
from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = []
        for item in range(len(A), 0, -1):
            current = A.index(len(A) - item + 1) + 1
            ans.append(current)
            A = A[current - 1::-1] + A[current:]
            ans.append(item)
            A = A[item - 1::-1] + A[item:]
        ans.append(len(A))
        return ans



obj = Solution()
A = [1, 6, 3, 4, 9, 7, 8, 5, 2]
print(obj.pancakeSort(A))
