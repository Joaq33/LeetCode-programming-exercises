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
            [1, 2, 3, 4, 5, 10, 6, 7, 8, 9],
            5,
            True
        ], [
            [1, 2, 3, 4, 5, 6],
            7,
            True
        ], [
            [1, 2, 3, 4, 5, 6],
            10,
            False
        ], [
            [5, 5, 1, 2, 3, 4, 3, 7],
            10,
            False
        ]
    ])
    def test_parameterized(self, arr, k, expected):
        print()
        ic(arr, k, expected)
        self.assertEqual(expected, Solution().canArrange(arr=arr, k=k))
