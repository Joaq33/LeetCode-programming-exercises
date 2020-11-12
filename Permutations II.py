# Done
from typing import List
from collections import Counter


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        ans = []

        def rec(cur, posibles):
            if not posibles:
                ans.append(cur)
            for i in posibles:
                tmp = posibles.copy()
                if posibles[i] == 1:
                    tmp.pop(i)
                else:
                    tmp[i] -= 1
                rec(cur + [i], tmp)

        rec([], count)
        return ans


obj = Solution()

nums = [1, 1, 2]
assert [[1, 1, 2],
        [1, 2, 1],
        [2, 1, 1]] == (ret := obj.permuteUnique(nums)), ret

print("Tests passed.")
