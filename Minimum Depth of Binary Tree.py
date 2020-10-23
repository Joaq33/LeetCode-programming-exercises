# Done
from collections import deque


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = [root]
        level = 1
        while queue:
            next_queue = []
            for node in queue:
                if not node.left and not node.right:
                    return level
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
            level += 1
        return level
    def minDepth2(self, root: TreeNode) -> int: #mio
        if not root:
            return 0
        queue = deque()
        row_number = deque()
        queue.append(root)
        row_number.append(1)
        while queue:
            reference = queue.popleft()
            level = row_number.popleft()
            # print(level, "ref: ",reference.val)
            # print(reference, end=" ")
            if reference.left:
                queue.append(reference.left)
                row_number.append(level+1)
                if reference.right:
                    queue.append(reference.right)
                    row_number.append(level+1)
            elif reference.right:
                queue.append(reference.right)
                row_number.append(level+1)
            else:
                break
        return level