from typing import List


class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        first = A[0]
        lower, bigger = A[0] + K, A[-1] - K
        o = 1
        while o < len(A):
            i = A[o]
            o += 1
            if i < lower:
                print(i, i+K)
            else:
                if i-K < lower:
                    lower = i-K
                    continue
                # if i < lower+K:
                #     print(i, i-K)

                print(i, i-K)
                bigger = i-K
            # if o < len(A)-1:
            # else:
            #     break


obj = Solution()

A = [1, 3, 6]
K = 3
assert 3 == (ret := obj.smallestRangeII(A, K)), ret

A = [1]
K = 0
assert 0 == (ret := obj.smallestRangeII(A, K)), ret

print("Tests passed.")
