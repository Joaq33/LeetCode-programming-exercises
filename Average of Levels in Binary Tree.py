# Done
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = [root]
        ans = []
        while queue:
            nextqueue = []
            recuento = 0
            for node in queue:
                recuento += node.val
                if node.left:
                    nextqueue.append(node.left)
                if node.right:
                    nextqueue.append(node.right)
            ans.append(recuento / len(queue))
            queue = nextqueue
        return ans


obj = Solution()
assert [3, 9, 20, 15, 7] == (ret := obj.averageOfLevels(root))

print("Tests passed.")
