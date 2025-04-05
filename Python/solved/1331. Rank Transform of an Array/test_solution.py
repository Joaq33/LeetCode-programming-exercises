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
        [
            [100, 100, 100],
            [1, 1, 1]
        ], [
            [40, 10, 20, 30],
            [4, 1, 2, 3]
        ], [
            [37, 12, 28, 9, 100, 56, 80, 5, 12],
            [5, 3, 4, 2, 8, 6, 7, 1, 3]
        ]
    ])
    def test_parameterized(self, arr, expected):
        print()
        ic(arr, expected)
        self.assertEqual(expected, Solution().arrayRankTransform(arr=arr))
