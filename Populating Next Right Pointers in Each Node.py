#Done

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def list_to_btree(l: []) -> Node:
    """
    Convert a list into a binary tree.
    :param l:
    :return:
    """
    head = Node(val=l[0])
    index = 1

    def rec(cur):
        nonlocal index
        if l[index]:
            cur.left = Node(l[index])
        index += 1
        if l[index]:
            cur.right = Node(l[index])
        if cur.left:
            index += 1
            rec(cur.left)
        if cur.right:
            index += 1
            rec(cur.right)

    try:
        rec(head)
    except:
        pass
    return head


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return root
        head = root
        queue = [root]
        while queue:
            next_queue = []
            last = None
            for node in queue:
                if not node.left and not node.right:
                    continue
                if node.right:
                    next_queue.append(node.right)
                    node.right.next = last
                    last = node.right
                if node.left:
                    next_queue.append(node.left)
                    node.left.next = last
                    last = node.left
            queue = next_queue
        return head


obj = Solution()

root = list_to_btree([1, 2, 3, 4, 5, 6, 7])
print(obj.connect(root))
