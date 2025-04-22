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
            10,
            7,
            3
        ], [
            243,
            640,
            6
        ],
        [
            10,
            82,
            3
        ],
        [
            383,
            181,
            5]
    ])
    def test_(self, start, goal, expected):
        print()  # fix pycharm output
        ic(start, goal, expected)
        self.assertEqual(expected, Solution().minBitFlips(start=start, goal=goal))
