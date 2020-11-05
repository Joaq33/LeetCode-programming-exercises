# Done
from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        ways = defaultdict(dict)
        conections = defaultdict(list)
        for a, b in edges:
            conections[a].append(b)
            conections[b].append(a)
        ans = []
        def dfs(cur, last = -1):
            ret = 0
            for con in conections[cur]:
                if con != last:
                    if con in ways[cur]:
                        ret = max(ret, ways[cur][con])
                    else:
                        tmp2 = dfs(con, cur)
                        ways[cur][con] = tmp2
                        ret = max(ret, tmp2)
            return ret + 1
        cur_min = float("inf")
        for i in conections:
            tmp = dfs(i)
            if tmp < cur_min:
                cur_min = tmp
                ans = [i]
            elif tmp == cur_min:
                ans.append(i)
        return ans


obj = Solution()

n = 6
edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
assert [3, 4] == (ret := obj.findMinHeightTrees(n, edges)), ret

n = 2
edges = [[0, 1]]
assert [0, 1] == (ret := obj.findMinHeightTrees(n, edges)), ret

n = 1
edges = []
assert [0] == (ret := obj.findMinHeightTrees(n, edges)), ret

n = 4
edges = [[1, 0], [1, 2], [1, 3]]
assert [1] == (ret := obj.findMinHeightTrees(n, edges)), ret

print("Tests passed.")
