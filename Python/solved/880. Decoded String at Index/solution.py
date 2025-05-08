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
        i = 0
        for c in s:
            if c.isdigit():
                i *= int(c)
            else:
                i += 1
        ic(i, k)
        for c in s[::-1]:
            ic('a', k, i)
            k %= i
            ic(' ', k, i)
            if k == 0 and c.isalpha():
                return c

            if c.isdigit():
                i /= int(c)
            else:
                i -= 1

        return Exception
