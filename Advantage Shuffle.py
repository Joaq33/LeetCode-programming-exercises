# Done (copied)
from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:  # copied (fastest, 2 pointers)
        idx = list(range(len(B)))
        idx.sort(key=lambda i: B[i])
        A.sort()
        res = [-1] * len(A)
        start, end = 0, len(B) - 1
        # iterate through sorted A and B
        # if a can cover b, then correspond b with a
        # if a cannot, correspond a with largest of b
        for a in A:
            if a > B[idx[start]]:
                res[idx[start]] = a
                start += 1
            else:
                res[idx[end]] = a
                end -= 1
        return res
    def advantageCount3(self, A: List[int], B: List[int]) -> List[int]:  # copied

        ans = [False] * len(A)
        A.sort()
        B = [[val, ind] for ind, val in enumerate(B)]
        B.sort()
        temp = []
        ind = 0

        for i in A:
            if i > B[ind][0]:
                ans[B[ind][1]] = i
                ind += 1
            else:
                temp.append(i)

        return [element if element != False else temp.pop() for element in ans]

    def advantageCount2(self, A: List[int], B: List[int]) -> List[int]:  # failed at last because there are duplicates

        A.sort()
        sort_B = sorted(B)
        references = dict()
        cur = 0
        ans = [None] * len(A)
        tmp = []
        for item in A:
            if item > sort_B[cur]:
                references[sort_B[cur]] = item
                cur += 1
            else:
                tmp.append(item)
        for index, item in enumerate(B):
            if item in references:
                ans[index] = references[item]
            else:
                ans[index] = tmp.pop()
        return ans


obj = Solution()

A = [2, 0, 4, 1, 2]
B = [1, 3, 0, 0, 2]
assert [2, 0, 2, 1, 4] == (ret := obj.advantageCount(A, B))

A = [12, 24, 8, 32]
B = [13, 25, 32, 11]
assert [24, 32, 8, 12] == (ret := obj.advantageCount(A, B))

A = [2, 7, 11, 15]
B = [1, 10, 4, 11]
assert [2, 11, 7, 15] == (ret := obj.advantageCount(A, B))

A = [2, 7, 11, 15]
B = [1, 10, 4, 11]
assert [2, 11, 7, 15] == (ret := obj.advantageCount(A, B))
