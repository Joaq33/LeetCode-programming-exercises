# Done
from typing import List
from collections import defaultdict


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        visited = {0, -1}
        ways = defaultdict(list)
        last = None
        for i, n in enumerate(arr):
            if n == last:
                ways[n][-1] = i
                continue
            last = n
            ways[n].append(i)
        queue = [0]
        level = 0
        while queue:
            next_queue = []
            for node in queue:
                if node == len(arr) - 1:
                    return level
                for item in ways[arr[node]][::-1]:
                    if item not in visited:
                        visited.add(item)
                        next_queue.append(item)
                if node + 1 not in visited:
                    visited.add(node + 1)
                    next_queue.append(node + 1)
                if node - 1 not in visited:
                    visited.add(node - 1)
                    next_queue.append(node - 1)
            queue = next_queue
            level += 1


obj = Solution()

arr = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
assert 3 == (ret := obj.minJumps(arr)), ret

arr = [11, 22, 7, 7, 7, 7, 7, 7, 7, 22, 13]
assert 3 == (ret := obj.minJumps(arr)), ret

arr = [6, 1, 9]
assert 2 == (ret := obj.minJumps(arr)), ret

arr = [7, 6, 9, 6, 9, 6, 9, 7]
assert 1 == (ret := obj.minJumps(arr)), ret

arr = [7]
assert 0 == (ret := obj.minJumps(arr)), ret

print("Tests passed.")
