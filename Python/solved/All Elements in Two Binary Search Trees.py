# Done
from typing import List# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans=[]
        def element(root):
            nonlocal ans
            ans.append(root.val)
            if root.left:
                element(root.left)
            if root.right:
                element(root.right)
        if root1:
            element(root1)
        if root2:
            element(root2)
        return sorted(ans)
