import logging
from icecream import ic


class Solution:

    def decodeAtIndex(self, s: str, k: int) -> str:  # memory limit exceeded
        cur = cur_count = 0
        cur_s = ""

        while cur_count < k:
            if s[cur].isalpha():
                cur_s += s[cur]
                cur_count += 1
            else:
                cur_s *= int(s[cur])
                cur_count *= int(s[cur])
            cur += 1
        return cur_s[k - 1]

    def decodeAtIndex(self, s: str, k: int) -> str:
        total = 0
        for ch in s:
            if ch.isdigit():
                total *= int(ch)
            else:
                total += 1
        for ch in reversed(s):
            if ch.isdigit():
                total //= int(ch)
                k %= total
            else:
                if k == 0 or total == k:
                    return ch
                total -= 1
        # return ""
