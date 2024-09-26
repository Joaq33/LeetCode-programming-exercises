from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """Dynamic programming approach"""
        f = [[1] for _ in range(numRows)]
        for i in range(1, numRows):
            for j in range(i // 2):
                f[i].append(f[i - 1][j] + f[i - 1][j + 1])
            f[i] += f[i][-2 + i % 2::-1]
        return f
