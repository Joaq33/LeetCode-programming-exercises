import unittest
from solution import Solution
from icecream import ic


class Test(unittest.TestCase):
    def test_1(self):
        """5"""

        numRows = 5
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
        ic(numRows, expected)
        self.assertEqual(expected, Solution().generate(numRows))

    def test_2(self):
        """6"""
        numRows = 6
        expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
        ic(numRows, expected)
        self.assertEqual(expected, Solution().generate(numRows))


if __name__ == '__main__':
    Test().test_1()
