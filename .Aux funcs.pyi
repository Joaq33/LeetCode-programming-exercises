# These are some handy functions to enhance the programming experience

#############################################################
#############################################################

# infinite while counter (Optimal for bfs)
from itertools import count

for step in count():
    print(step)


#############################################################
#############################################################

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


#############################################################
#############################################################

def bsearch(self, nums: List[int], target: int) -> int:
    """
    Best binary search time complexity.
    :param self:
    :param nums:
    :param target:
    :return:
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = (left + right) // 2
        if target == nums[pivot]:
            return pivot
        if target > nums[pivot]:
            left = pivot + 1
        else:
            right = pivot - 1
    return -1


def bfs(self, root: TreeNode) -> int:
    """
    extraido de minimum depth of binary tree
    PROBABLEMENTE MEJOR Q EL DE ABAJO
    :param self:
    :param root:
    :return:
    """
    if not root: return 0
    queue = [root]
    level = 1
    while queue:
        next_queue = []
        for node in queue:
            if not node.left and not node.right:
                return level
            if node.left:
                next_queue.append(node.left)
            if node.right:
                next_queue.append(node.right)
        queue = next_queue
        level += 1
    return level


def BFS(self, s):
    """
    Breadth First Search
    PROBABLEMENTE PEOR Q EL DE ARRIBA(mucho)
    :param self:
    :param s:
    :return:
    """
    from collections import deque
    # Mark all the vertices as not visited
    visited = [False] * (len(self.graph))

    # Create a queue for BFS
    queue = deque()

    # Mark the source node as
    # visited and enqueue it
    queue.append(s)
    visited[s] = True

    while queue:

        # Dequeue a vertex from
        # queue and print it
        s = queue.popleft()
        print(s, end=" ")

        # Get all adjacent vertices of the
        # dequeued vertex s. If a adjacent
        # has not been visited, then mark it
        # visited and enqueue it
        for i in self.graph[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True


#############################################################
#############################################################

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


#############################################################
#############################################################

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


#############################################################
#############################################################

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


#############################################################
#############################################################

def list_to_btree(l: []) -> TreeNode:
    """
    Convert a list into a binary tree.
    :param l:
    :return:
    """
    head = TreeNode(val=l[0])
    index = 1

    def rec(cur):
        nonlocal index
        if l[index]:
            cur.left = TreeNode(l[index])
        index += 1
        if l[index]:
            cur.right = TreeNode(l[index])
        if cur.left:
            index += 1
            rec(cur.left)
        if cur.right:
            index += 1
            rec(cur.right)

    try:
        rec(head)
    except:
        pass
    return head


def btree_to_list(head: TreeNode) -> []:
    """
    Convert binary-tree into list
    :param head:
    :return:
    """
    ans = [head.val]

    def rec(cur):
        queue = []
        if cur.left:
            ans.append(cur.left.val)
            queue.append(cur.left)
        else:
            ans.append(None)
        if cur.right:
            ans.append(cur.right.val)
            queue.append(cur.right)
        else:
            ans.append(None)
        for item in queue:
            rec(item)

    rec(head)
    last = len(ans) - 1
    while not ans[last]:
        last -= 1
    return ans[:last + 1]


#############################################################
#############################################################

# to write a List to a .txt
# define list of places
places_list = ['Berlin', 'Cape Town', 'Sydney', 'Moscow']

with open('listfile.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % place for place in places_list)

# this part is in another file
# define empty list
places = []

# open file and read the content in a list
with open('listfile.txt', 'r') as filehandle:
    filecontents = filehandle.readlines()

    for line in filecontents:
        # remove linebreak which is the last character of the string
        current_place = line[:-1]

        # add item to the list
        places.append(current_place)

#############################################################
#############################################################
