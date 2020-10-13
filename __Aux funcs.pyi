# These are some handy functions to enhance the programming experience

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