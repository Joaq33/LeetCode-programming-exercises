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


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        number1 = 0
        while l1:
            number1 = number1 * 10 + l1.val
            l1 = l1.next
        number2 = 0
        while l2:
            number2 = number2 * 10 + l2.val
            l2 = l2.next
        number = str(number1 + number2)
        head = ListNode(val=int(number[0]))
        cur = head
        for letter in number[1:]:
            cur.next = ListNode(int(letter))
            cur = cur.next
        return head

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode) -> ListNode:  # optimal
        a = 0
        b = 0
        head1, head2 = l1, l2
        while head1:
            a = a * 10 + head1.val
            head1 = head1.next
        while head2:
            b = b * 10 + head2.val
            head2 = head2.next
        res = a + b
        new_head = None
        if res == 0:
            return ListNode(0)
        while res:
            val = res % 10
            res = res // 10
            node = ListNode(val)
            node.next = new_head
            new_head = node
        return new_head


obj = Solution()

l1 = list_to_linked([7, 2, 4, 3])
l2 = list_to_linked([5, 6, 4])
assert [7, 8, 0, 7] == (ret := linked_to_list(obj.addTwoNumbers(l1, l2))), ret

l1 = list_to_linked([0])
l2 = list_to_linked([0])
assert [0] == (ret := linked_to_list(obj.addTwoNumbers(l1, l2))), ret

print("Tests passed.")
