import unittest
from solution import Solution


class Test(unittest.TestCase):
    def test_1(self):
        n = 11
        expected = 3
        self.assertEqual(expected, Solution().hammingWeight(n=n))

    def test_2(self):
        n = 128
        expected = 1
        self.assertEqual(expected, Solution().hammingWeight(n=n))

    def test_3(self):
        n = 2147483645
        expected = 30
        self.assertEqual(expected, Solution().hammingWeight(n=n))
