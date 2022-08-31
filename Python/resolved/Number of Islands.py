from typing import List
from icecream import ic


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid = grid
        n = len(grid)
        m = len(grid[0])

        def visit_cell(row_index, column_index):
            visited_matrix[row_index][column_index] = 1

            if grid[row_index][column_index] == "0":
                return
            if row_index > 0 and visited_matrix[row_index - 1][column_index] == 0:
                print("entra0")
                visit_cell(row_index - 1, column_index)
            if row_index < n - 1 and visited_matrix[row_index + 1][column_index] == 0:
                print("entra1")
                visit_cell(row_index + 1, column_index)
            if column_index > 0 and visited_matrix[row_index][column_index - 1] == 0:
                print("entra2")
                visit_cell(row_index, column_index - 1)
            if column_index < m - 1 and visited_matrix[row_index][column_index + 1] == 0:
                print("entra3")
                visit_cell(row_index, column_index + 1)

        visited_matrix = [[0] * m for _ in range(n)]
        number_of_islands = 0
        for row_index in range(n):
            for column_index in range(m):
                print("cur", row_index, column_index)
                print("visited", visited_matrix)
                print(visited_matrix[row_index][column_index] == 0)
                print(grid[0][0] == "1")
                if visited_matrix[row_index][column_index] == 0:
                    if grid[row_index][column_index] == "1":
                        print("not visited")
                        number_of_islands += 1
                        visit_cell(row_index, column_index)
                    else:
                        visited_matrix[row_index][column_index] = 1

        return number_of_islands


obj = Solution()

grid = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
assert 3 == (ret := obj.numIslands(grid)), ret

grid = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
assert 1 == (ret := obj.numIslands(grid)), ret

print("Tests passed.")
