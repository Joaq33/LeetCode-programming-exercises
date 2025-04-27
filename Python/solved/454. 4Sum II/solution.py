# not Done
from typing import List
from collections import Counter, defaultdict
import itertools
from icecream import ic


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int],
                     nums4: List[int]) -> int:  # time exceeded
        options = []
        # try:
        #     visited_a = {A[0]}
        #     visited_b = {B[0]}
        # except:
        #     return 0
        if not A or not B or not C or not D:
            return 0
        ans = 0
        new_d = Counter(D)

        for a in A:
            # visited_a.add(a)
            for b in B:
                for c in C:
                    # print(d:=-(a + b + c))
                    if (d := -(a + b + c)) in new_d:
                        print(d)
                        ans += new_d[d]
                        options.append([a, b, c, -(a + b + c)])

        print(options)
        return ans
        # options = []
        # try:
        #     visited_a = {A[0]}
        #     visited_b = {B[0]}
        # except:
        #     return 0
        # if not C or not D:
        #     return 0
        #
        # visited_a = set()
        # visited_b = set()
        # visited_c = set()
        # reduced_b, reduced_c = [], []
        #
        # ans = 0
        # new_d = set(D)
        # new_d = Counter(D)
        #
        # for c in C:
        #     # if c in visited_c:
        #     #     continue
        #     visited_c.add(c)
        #     reduced_c.append(c)
        #     if -(A[0] + B[0] + c) in new_d:
        #         ans += new_d[-(A[0] + B[0] + c)]
        #         options.append([A[0],B[0],c,-(A[0] + B[0] + c)])
        #
        # for b in B[1:]:
        #     # if b in visited_b:
        #     #     continue
        #     visited_b.add(b)
        #     reduced_b.append(b)
        #     for c in reduced_c:
        #         if -(A[0] + b + c) in new_d:
        #             ans += new_d[-(A[0] + b + c)]
        #             options.append([A[0], b, c, -(A[0] + b + c)])
        # print(reduced_b, reduced_c)
        # for a in A[1:]:
        #     # if a in visited_a:
        #     #     continue
        #     visited_a.add(a)
        #     for b in B:
        #         for c in C:
        #             if -(a + b + c) in new_d:
        #                 ans += new_d[-(a + b + c)]
        #                 options.append([a, b, c, -(a + b + c)])
        #
        # print(options)
        # return ans

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """prefix sums algohorithm"""
        ans = 0
        d_counter = Counter(sum(x) for x in itertools.product(nums3, nums4))
        # ic(d_counter)
        for product_item in itertools.product(nums1, nums2):
            cur_sum = sum(product_item)
            ans += d_counter[-cur_sum]
        return ans

    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        """prefix sums (simplified) algohorithm"""
        ans = 0
        dict_first_two = defaultdict(int)
        for num3, num4 in itertools.product(nums3, nums4):
            dict_first_two[num4 + num3] += 1

        for num1, num2 in itertools.product(nums1, nums2):
            ans += dict_first_two[-(num1 + num2)]
        return ans
