# Done
from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak = False
        cur = arr[1]
        if cur <= arr[0]:
            return False
        for i in arr[2:-1]:
            print(cur, i)
            if cur == i:
                return False
            if not peak:
                if cur > i:
                    peak = True
                cur = i
            else:
                if cur < i:
                    return False
                cur = i
        return cur > arr[-1]


obj = Solution()

arr = [0, 1, 2, 4, 2, 1]
assert True == (ret := obj.validMountainArray(arr)), ret

arr = [0, 3, 2, 1]
assert True == (ret := obj.validMountainArray(arr)), ret

print("Tests passed.")
