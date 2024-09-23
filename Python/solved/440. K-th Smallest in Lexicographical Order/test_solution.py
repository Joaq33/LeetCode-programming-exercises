import unittest
from solution import Solution
from icecream import ic


class Test(unittest.TestCase):
    def test_1(self):
        """n = 13 k =2"""
        n = 13
        k = 2
        expected = 10
        ic(n, k, expected)
        self.assertEqual(expected, Solution().findKthNumber(n, k))

    def test_2(self):
        """n 20 case"""
        n = 20
        k = 4
        expected = 12
        ic(n, k, expected)
        self.assertEqual(expected, Solution().findKthNumber(n, k))

    def test_3(self):
        """n 20 case"""
        n = 1
        k = 1
        expected = 1
        ic(n, k, expected)
        self.assertEqual(expected, Solution().findKthNumber(n, k))

    # def test_3(self):
    #     """n 19 case"""
    #     n = 19
    #     expected = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 3, 4, 5, 6, 7, 8, 9]
    #     ic(n, expected, compact=True)
    #     self.assertEqual(expected, Solution().lexicalOrder(n))
