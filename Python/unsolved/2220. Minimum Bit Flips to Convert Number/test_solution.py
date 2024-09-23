import unittest
from solution import Solution
from icecream import ic

class Test(unittest.TestCase):
    def test_1(self):
        """expect 3"""
        start = 10
        goal = 7
        expected = 3

        ic(start, goal, expected)
        print("asd?")
        self.assertEqual(expected, Solution().minBitFlips(start=start, goal=goal))

    def test_2(self):
        """expect 3"""
        start = 10
        goal = 82
        expected = 3

        ic(start, goal, expected)
        self.assertEqual(expected, Solution().minBitFlips(start=start, goal=goal))
