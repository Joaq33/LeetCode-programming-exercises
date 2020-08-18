# Done
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        counter = collections.Counter(s)
        for quantity in counter.values():
            ans += quantity // 2 * 2
        return ans + (ans < len(s))
