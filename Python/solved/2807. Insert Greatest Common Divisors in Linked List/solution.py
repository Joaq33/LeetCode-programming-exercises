# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


def gcd(a, b):
    """
    (already exists in leetcode environment)
    The below code demonstrates how to implement
    Euclid's algorithm to find the greatest
    common divisor of two integer values a and b.

    Time complexity: O(log2(min(a, b)))
    Space complexity: O(1)
    """
    while b != 0:
        a, b = b, a % b
    return abs(a)


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tmp = lastnode = head
        tmp = tmp.next
        while tmp:
            lastnode.next = ListNode(val=gcd(lastnode.val, tmp.val), next=tmp)
            lastnode = tmp
            tmp = tmp.next
        return head
