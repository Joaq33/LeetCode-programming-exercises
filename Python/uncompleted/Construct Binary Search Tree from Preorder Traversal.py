# not Done
from typing import List, Optional


# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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


class Solution:
    # def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
    #     treelist = [TreeNode(preorder[0])]
    #     comparison = 0
    #     for i in range(1, len(preorder)):
    #         print(preorder[i])
    #         treelist.append(TreeNode(preorder[i]))
    #         if preorder[i] < preorder[comparison]:
    #             treelist[comparison].left = treelist[i]
    #             comparison = i
    #         else:
    #             print("aSD")
    #             print(list(range(i-1, -1, -1)))
    #             for comparison in range(i-1, -1, -1):
    #                 print(preorder[comparison])
    #                 if preorder[comparison] < preorder[i]:
    #                     break
    #
    #     print(btree_to_list(treelist[0]))
    #     return treelist[0]

    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        treelist = [TreeNode(preorder[0])]
        comparison = 0
        cur = 1
        while cur < len(preorder):
            print(preorder[cur])
            treelist.append(TreeNode(preorder[cur]))
            if preorder[cur] < preorder[comparison]:
                treelist[comparison].left = treelist[cur]
                comparison = cur
            else:
                print(cur, preorder[cur])
                temp = cur-1
                maxim_val, maxim_i = preorder[temp], temp
                while preorder[cur] > preorder[temp-1]:
                    temp -= 1
                    if preorder[temp] > maxim_val:
                        maxim_val,maxim_i = preorder[temp], temp
                print(temp, preorder[temp])
                treelist[maxim_i].right = treelist[-1]
                print(btree_to_list(treelist[0]))

            cur += 1

        return treelist[0]

obj = Solution()

pre = [8, 5, 1, 7, 10, 12]
assert list_to_btree([8, 5, 10, 1, 7, None, 12]) == (ret := obj.bstFromPreorder(pre)), btree_to_list(ret)

print("Tests passed.")
