from typing import List
from collections import Counter


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:  # copied

        arr = list(zip(A, B))
        d = Counter(A) + Counter(B)
        key, value = d.most_common()[0]
        if value < len(A):
            return -1  # False

        max_flips = len(arr)
        flips = 0
        for i, j in arr:
            if i == key and j == key:
                max_flips -= 1
            elif i == key:
                pass
            elif j == key:
                flips += 1
            else:
                return -1  # False

        return min(flips, max_flips - flips)

    def minDominoRotations2(self, A: List[int], B: List[int]) -> int:
        totrack = None
        defined = False
        orientation = 3  # 1: up, 2: down, 3: not defined yet
        switches = 0

        begin = 1  # esto cambiarlo por el primer item +1 q cuya parte superior e inferior no sean iguales
        for item in range(begin, len(A)):
            if not defined:
                if A[item] != B[0]:  # check oriented
                    pass
                    # if B[item] != A[0]:
                # # if A[item] != A[0] and :
                # if B[item] != A[0]:
                #     if B[item] != B[0]:
                #         return -1
                #     else:
                #         defined = True
                #         up = False
                # else:
                #     switches += 1
                else:# A[item] == B[0]
                    if A[item] != B[item]:
                        switches += 1
                        if B[item] != A[0]:
                            defined = True
                            up = 2
                            totrack = B[0]
                    else:
                        defined = True
                        totrack = A[item]
        return switches


obj = Solution()

A = [2, 1, 2, 4, 2, 2]
B = [5, 2, 6, 2, 3, 2]
assert (ret := obj.minDominoRotations(A, B)) == 2, ret

print("Tests passed.")