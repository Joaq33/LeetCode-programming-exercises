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
            "leet2code3",
            30,
            "e"
        ], [
            "ha22",
            5,
            "h"
        ], [
            "a2345678999999999999999",
            1,
            "a"
        ], [
            "leet2code3",
            10,
            "o"
        ]
    ])
    def test_(self, s, k, expected):
        print()  # fix pycharm output
        ic(s, k, expected)
        self.assertEqual(expected, Solution().decodeAtIndex(s=s, k=k))
