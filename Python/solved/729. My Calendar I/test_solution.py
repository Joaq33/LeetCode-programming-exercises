import unittest
from solution import MyCalendar
from icecream import ic


class Test(unittest.TestCase):
    def test_1(self):
        """[[], [10, 20], [15, 25], [20, 30]]"""
        # calls_b = ["MyCalendar", "book", "book", "book"]
        calls = [[], [10, 20], [15, 25], [20, 30]]
        expected = [None, True, False, True]

        ic(calls, expected)
        obj = MyCalendar()
        output = [None]
        for i in calls[1:]:
            output.append(obj.book(*i))
        self.assertEqual(expected, output)

    def test_2(self):
        """[[],[47,50],[33,41],[39,45],[33,42],[25,32],[26,35],[19,25],[3,8],[8,13],[18,27]]"""
        calls = [[], [47, 50], [33, 41], [39, 45], [33, 42], [25, 32], [26, 35], [19, 25], [3, 8], [8, 13], [18, 27]]
        expected = [None, True, True, False, False, True, False, True, True, True, False]

        ic(calls, expected)
        obj = MyCalendar()
        output = [None]
        for i in calls[1:]:
            output.append(obj.book(*i))
        self.assertEqual(expected, output)
