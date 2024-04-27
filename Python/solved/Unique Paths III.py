# Done (fast in performance and memory usage)
from typing import List


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        notvisited = set()
        for index_row, row in enumerate(grid):
            for index_item, item in enumerate(row):
                if item != -1:
                    notvisited.add((index_row, index_item))
                    if item == 1:
                        start = (index_row, index_item)
                    elif item == 2:
                        end = (index_row, index_item)
        ans = 0
        def dfs(no_visited, current):
            nonlocal end, ans
            no_visited.remove(current)
            if current == end:
                if not no_visited:
                    ans += 1
                return
            if (new_pos:=(current[0] - 1, current[1])) in no_visited:
                dfs(no_visited.copy(), new_pos)
            if (new_pos:=(current[0] + 1, current[1])) in no_visited:
                dfs(no_visited.copy(), new_pos)
            if (new_pos:=(current[0], current[1] - 1)) in no_visited:
                dfs(no_visited.copy(), new_pos)
            if (new_pos:=(current[0], current[1] + 1)) in no_visited:
                dfs(no_visited.copy(), new_pos)
        dfs(notvisited, start)
        return ans

obj = Solution()

grid = [[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 2, -1]]
assert (ret := obj.uniquePathsIII(grid)) == 2, ret
