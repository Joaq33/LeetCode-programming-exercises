from collections import deque
from typing import List
from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        queue = [root]

        while queue:
            while node := queue.pop():
                if node.val:
                    ans.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return ans[::-1]
