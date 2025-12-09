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
            5,
            2
        ],
        [
            10,
            4
        ]
    ])
    def test_(self, n, expected):
        print()  # fix pycharm output
        ic(n, expected)
        self.assertEqual(expected, Solution().countTriples(n=n))
