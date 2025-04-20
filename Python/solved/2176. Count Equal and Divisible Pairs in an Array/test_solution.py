import unittest
from pickle import FALSE

from solution import Solution
from icecream import ic
from parameterized import parameterized

ic.use_stdout()


# null = None
# true = True
# false = False


class Test(unittest.TestCase):
    @parameterized.expand([
        [[3, 1, 2, 2, 2, 1, 3],
         2,
         4],
        [[1, 2, 3, 4],
         1,
         0]
    ])
    def test_(self, nums, k, expected):
        print()
        ic(nums, k, expected)
        self.assertEqual(expected, Solution().countPairs(nums=nums, k=k))
