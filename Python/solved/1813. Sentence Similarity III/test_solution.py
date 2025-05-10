import unittest
from pickle import FALSE

from solution import Solution
from icecream import ic
from parameterized import parameterized

ic.use_stdout()


# null = None
# true = True
# false = False


class Test(unittest.TestCase):
    @parameterized.expand([
        [
            "Eating no right now",
            "Eating now",
            True
        ],
        [
            "My name is Haley",
            "My Haley",
            True
        ], [
            "of",
            "A lot of words",
            False
        ], [
            "Eating right now",
            "Eating",
            True
        ], [
            "Luky",
            "Lucccky",
            False
        ], [
            "My name is Haley",
            "My nHaley",
            False
        ], [
            "My name is Haley",
            "Haley",
            True
        ], [
            "xD iP tqchblXgqvNVdi",
            "FmtdCzv Gp YZf UYJ xD iP tqchblXgqvNVdi",
            True
        ], [
            "B",
            "By",
            False
        ], [
            "URhnaPlQqSx h",
            "URhnaPlQqSx RpASX h",
            True
        ], [
            "A A",
            "A aA",
            False
        ], [
            "A A AAa",
            "A AAa",
            True
        ], [
            "C",
            "CB B C",
            True
        ]
    ])
    def test_(self, sentence1, sentence2, expected):
        print()
        ic(sentence1, sentence2, expected)
        self.assertEqual(expected, Solution().areSentencesSimilar(sentence1=sentence1, sentence2=sentence2))
