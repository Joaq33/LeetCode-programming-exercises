import unittest
from solution import Solution


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.children = [self.left, self.right]


def creatBTree(lst) -> TreeNode:
    if len(lst) == 0:
        return None
    nodes = [None if val is None else TreeNode(val) for val in lst]
    # nodes = [None if val == 'null' else TreeNode(int(val)) for val in string.strip('[]').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


null = None


class Test(unittest.TestCase):
    def test_1(self):
        root = [1, null, 2, 3]
        expected = [3, 2, 1]
        print('root', root)
        self.assertEqual(expected, Solution().postorderTraversal(root=creatBTree(root)))

    def test_2(self):
        root = []
        expected = []
        print('root', root)
        self.assertEqual(expected, Solution().postorderTraversal(root=creatBTree(root)))

    def test_3(self):
        root = [1]
        expected = [1]
        print('root', root)
        self.assertEqual(expected, Solution().postorderTraversal(root=creatBTree(root)))

    def test_4(self):
        root = [3, 1, 2]
        expected = [1, 2, 3]
        print('root', root)
        self.assertEqual(expected, Solution().postorderTraversal(root=creatBTree(root)))

    def test_5(self):
        root = [3, 1, 2, 4, null, 7]
        expected = [4, 1, 7, 2, 3]
        print('root', root)
        self.assertEqual(expected, Solution().postorderTraversal(root=creatBTree(root)))
