from typing import List
from icecream import ic
from collections import defaultdict
from itertools import combinations


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        track_hashmap = defaultdict(list)
        for i in range(len(nums)):
            ic(nums[i])
            track_hashmap[nums[i]].append(i)
        ic(track_hashmap)
        ans = 0
        for ke in track_hashmap.keys():
            for (i, j) in list(combinations(track_hashmap[ke], 2)):
                ic(i, j, i * j, k)
                ic((i * j) % k == 0)

                if (i * j) % k == 0:
                    ans += 1
        ic(5 % 2, 5 % 2 == 0)
        return ans
