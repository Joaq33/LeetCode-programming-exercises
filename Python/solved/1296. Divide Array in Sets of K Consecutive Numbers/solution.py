from collections import Counter
from typing import List
from icecream import ic


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool: #time exceeded
        if k == 1: return True
        if not len(nums) % k == 0: return False
        nums_sorted = sorted(nums)
        # ic(nums_sorted)

        max_paths = len(nums) // k
        all_paths = [[None, None] for _ in range(max_paths)]
        # ic(all_paths)
        first_available = cur_path = cur_item_index = 0

        while cur_path < max_paths:
            # ic("entering again")
            # cur_path = first_available
            if all_paths[cur_path][0] == None:
                # path not initialized
                all_paths[cur_path][0] = nums_sorted[cur_item_index]
                all_paths[cur_path][1] = 1
                cur_path = first_available
                # print('pasa')
                # ic('path not initialized', nums_sorted[cur_item_index], cur_item_index, all_paths, first_available,
                #    cur_path)
                # break # todo borrar
                # continue

            elif all_paths[cur_path][0] == nums_sorted[cur_item_index] - 1:
                # append to path
                all_paths[cur_path][1] += 1
                if all_paths[cur_path][1] == k:
                    # closing a path
                    first_available += 1
                    cur_path += 1
                    # ic('closing a path', nums_sorted[cur_item_index], cur_item_index, all_paths, first_available,
                    #    cur_path)
                    cur_item_index += 1
                    continue  # todo borrar
                    # continue

                all_paths[cur_path][0] = nums_sorted[cur_item_index]
                cur_path = first_available

                # ic('append to path', nums_sorted[cur_item_index], cur_item_index, all_paths, first_available, cur_path)
                # cur_path += 1
            elif all_paths[cur_path][0] == nums_sorted[cur_item_index]:
                # path already exists
                cur_path += 1
                # ic('path already exists', nums_sorted[cur_item_index], cur_item_index, all_paths, first_available,
                #    cur_path)
                # breakpoint()
                continue
            else:
                # ic('not append to path', nums_sorted[cur_item_index], cur_item_index, all_paths, first_available,
                #    cur_path)
                return False
            cur_item_index += 1
        else:
            # ic('else of while', nums_sorted[cur_item_index], cur_item_index, all_paths, first_available, cur_path)
            # ic(cur_item_index, len(nums)-1)
            if cur_item_index == len(nums):
                return True
            return False

            # if cur_item_index == 2: break
        # ic(all_paths)
        # return False
        # open_paths = [(nums_sorted[0], 1)]
        # for i in nums_sorted[1:]:
        #     if
        # return
        # return True
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        cnt = Counter(nums)
        for x in sorted(nums):
            if cnt[x]:
                for y in range(x, x + k):
                    if cnt[y] == 0:
                        return False
                    cnt[y] -= 1
        return True