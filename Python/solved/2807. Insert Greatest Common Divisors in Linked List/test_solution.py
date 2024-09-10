import unittest
from solution import Solution


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


class Test(unittest.TestCase):
    def test_1(self):
        head = [18, 6, 10, 3]
        print("head:", head)
        head = list_to_linked(head)
        expected = [18, 6, 6, 2, 10, 1, 3]
        self.assertEqual(expected, linked_to_list(Solution().insertGreatestCommonDivisors(head=head)))
