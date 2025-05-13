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
            [1, 2],
            1
        ],
        [
            [1, 1],
            0
        ], [
            [2, 1],
            0
        ], [
            [1, 2, 3],
            2
        ], [
            [7, 1, 5, 3, 6, 4],
            7
        ], [
            [1, 2, 3, 4, 5],
            4
        ], [
            [7, 6, 4, 3, 1],
            0
        ], [
            [34, 82, 16, 74, 55, 46, 44, 25, 96, 80, 51, 62, 73, 26, 76, 30, 20, 30, 55, 6, 3, 93, 74, 80, 8, 13, 3, 82,
             1, 35, 68, 22, 81, 63, 77, 41, 51, 84, 36, 46, 86, 71, 5, 65, 65, 91, 97, 57, 92, 96, 57, 97, 74, 33, 19,
             42, 44, 22, 12, 26],
            907
        ]
    ])
    def test_(self, prices, expected):
        print()  # fix pycharm output
        ic(prices, expected)
        self.assertEqual(expected, Solution().maxProfit(prices=prices))
