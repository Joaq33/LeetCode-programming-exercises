import unittest
from solution import Solution
from icecream import ic


class Test(unittest.TestCase):
    def test_1(self):
        """leetscode"""
        s = "leetscode"
        dictionary = ["leet", "code", "leetcode"]
        expected = 1
        ic(s, dictionary, expected)
        self.assertEqual(expected, Solution().minExtraChar(s, dictionary))

    def test_2(self):
        """sayhelloworld"""
        s = "sayhelloworld"
        dictionary = ["hello", "world"]
        expected = 3
        ic(s, dictionary, expected)
        self.assertEqual(expected, Solution().minExtraChar(s, dictionary))

    def test_3(self):
        """sayhelloworld"""
        s = "he"
        dictionary = ["h"]
        expected = 1
        ic(s, dictionary, expected)
        self.assertEqual(expected, Solution().minExtraChar(s, dictionary))


if __name__ == '__main__':
    Test().test_3()
