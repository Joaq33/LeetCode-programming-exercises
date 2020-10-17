# These are some handy functions to enhance the programming experience
def bsearch(self, nums: List[int], target: int) -> int:
    """
    Best binary search time complexity.
    :param self:
    :param nums:
    :param target:
    :return:
    """
    left, right = 0, len(nums)-1
    while left <= right:
        pivot = (left + right)//2
        if target == nums[pivot]:
            return pivot
        if target > nums[pivot]:
            left = pivot+1
        else:
            right = pivot-1
    return -1
def reverse(nums, start, end):
    """
    Reverse a list.
    :param nums:
    :param start:
    :param end:
    :return:
    """
    while start < end:
        nums[start], nums[end - 1] = nums[end - 1], nums[start]
        start += 1
        end -= 1

def linked_to_list(head: ListNode):
    """
    Convert a linked list into a list.
    :param head:
    :return:
    """
    ans = [head.val]
    cur = head
    while cur.next:
        cur = cur.next
        ans.append(cur.val)
    return ans


def list_to_linked(list: []):
    """
    Convert a list into a linked list.
    :param list:
    :return:
    """
    head = ListNode(list[0])
    cur = head
    for item in list[1:]:
        cur.next = ListNode(item)
        cur = cur.next
    return head