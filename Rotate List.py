# Done
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # def rotateRight(self, head: ListNode, k: int) -> ListNode:
    #     if k == 0 or not head:
    #         return head
    #     count = 1
    #     cur = head
    #     newtail = head
    #     while cur.next:
    #         cur = cur.next
    #         count += 1
    #         if count > k + 1:
    #             newtail = newtail.next
    #             # print(linked_to_list(newtail))
    #     if count > k:
    #         tmp = newtail
    #         newtail = newtail.next
    #         tmp.next = None
    #         cur.next = head
    #         return newtail
    #     cur.next = newhead = head
    #     pos = count - k % count - 1
    #     for _ in range(pos):
    #         newhead = newhead.next
    #     tmp = newhead
    #     newhead = newhead.next
    #     tmp.next = None
    #     print(linked_to_list(newhead))
    #     return newhead

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head:
            return head
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        remain = length - k % length - 1
        tail.next = newhead = head
        for _ in range(remain):
            newhead = newhead.next
        tmp = newhead
        newhead = newhead.next
        tmp.next = None
        return newhead


def linked_to_list(head: ListNode):
    ans = [head.val]
    cur = head
    while cur.next:
        cur = cur.next
        ans.append(cur.val)
    return ans


def list_to_linked(list: []):
    head = ListNode(list[0])
    cur = head
    for item in list[1:]:
        cur.next = ListNode(item)
        cur = cur.next
    return head


obj = Solution()

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))  # [1,2,3,4,5]
k = 2
# assert (ret := linked_to_list(obj.rotateRight(head, k))) == [4, 5, 1, 2, 3], ret

head = list_to_linked([0, 1, 2])
k = 4
assert (ret := linked_to_list(obj.rotateRight(head, k))) == [2, 0, 1], ret

head = list_to_linked([1, 2])
k = 1
assert (ret := linked_to_list(obj.rotateRight(head, k))) == [2, 1], ret

print("Tests passed.")
