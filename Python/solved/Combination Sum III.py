# Done
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def rec_comb(remains: int, path, index: int):
            nonlocal ans
            if len(path) == k and remains == 0:
                ans.append(path)
                print()
                return
            if remains < 0:
                return

            if remains == 0 and len(path) < k:
                return
            for i in range(index, 10):
                rec_comb(remains - i, path + [i], i + 1)

        ans = []
        rec_comb(n, [], 1)
        return ans


obj = Solution()
k = 3
n = 9

print(obj.combinationSum3(k, n))
