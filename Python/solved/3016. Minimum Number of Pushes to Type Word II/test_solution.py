import unittest
from solution import Solution


class Test(unittest.TestCase):
    def test_1(self):
        word = "abcde"
        expected = 5
        self.assertEqual(expected, Solution().minimumPushes(word=word))

    def test_2(self):
        word = "xyzxyzxyzxyz"
        expected = 12
        self.assertEqual(expected, Solution().minimumPushes(word=word))

    def test_3(self):
        word = "aabbccddeeffgghhiiiiii"
        expected = 24
        self.assertEqual(expected, Solution().minimumPushes(word=word))
