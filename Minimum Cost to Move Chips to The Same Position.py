# Done
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = even = 0
        for i in position:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
        return odd if odd < even else even


obj = Solution()

position = [1, 2, 3]
assert 1 == (ret := obj.minCostToMoveChips(position)), ret

position = [2, 2, 2, 3, 3]
assert 2 == (ret := obj.minCostToMoveChips(position)), ret

print("Tests passed.")
