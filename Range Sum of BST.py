# Done
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_btree(l: []) -> TreeNode:
    """
    Convert a list into a binary tree.
    :param l:
    :return:
    """
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


def btree_to_list(head: TreeNode) -> []:
    """
    Convert binary-tree into list
    :param head:
    :return:
    """
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


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        ans = 0

        def dfs(node):
            if not node:
                return
            print(node.val)
            nonlocal ans
            if node.val < high and node.val > low:
                ans += node.val
                dfs(node.left)
                dfs(node.right)
            elif node.val == high:
                ans += node.val
                dfs(node.left)
            elif node.val == low:
                ans += node.val
                dfs(node.right)
            elif node.val > high:
                dfs(node.left)
            elif node.val < low:
                dfs(node.right)

        if root.val < high and root.val > low:
            ans = root.val
            dfs(root.left)
            dfs(root.right)
        elif root.val == high:
            ans = root.val
            dfs(root.left)
        elif root.val == low:
            ans = root.val
            dfs(root.right)
        elif root.val > high:
            dfs(root.left)
        elif root.val < low:
            print()
            dfs(root.right)

        return ans


obj = Solution()

root = list_to_btree([18, 9, 27, 6, 15, 24, 30, 3, None, 12, None, 21])
low = 18
high = 24
assert 63 == (ret := obj.rangeSumBST(root, low, high)), ret

root = list_to_btree([15, 9, 21, 7, 13, 19, 23, 5, None, 11, None, 17])
low = 21
high = 23
assert 44 == (ret := obj.rangeSumBST(root, low, high)), ret

root = list_to_btree([10, 5, 15, 3, 7, 13, 18, 1, None, 6])
low = 6
high = 10
assert 23 == (ret := obj.rangeSumBST(root, low, high)), ret

root = list_to_btree([10, 5, 15, 3, 7, None, 18])
low = 7
high = 15
assert 32 == (ret := obj.rangeSumBST(root, low, high)), ret

print("Tests passed.")
