from typing import List
from icecream import ic
from collections import Counter


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        time limit exceeded
        o(n**2)
        :param dominoes:
        :return:
        """
        # ic([1,10],sorted([10,1]))
        dominoes = [sorted(x) for x in dominoes]
        # ic(dominoes, dominoes)
        ans = 0
        for i in range(len(dominoes)):
            for j in dominoes[i + 1:]:
                # ic(i,dominoes[i],j)
                if dominoes[i] == j:
                    ans += 1
        # return ans

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        """
        solved as a series approach
        o(n)
        can be improved constructing the output during counter creation(comparing current item to set),
         one less iteration
        :param dominoes:
        :return:
        """
        s_dom = Counter([tuple(sorted(x)) for x in dominoes])
        ans = 0
        for x in s_dom.items():
            # formula of series
            # 1 - 0
            # 2 - 1
            # 3 - 3
            # 4 - 6
            ans += (x[1] ** 2 - x[1]) // 2
        return ans
