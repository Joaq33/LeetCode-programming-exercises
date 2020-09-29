from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        print(len(queries))

        def dfs(cur, destiny):
            if destiny in divs[cur]:
                print("asd", divs[destiny])
                return [divs[cur][destiny]]
            else:
                print(divs[cur].keys())
                for key in divs[cur].keys():
                    tmp = dfs(key, destiny)
                    if tmp:
                        print(divs[cur][key])
                        return [divs[cur][key]] + tmp
                # return

        divs = defaultdict(dict)
        existing = set()
        for n in range(len(equations)):
            existing.add(equations[n][0])
            existing.add(equations[n][1])
            divs[equations[n][0]][equations[n][1]] = values[n]
        ans = []
        for origin, destiny in queries:
            if origin in existing and destiny in existing:
                if origin == destiny:
                    ans.append(1)
                    continue
                tmp = dfs(origin, destiny)
                if tmp:
                    tmp2 = 1
                    for i in tmp:
                        tmp2 *= i
                    ans.append(tmp2)
                else:
                    tmp = dfs(destiny, origin)
                    if tmp:
                        tmp2 = 1
                        for i in tmp:
                            tmp2 /= i
                        ans.append(tmp2)
                    else:
                        ans.append(-1)#aca agregar la excepcion
                # else:
                #
            else:
                ans.append(-1)
        return ans


obj = Solution()

equations = [["a", "b"], ["b", "c"]]
values = [2.0, 3.0]
queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
# assert (ret := obj.calcEquation(equations, values, queries)) == [6.00000, 0.50000, -1.00000, 1.00000, -1.00000], ret

equations = [["a", "e"], ["b", "e"]]
values = [4.0, 3.0]
queries = [["a", "b"], ["e", "e"], ["x", "x"]]
assert (ret := obj.calcEquation(equations, values, queries)) == [1.33333,1.00000,-1.00000], ret

print("Tests passed")
