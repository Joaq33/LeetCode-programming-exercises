from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        def get_number():
            for i in range(1,len(matrix[0])):
                yield i
            for i in range(len(matrix), 0, -1):
                yield i
        ans = []
        x = 1
        curx = cury = 0
        for i in get_number():
            for subi in range(i):
                print(subi, curx-x*subi)
                curx, cury = cury, curx
                cury += 1
                curx -= 1
                ans.append(matrix[cury-x*subi][curx+x*subi])
                # cury += x
                # curx -= x
            curx = 0
            cury -= x
        print(ans)

obj = Solution()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
assert [1, 2, 4, 7, 5, 3, 6, 8, 9] == (ret := obj.findDiagonalOrder(matrix)), ret

print("Tests passed.")
