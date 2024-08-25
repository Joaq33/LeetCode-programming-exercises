import unittest
from solution import Solution


class Test(unittest.TestCase):
    def test_1(self):
        n = "1"
        expected = "0"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_123(self):
        n = "123"
        expected = "121"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_12345(self):
        n = "12345"
        expected = "12321"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_807045053224792883(self):
        n = "807045053224792883"
        expected = "807045053350540708"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_11(self):
        n = "11"
        expected = "9"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_88(self):
        n = "88"
        expected = "77"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_12321(self):
        n = "12321"
        expected = "12221"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_1221(self):
        n = "1221"
        expected = "1111"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_100(self):
        n = "100"
        expected = "99"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_230(self):
        n = "230"
        expected = "232"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_99(self):
        n = "99"
        expected = "101"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_11011(self):
        n = "11011"
        expected = "11111"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_1283(self):
        n = "1283"
        expected = "1331"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_12021(self):
        n = "12021"
        expected = "11911"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_12(self):
        n = "12"
        expected = "11"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))

    def test_76(self):
        n = "76"
        expected = "77"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))
    def test_9(self):
        n = "9"
        expected = "8"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))
    def test_10001(self):
        n = "10001"
        expected = "9999"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))
    def test_123892133(self):
        n = "123892133"
        expected = "123888321"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))
    def test_1837722381(self):
        n = "1837722381"
        expected = "1837667381"
        self.assertEqual(expected, Solution().nearestPalindromic(n=n))
