# Done
from math import log, ceil


class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        return ceil(log(buckets, ceil(minutesToTest/minutesToDie)+1))


obj = Solution()

buckets = 1000
minutesToDie = 15
minutesToTest = 60
assert 5 == (ret := obj.poorPigs(buckets, minutesToDie, minutesToTest)), ret

buckets = 4
minutesToDie = 15
minutesToTest = 15
assert 2 == (ret := obj.poorPigs(buckets, minutesToDie, minutesToTest)), ret

print("Tests passed.")
