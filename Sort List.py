# Donem
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        arr = []

        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next

        arr.sort()

        cur = head
        for n in arr:
            cur.val = n
            cur = cur.next

        return head

    def sortList2(self, head: ListNode) -> ListNode:
        if not head:
            return
        left = right = head
        while head.next:
            head = head.next
            if right.val <= head.val:
                right.next = head
                right = right.next
            else:
                previous = left
                place_to_search = left
                if left.val >= head.val:
                    tmp = left
                    left = ListNode(head.val, tmp)
                    continue
                while True:
                    previous = place_to_search
                    place_to_search = place_to_search.next
                    if place_to_search.val >= head.val:
                        previous.next = ListNode(head.val, place_to_search)
                        break
        right.next = None
        return left


obj = Solution()
head = list_to_linked([-1, 5, 3, 4, 0])
# assert linked_to_list(ret := obj.sortList(head)) == [-1, 0, 3, 4, 5], linked_to_list(ret)

head = list_to_linked([-1, 5, 3, -2, 4, 0])
assert linked_to_list(ret := obj.sortList(head)) == [-2, -1, 0, 3, 4, 5], linked_to_list(ret)

print("Tests passed")
