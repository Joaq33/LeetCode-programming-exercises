from typing import List
from icecream import ic
from line_profiler import profile


# ic = lambda *x: x


class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        """
        it iterates over the grid once, storing the 2 minimal values' indexes
        of each row and editing the grid as it goes. Fastest
        """
        if (n := len(grid)) == 1:
            return grid[0][0]
        cur_row = grid[0]
        # cur_row = grid[0]
        for i in range(1, n):
            # ic(cur_row)
            indx1 = cur_row.index(min(cur_row))
            indx2 = cur_row.index(min(cur_row[:indx1] + cur_row[indx1 + 1:]))
            for j in range(n):
                if j != indx1:
                    grid[i][j] += cur_row[indx1]
                else:
                    grid[i][j] += cur_row[indx2]
            cur_row = grid[i]
            # ic(grid)
        return min(cur_row)

    # @profile
    # def minFallingPathSum(self, grid: List[List[int]]) -> int:
    #     """
    #     this is a test version of the function above, it is just worse
    #     :param grid:
    #     :return:
    #     """
    #     n = len(grid)
    #
    #     def min_indexes(row: List) -> (int, int):
    #
    #         # indx1 = row.index(min(row))
    #         # indx2 = row.index(min(row[:indx1] + row[indx1 + 1:]))
    #         m1 = m2 = 200
    #         indx1 = indx2 = n
    #         for i in range(n):
    #             val = row[i]
    #             if val < m1:
    #                 m2 = m1
    #                 m1 = val
    #                 indx2 = indx1
    #                 indx1 = i
    #                 continue
    #             if val < m2:
    #                 m2 = val
    #                 indx2 = i
    #
    #         return indx1, indx2
    #
    #     cur_row = grid[0]
    #     for i in range(1, n):
    #         # indx1 = cur_row.index(min(cur_row))
    #         # indx2 = cur_row.index(min(cur_row[:indx1] + cur_row[indx1 + 1:]))
    #         indx1, indx2 = min_indexes(cur_row)
    #         for j in range(n):
    #             if j != indx1:
    #                 grid[i][j] += cur_row[indx1]
    #             else:
    #                 grid[i][j] += cur_row[indx2]
    #         cur_row = grid[i]
    #     return min(cur_row)

    # def minFallingPathSum(self, grid: List[List[int]]) -> int:
    #     """
    #     keeps track of count for every row and calculates the sum for every position, taking valid min
    #     from previous row
    #     :param grid:
    #     :return:
    #     """
    #     if n := len(grid) == 1:
    #         return grid[0][0]
    #     totals = [0] * n
    #     # l = [False] * n
    #     for cur_row in grid:
    #         l = [False] * n
    #         # ic('--------------')
    #         for i in range(n):
    #             prev_vals = [totals[val] for val in range(n) if val != i]
    #             l[i] = cur_row[i] + min(prev_vals)
    #         # ic('final', l)
    #         # totals = l.copy()
    #         totals = l
    #     return min(totals)
    #
    # def minFallingPathSum(self, grid: List[List[int]]) -> int:
    #     """TLE
    #     dfs approach
    #     """
    #     n = len(grid)
    #
    #     def memoize(f):
    #         memo = {}
    #
    #         def helper(x, y, z):
    #             if (x, y, z) not in memo:
    #                 memo[(x, y, z)] = f(x, y, z)
    #             return memo[(x, y, z)]
    #
    #         return helper
    #
    #     @memoize
    #     def dp(total, cur_row, invalid_pos):
    #         # ic(total, cur_row, invalid_pos)
    #         posible_pos = (i for i in range(n) if i != invalid_pos)  # generator
    #         if cur_row + 1 == n:
    #             return total + min([grid[cur_row][i] for i in posible_pos])
    #         tmp = [99] * n
    #         for i in posible_pos:
    #             # ic(i)
    #             tmp[i] = dp(total + grid[cur_row][i], cur_row + 1, i)
    #         # ic(tmp)
    #         return min(tmp)
    #
    #     return dp(0, 0, n)
