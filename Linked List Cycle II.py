# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head:
            return None
        tortoise = hare = head
        if hare.next and hare.next.next:
            hare = hare.next.next
        else:
            return None
        tortoise = tortoise.next
        while tortoise != hare:
            if hare.next and hare.next.next:
                hare = hare.next.next
            else:
                return None
            tortoise = tortoise.next
        newtortoise = head
        while tortoise != newtortoise:
            tortoise = tortoise.next
            newtortoise = newtortoise.next
        return tortoise