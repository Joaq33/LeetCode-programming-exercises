# Done
from collections import deque


class Solution:
    def sortArrayByParity(self, A):
        ans = deque()
        for item in A:
            if item % 2:
                ans.append(item)
            else:
                ans.appendleft(item)
        return list(ans)


coso = Solution()
A = [3, 1, 2, 4]
print(coso.sortArrayByParity(A))
