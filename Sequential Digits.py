# Done
from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        stl = str(low)
        lar = len(stl)
        first = int(stl[0]) - 1
        alldigits = [str(i) for i in range(1, 10)]
        ans = []
        while True:
            cur = int("".join(alldigits[first:first + lar]))
            if cur > high:
                return ans
            if cur >= low:
                ans.append(cur)
            if cur % 10 < 9:
                first += 1
            elif lar == 9:
                return ans
            else:
                first = 0
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

low = 10
high = 1000000000
assert (ret := obj.sequentialDigits(low, high)) == [12, 23, 34, 45, 56, 67, 78, 89, 123, 234, 345, 456, 567, 678, 789,
                                                    1234, 2345, 3456, 4567, 5678, 6789, 12345, 23456, 34567, 45678,
                                                    56789, 123456, 234567, 345678, 456789, 1234567, 2345678, 3456789,
                                                    12345678, 23456789, 123456789], ret

print("Tests passed")
