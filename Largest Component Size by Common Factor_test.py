# from _collections import defaultdict
from typing import List


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        dict_facts = {}

        print(9%6)
        for item in A:
            dict_facts[item] = [item2 for item2 in range(2, item + 1) if item % item2 == 0]


        # def rec_connections(cur):
        #     nonlocal used
        #     used.add(cur)
        #     temp=1
        #
        #     return temp
        # for item in A:
        #     if item not in used:
        #         posibles_lenghts.append(rec_connections(item))
        # return max(posibles_lenghts)
        # for index,item in enumerate(A):
        #     if item in used:
        #         continue
        #     used.add(item)
        #     temp=0
        #     for item2 in A[index+1:]:
        #         if item2 in used:
        #             continue
        #         if any(fact in dict_facts[item2] for fact in dict_facts[item]):
        #             temp+=1
        #         print(any(fact in dict_facts[item2] for fact in dict_facts[item]))
        #     posibles_lenghts.append(temp)



obj = Solution()
A = [4, 6, 15, 35, 8, 18, 42, 7, 4, 5, 6, 5, 14]
A = [2, 3, 6, 7, 4, 12, 21, 39,11]
print(obj.largestComponentSize(A))
