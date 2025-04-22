from icecream import ic


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = 0
        for i in range(max(start.bit_length(), goal.bit_length())):
            ans += ((start ^ goal) >> i) & 1
        return ans
