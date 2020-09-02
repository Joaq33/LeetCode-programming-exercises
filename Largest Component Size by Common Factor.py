from _collections import defaultdict
from typing import List


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        dict_facts = defaultdict(list)
        connections = defaultdict(set)

        for item in A:
            dict_facts[item] = [item2 for item2 in range(2, item + 1) if item % item2 == 0]

        for index, item in enumerate(A):
            for othernumber in A[index+1:]:
                # if othernumber==item:
                #     continue
                for fact in dict_facts[item]:
                    if fact in dict_facts[othernumber]:
                        connections[item].add(othernumber)
        print("-"*10,connections)

        used = set()

        # def rec_connections(cur):
        #     nonlocal used
        #     if cur in used:
        #         return 0
        #     used.add(cur)
        #     temp = [1]
        #     for item in connections[cur]:
        #         if item not in used:
        #             temp.append(rec_conections(item))
        #         # temp.append(rec_conections(item))
        #     print(temp, connections[cur])
        #     return sum(temp)

        def rec_connections(cur):
            nonlocal used
            if cur in used:
                return 0
            used.add(cur)
            temp=[1]
            for item in connections[cur]:
                if item not in used:
                    temp.append(rec_connections(item))
            return sum(temp)

        posible_lenghts = []
        for item in A:
            posible_lenghts.append(rec_connections(item))
        print(posible_lenghts)
        return max(posible_lenghts)


obj = Solution()
A = [4, 6, 15, 35, 8, 18, 42, 7, 4, 5, 6, 5, 14]
A = [2, 3, 6, 7, 4, 12, 21, 39]
print(obj.largestComponentSize(A))
