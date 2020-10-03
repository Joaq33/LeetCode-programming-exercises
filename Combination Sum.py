from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        s_can = set(candidates)
        if target in s_can:
            ans = [[target]]
        else:
            ans = []
        l_can = [i for i in s_can if i < target]

        def dfs(cur, index):
            value = []
            for i in range(index, len(l_can)):
                tmp = l_can[i] + cur
                if tmp == target:
                    value.append([l_can[i]])
                elif tmp < target:
                    for i2 in dfs(tmp, i):
                        value.append([l_can[i]] + i2)
            return value

        for index, item in enumerate(l_can):
            # print(item)
            for i in dfs(item, index):
                ans.append([item] + i)
        return ans


obj = Solution()

candidates = [2, 3, 6, 7]
target = 7
assert (ret := obj.combinationSum(candidates, target)) == [[7], [2, 2, 3]], ret

candidates = [2,3,5]
target = 8
assert (ret := obj.combinationSum(candidates, target)) == [[2,2,2,2],[2,3,3],[3,5]], ret

print("Tests passed.")