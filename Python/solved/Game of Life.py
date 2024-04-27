# Done
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        lenx = len(board[0])
        leny = len(board)

        def check_neighbours(xcheck, ycheck):
            if not (-1 < xcheck < lenx) or not (-1 < ycheck < leny):
                return 0
            return board[ycheck][xcheck]

        def count_neighbours(x, y):
            ret = check_neighbours(x - 1, y - 1)
            ret += check_neighbours(x, y - 1)
            ret += check_neighbours(x + 1, y - 1)

            ret += check_neighbours(x - 1, y)
            ret += check_neighbours(x + 1, y)

            ret += check_neighbours(x - 1, y + 1)
            ret += check_neighbours(x, y + 1)
            ret += check_neighbours(x + 1, y + 1)

            return ret
        ans2 = []
        for ypos in range(leny):
            ans2.append([])
            for xpos in range(lenx):
                cur_neig = count_neighbours(xpos, ypos)
                if board[ypos][xpos] == 0:
                    if cur_neig == 3:
                        ans2[ypos].append(1)
                    else:
                        ans2[ypos].append(0)
                    continue
                if 1 < cur_neig < 4:
                    ans2[ypos].append(1)
                else:
                    ans2[ypos].append(0)
        for y in range(leny):
            for x in range(lenx):
                board[y][x] = ans2[y][x]
        return board


obj = Solution()

board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
obj.gameOfLife(board)
assert [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]] == board, board

board = [[1, 1], [1, 0]]
obj.gameOfLife(board)
assert [[1, 1], [1, 1]] == board, board

print("Tests passed.")
