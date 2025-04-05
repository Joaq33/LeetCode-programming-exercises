from typing import List
from icecream import ic
from functools import cmp_to_key
import numpy


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        b = sorted(set(arr))
        ic(b)
        c = {ele: rank + 1 for rank, ele in enumerate(b)}
        ic(c)
        ranked_arr = [c[ele] for ele in arr]
        return ranked_arr

    # def arrayRankTransform(self, arr: List[int]) -> List[int]:
    # ic(arr)
    # l = list(enumerate(arr))
    # sor = sorted(l, key=lambda x: x[1])
    # ic(l, sor)
    #
    # ans = [None] * len(arr)
    # tmp = 0
    # lastitem = None
    # for original_pos, val in sor:
    #     if lastitem != val:
    #         tmp += 1
    #     ans[original_pos] = tmp
    #     print(original_pos, val)
    #     lastitem = val
    # ic(ans)
    # return ans
