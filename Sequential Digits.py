# Done
from typing import List
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        stl = str(low)
        lar = len(stl)
        first = int(stl[0])
        if first > 10-lar:
            lar += 1
            first = 1

        ans = []
        while True:
            cur = ""
            for pos in range(lar):
                cur += str(first + pos)
            cur = int(cur)
            if cur > high:
                return ans
            if cur >= low:
                ans.append(cur)
            if first + pos < 9:
                first += 1
            else:
                first = 1
                lar += 1

        return []


obj = Solution()

low = 8511
high = 23553
assert (ret := obj.sequentialDigits(low, high)) == [12345, 23456], ret

low = 234
high = 2314
assert (ret := obj.sequentialDigits(low, high)) == [234, 345, 456, 567, 678, 789, 1234], ret

low = 100
high = 300
assert (ret := obj.sequentialDigits(low, high)) == [123, 234], ret

print("Tests passed")
