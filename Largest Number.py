# Done copiado
from functools import cmp_to_key
from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(x, y):
            u = x + y
            v = y + x
            if u == v:
                return 0
            elif u < v:
                return -1
            else:
                return 1

        v = map(str, nums)
        result = ''.join(reversed(sorted(v, key=cmp_to_key(cmp))))
        if result and result[0] == '0':
            return '0'
        else:
            return result


obj = Solution()

nums = [10, 2, 11]
assert (ret := obj.largestNumber(nums)) == "21110", ret

print("Tests passed")
