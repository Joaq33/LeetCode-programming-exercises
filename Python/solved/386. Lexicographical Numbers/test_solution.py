import unittest
from solution import Solution
from icecream import ic


class Test(unittest.TestCase):
    def test_1(self):
        """n 13 case"""
        n = 13
        expected = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
        ic(n, expected)
        self.assertEqual(expected, Solution().lexicalOrder(n))

    def test_2(self):
        """n 20 case"""
        n = 20
        expected = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 8, 9]
        ic(n, expected, compact=True)
        self.assertEqual(expected, Solution().lexicalOrder(n))

    def test_3(self):
        """n 19 case"""
        n = 19
        expected = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 3, 4, 5, 6, 7, 8, 9]
        ic(n, expected, compact=True)
        self.assertEqual(expected, Solution().lexicalOrder(n))
