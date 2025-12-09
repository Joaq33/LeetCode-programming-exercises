from math import sqrt
from icecream import ic


class Solution:
    def countTriples(self, n: int) -> int:
        """
        time O(n^2)
        space O(1)
        """
        ans = 0
        for a in range(1, n + 1):
            for b in range(a + 1, n + 1):
                c_squared = a * a + b * b
                c = int(sqrt(c_squared))
                if c * c == c_squared and c <= n:
                    ans += 2
        return ans
        # print(n)
        # cur = 1
        # track = set()
        # inorder = list()
        # while cur <= n:
        #     track.add(cur ** 2)
        #     inorder.append(cur ** 2)
        #     cur += 1
        # ic(track)
        # ic(inorder)
        # pointer_end = len(inorder) - 1
        # ans = 0
        # ic(inorder[pointer_end])
        # while pointer_end>=5:
        #     for pointer_start in range(pointer_end):
        #         ic(pointer_end+1,inorder[pointer_end])
        #         ic(pointer_start+1,inorder[pointer_start])
        #         if ic(inorder[pointer_end] - inorder[pointer_start]) in track:
        #             ic('añadiendo')
        #             ans += 1
        #     pointer_end-=1

