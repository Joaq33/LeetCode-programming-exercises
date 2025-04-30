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
        [
            [12, 345, 2, 6, 7896],
            2
        ],
        [
            [555, 901, 482, 1771],
            1
        ]
    ])
    def test_(self, nums, expected):
        print()  # fix pycharm output
        ic(nums, expected)
        self.assertEqual(expected, Solution().findNumbers(nums=nums))
