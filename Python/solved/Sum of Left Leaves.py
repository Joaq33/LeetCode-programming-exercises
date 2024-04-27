# Done

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        def rec(node, isleft):
            if not (node.left or node.right):
                return node.val * isleft
            branches = 0
            if node.left:
                branches += rec(node.left, True)
            if node.right:
                branches += rec(node.right, False)
            return branches
        return rec(root, False)

obj = Solution()
param1 = TreeNode(3, left=TreeNode(9), right=TreeNode(20,left=TreeNode(15),right=TreeNode(7)))
print(obj.sumOfLeftLeaves(param1))