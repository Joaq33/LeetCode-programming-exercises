# Done
from typing import List


class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:  # copied
        def dist(p1, p2):
            return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

        lookup = set([dist(p1, p2), dist(p1, p3), \
                      dist(p1, p4), dist(p2, p3), \
                      dist(p2, p4), dist(p3, p4)])
        return 0 not in lookup and len(lookup) == 2


obj = Solution()
p1 = [1, 0]
p2 = [-1, 0]
p3 = [0, 1]
p4 = [0, -1]

assert True == (ret := obj.validSquare(p1, p2, p3, p4)), ret
p1 = [0, 0]
p2 = [1, 1]
p3 = [1, 0]
p4 = [0, 1]

assert True == (ret := obj.validSquare(p1, p2, p3, p4)), ret

print("Tests passed.")
