import unittest
from solution import Solution
from icecream import ic


class Test(unittest.TestCase):
    def test_1(self):
        """["abc", "ab", "bc", "b"]"""
        numRows = ["abc", "ab", "bc", "b"]
        expected = [5, 4, 3, 2]
        ic(numRows, expected)
        self.assertEqual(expected, Solution().sumPrefixScores(numRows))

    def test_2(self):
        """["abcd"]"""
        numRows = ["abcd"]
        expected = [4]
        ic(numRows, expected)
        self.assertEqual(expected, Solution().sumPrefixScores(numRows))
