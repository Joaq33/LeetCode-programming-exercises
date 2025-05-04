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
            [[1, 2], [2, 1], [3, 4], [5, 6]],
            1
        ],
        [
            [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]],
            3
        ]
    ])
    def test_(self, dominoes, expected):
        print()  # fixes pycharm output
        ic(dominoes, expected)
        self.assertEqual(expected, Solution().numEquivDominoPairs(dominoes=dominoes))
