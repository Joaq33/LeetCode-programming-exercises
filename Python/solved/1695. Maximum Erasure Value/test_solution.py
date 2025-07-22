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
            [4, 2, 4, 5, 6],
            17,
        ],
        [
            [5, 2, 1, 2, 5, 2, 1, 2, 5],
            8,
        ]
    ])
    def test_(self, param1, expected):
        print()  # fix pycharm output
        ic(param1, expected)
        self.assertEqual(expected, Solution().maximumUniqueSubarray(nums=param1))
