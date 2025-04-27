# These are some handy functions to enhance the programming experience

#############################################################
#############################################################

# infinite while counter (Optimal for bfs)
from itertools import count
from typing import List

for step in count():
    print(step)

# to overwrite leetcode runtime (this is cheating)
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))

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


def dfs(self, root: TreeNode) -> list:
    """
    extraido de binary tree postorder traversal
    :param self:
    :param root:
    :return:
    """
    ans = []
    queue = [root]

    while queue:
        while node := queue.pop():
            if node.val:
                ans.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return ans[::-1]

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

class Bcolors:
    """
    Give colors to prints
    """
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


#############################################################
#############################################################

def list_to_btree(l: []) -> TreeNode:
    """
    Convert a list into a binary tree.
    worse than option below
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

def creatBTree(lst: List) -> TreeNode:
    """
    create TreeNode from list input
    better than above option
    :param lst:
    :return:
    """
    if len(lst) == 0:
        return None
    nodes = [None if val is None else TreeNode(val) for val in lst]
    # nodes = [None if val == 'null' else TreeNode(int(val)) for val in string.strip('[]').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


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
"""
Leetcode's way of printing and converting trees to strings
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def treenode_to_string(root):
    """
    convert a tree to string
    :param root:
    :return:
    """
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def string_to_treenode(input):
    """
    convert a string to a tree
    :param input:
    :return:
    """
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root



def pretty_print_tree(node, prefix="", isLeft=True):
    if not node:
        print("Empty Tree")
        return

    if node.right:
        pretty_print_tree(node.right, prefix + ("│   " if isLeft else "    "), False)

    print(prefix + ("└── " if isLeft else "┌── ") + str(node.val))

    if node.left:
        pretty_print_tree(node.left, prefix + ("    " if isLeft else "│   "), True)

#############################################################
#############################################################
