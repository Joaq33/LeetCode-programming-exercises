# Done
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def linked_to_list(head: ListNode):
    """
    Convert a linked list into a list.
    :param head:
    :return:
    """
    if not head:
        return None
    ans = [head.val]
    cur = head
    while cur.next:
        cur = cur.next
        ans.append(cur.val)
    return ans


def list_to_linked(l: []):
    """
    Convert a list into a linked list.
    :param l:
    :return:
    """
    if not l:
        return None
    head = ListNode(l[0])
    cur = head
    for item in l[1:]:
        cur.next = ListNode(item)
        cur = cur.next
    return head


import bisect


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        ans = []
        clon = clon2 = head

        while head:
            ans.insert(bisect.bisect(ans, head.val), head.val)
            head = head.next
        i = 0
        while clon:
            clon.val = ans[i]
            i += 1
            clon = clon.next
        return clon2


obj = Solution()

head = list_to_linked([])
assert [] == (ret := linked_to_list(obj.insertionSortList(head))), ret

head = list_to_linked([4, 2, 1, 3])
assert [1, 2, 3, 4] == (ret := linked_to_list(obj.insertionSortList(head))), ret

print("Tests passed.")
