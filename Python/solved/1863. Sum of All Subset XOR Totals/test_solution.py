import unittest
from solution import Solution
from icecream import ic
from parameterized import parameterized

ic.use_stdout()

null = None
true = True
false = False


class Test(unittest.TestCase):
    @parameterized.expand([
        [[1, 3], 6],
        [[5, 1, 6], 28],
        [[3, 4, 5, 6, 7, 8], 480]
    ])
    def test_(self, nums, expected):
        print()
        ic(nums, expected)
        self.assertEqual(expected, Solution().subsetXORSum(nums=nums))
