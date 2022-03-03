# Done
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        if not head.next:
            return

        def addnode(node, value):
            node.next = ListNode(value)
            return node.next

        listofnodes = []
        actualnode = head
        while True:
            listofnodes.append(actualnode.val)
            if actualnode.next:
                actualnode = actualnode.next
            else:
                break

        currentnode = head
        largo = len(listofnodes)
        for nodeindex in range(largo // 2):
            if nodeindex != 0:
                currentnode = addnode(currentnode, listofnodes[nodeindex])
            currentnode = addnode(currentnode, listofnodes[largo - nodeindex - 1])
        if largo % 2:
            currentnode.next = ListNode(listofnodes[largo // 2])


coso = Solution()
LNode = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
coso.reorderList(LNode)
