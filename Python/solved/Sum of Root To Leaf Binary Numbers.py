# Done

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        total = 0
        def dfs(branch, cur):
            nonlocal total
            cur = cur * 2 + branch.val
            hasnext = False
            if branch.right:
                dfs(branch.right, cur)
                hasnext = True
            if branch.left:
                dfs(branch.left, cur)
                hasnext = True
            if not hasnext:
                total += cur
        dfs(root, 0)
        return total