# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def btree_to_list(head: TreeNode):
    ans = [head.val]

    def rec(cur):
        queue = []
        if cur.left:
            ans.append(cur.left.val)
            queue.append(cur.left)
        else:
            ans.append(None)
        if cur.right:
            ans.append(cur.right.val)
            queue.append(cur.right)
        else:
            ans.append(None)
        for item in queue:
            rec(item)

    rec(head)
    last = len(ans) - 1
    while not ans[last]:
        last -= 1
    return ans[:last + 1]


def list_to_btree(l: []):
    head = TreeNode(val=l[0])
    index = 1

    def rec(cur):
        nonlocal index
        if l[index]:
            cur.left = TreeNode(l[index])
        index += 1
        if l[index]:
            cur.right = TreeNode(l[index])
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
    _previous = None
    _swapA = _swapB = None

    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
      self._coverTree(root)

      # Swap the node's value
      if self._swapA is not None and self._swapB is not None:
        temp = self._swapA.val
        self._swapA.val = self._swapB.val
        self._swapB.val = temp

      return root

    # @param root, a tree node
    # @return a tree node
    def _coverTree(self, root):
      if root is None or root.val is None:
        return

      self._coverTree(root.left)

      if self._previous is not None and self._previous.val is not None:
        if self._previous.val > root.val:
          if self._swapA is None:
            self._swapA = self._previous
          self._swapB = root

      self._previous = root
      self._coverTree(root.right)
    # def recoverTree(self, root: TreeNode) -> None: don't work between branches
    #     """
    #     Do not return anything, modify root in-place instead.
    #     """
    #
    #     def dfs(cur, left, right):
    #         print(cur.val)
    #         tmp1 = None
    #         if left:
    #             if cur.left:
    #                 if left.val < cur.left.val:
    #                     if cur.left.val < cur.val:
    #                         print()
    #                         tmp1 = cur.left
    #                     else:
    #                         cur.left.val, cur.val = cur.val, cur.left.val
    #                         return True
    #                 else:
    #                     cur.left.val, left.val = left.val, cur.left.val
    #                     return True
    #         else:
    #             if cur.left:
    #                 if cur.left.val < cur.val:
    #                     tmp1 = cur.left
    #                 else:
    #                     cur.left.val, cur.val = cur.val, cur.left.val
    #                     return True
    #
    #         tmp2 = None
    #         if right:
    #             if cur.right:
    #                 if cur.val < cur.right.val:
    #                     if cur.right.val < right.val:
    #                         tmp2 = cur.right
    #                     else:
    #                         cur.right.val, right.val = right.val, cur.right.val
    #                         return True
    #                 else:
    #                     cur.val, cur.right.val = cur.right.val, cur.val
    #                     return True
    #         else:
    #             if cur.right:
    #                 if cur.val < cur.right.val:
    #                     tmp2 = cur.right
    #                 else:
    #                     cur.val, cur.right.val = cur.right.val, cur.val
    #                     return True
    #
    #         if tmp1:
    #             if dfs(tmp1, left, cur):
    #                 return True
    #         if tmp2:
    #             if dfs(tmp2, cur, right):
    #                 return True
    #         return False
    #
    #     dfs(root, None, None)


obj = Solution()

root = [2, 3, 1]
tree = list_to_btree(root)
obj.recoverTree(tree)
assert (ret := btree_to_list(tree)) == [2, 1, 3], ret

root = [3, 1, 4, None, None, 2]
tree = list_to_btree(root)
obj.recoverTree(tree)
assert (ret := btree_to_list(tree)) == [2, 1, 4, None, None, 3], ret

print("Tests passed.")
