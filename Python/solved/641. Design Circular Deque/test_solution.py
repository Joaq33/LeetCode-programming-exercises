import unittest
from solution import MyCircularDeque
from icecream import ic
from parameterized import parameterized

null = None
true = True
false = False


class Test(unittest.TestCase):
    @parameterized.expand([
        [
            ["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull",
             "deleteLast", "insertFront", "getFront"],
            [[3], [1], [2], [3], [4], [], [], [], [4], []],
            [None, True, True, True, False, 2, True, True, True, 4]
        ], [
            ["MyCircularDeque", "insertFront", "deleteLast", "getRear", "getFront", "getFront", "deleteFront",
             "insertFront", "insertLast", "insertFront", "getFront", "insertFront"],
            [[4], [9], [], [], [], [], [], [6], [5], [9], [], [6]],
            [None, True, True, -1, -1, -1, False, True, True, True, 9, True]
        ], [
            ["MyCircularDeque", "insertFront", "insertLast", "getFront", "insertLast", "getFront", "insertFront",
             "getRear", "getFront", "getFront", "deleteLast", "getRear"],
            [[5], [7], [0], [], [3], [], [9], [], [], [], [], []],
            [None, True, True, 7, True, 7, True, 3, 9, 9, True, 0]
        ], [
            ["MyCircularDeque", "insertFront", "deleteLast", "getFront", "insertLast", "insertFront", "getFront",
             "getRear", "getFront", "getFront", "getRear", "insertLast"],
            [[2], [7], [], [], [5], [0], [], [], [], [], [], [0]],
            [null, true, true, -1, true, true, 0, 5, 0, 0, 5, false]
        ]
    ])
    def test_parameterized(self, calls, calls_vals, expected):
        print()
        ic(calls, calls_vals, expected)
        obj = MyCircularDeque(calls_vals[0][0])
        output = [None]
        # ic(zip(calls, calls_vals))
        for i in range(1, len(calls)):

            method_name = calls[i]
            v = calls_vals[i]
            if v:
                v = v[0]
            else:
                v = None
            call = getattr(obj, method_name)
            ic("calling:", method_name, v)
            if v is not None:
                output.append(call(v))
            else:
                output.append(call())
            # print("    output", output[-1])
            # print('   ', obj.array)
            ic(output[-1], obj.array, obj.head, obj.array[obj.head], obj.tail, obj.array[obj.tail])

        self.assertEqual(expected, output)
