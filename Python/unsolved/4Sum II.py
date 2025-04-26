# not Done
from typing import List
from collections import Counter


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:  # time exceeded
        options = []
        # try:
        #     visited_a = {A[0]}
        #     visited_b = {B[0]}
        # except:
        #     return 0
        if not A or not B or not C or not D:
            return 0
        ans = 0
        new_d = Counter(D)

        for a in A:
            # visited_a.add(a)
            for b in B:
                for c in C:
                    # print(d:=-(a + b + c))
                    if (d := -(a + b + c)) in new_d:
                        print(d)
                        ans += new_d[d]
                        options.append([a, b, c, -(a + b + c)])

        print(options)
        return ans
        # options = []
        # try:
        #     visited_a = {A[0]}
        #     visited_b = {B[0]}
        # except:
        #     return 0
        # if not C or not D:
        #     return 0
        #
        # visited_a = set()
        # visited_b = set()
        # visited_c = set()
        # reduced_b, reduced_c = [], []
        #
        # ans = 0
        # new_d = set(D)
        # new_d = Counter(D)
        #
        # for c in C:
        #     # if c in visited_c:
        #     #     continue
        #     visited_c.add(c)
        #     reduced_c.append(c)
        #     if -(A[0] + B[0] + c) in new_d:
        #         ans += new_d[-(A[0] + B[0] + c)]
        #         options.append([A[0],B[0],c,-(A[0] + B[0] + c)])
        #
        # for b in B[1:]:
        #     # if b in visited_b:
        #     #     continue
        #     visited_b.add(b)
        #     reduced_b.append(b)
        #     for c in reduced_c:
        #         if -(A[0] + b + c) in new_d:
        #             ans += new_d[-(A[0] + b + c)]
        #             options.append([A[0], b, c, -(A[0] + b + c)])
        # print(reduced_b, reduced_c)
        # for a in A[1:]:
        #     # if a in visited_a:
        #     #     continue
        #     visited_a.add(a)
        #     for b in B:
        #         for c in C:
        #             if -(a + b + c) in new_d:
        #                 ans += new_d[-(a + b + c)]
        #                 options.append([a, b, c, -(a + b + c)])
        #
        # print(options)
        # return ans


obj = Solution()

A = [1, 2]
B = [-2, -1]
C = [-1, 2]
D = [0, 2]
assert 2 == (ret := obj.fourSumCount(A, B, C, D)), ret

A = [-1, -1]
B = [-1, 1]
C = [-1, 1]
D = [1, -1]
assert 6 == (ret := obj.fourSumCount(A, B, C, D)), ret

print("Tests passed.")
