from typing import List
from icecream import ic


class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
        Dynamic programming answer
        """
        # set for o(1) access time
        ss = set(dictionary)

        # initialize dp base array
        f = [0] * (len(s) + 1)

        for i in range(1, len(s) + 1):
            # fill dp array
            f[i] = f[i - 1] + 1
            ic(f)
            for j in range(i):
                if s[j:i] in ss and f[j] < f[i]:
                    # backtrack return value to minimal in position
                    f[i] = f[j]

        # return last state
        return f[i]
