# Done
from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        ans = []
        length = len(A)
        for item in range(length, 0, -1):
            current = A.index(length - item + 1) + 1
            ans.append(current)
            A = A[current - 1::-1] + A[current:]
            ans.append(item)
            A = A[item - 1::-1] + A[item:]
        ans.append(length)
        return ans



obj = Solution()
A = [1, 6, 3, 4, 9, 7, 8, 5, 2]
print(obj.pancakeSort(A))
