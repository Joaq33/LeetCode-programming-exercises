class MyCircularDeque:
    """two pointers array aproach"""

    def __init__(self, k: int):
        self.array = [None] * k
        self.head = self.tail = 0
        # it would work without tracking the length too, with minor changes, but the performance difference is not important
        self.len = 0
        self.max_len = k

    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.len += 1

        if self.len != 1:
            self.head -= 1
            if self.head == -1:
                self.head = self.max_len - 1

        self.array[self.head] = value
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.len += 1

        if self.len != 1:
            self.tail += 1
            if self.tail == self.max_len:
                self.tail = 0

        self.array[self.tail] = value
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.array[self.head] = None

        self.len -= 1

        if self.len != 0:
            self.head += 1
            if self.head == self.max_len:
                self.head = 0
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.array[self.tail] = None
        self.len -= 1

        if self.len != 0:
            self.tail -= 1
            if self.tail == -1:
                self.tail = self.max_len - 1
        return True

    def getFront(self) -> int:
        tmp = self.array[self.head]
        return tmp if tmp is not None else -1

    def getRear(self) -> int:
        tmp = self.array[self.tail]
        return tmp if tmp is not None else -1

    def isEmpty(self) -> bool:
        return self.len == 0

    def isFull(self) -> bool:
        return self.len == self.max_len

# from __future__ import annotations
#
#
# class MyCircularDeque:
#     """Linked list approach"""
#
#     class Node:
#         def __init__(self, val: int, prev_node: Node = None, next_node: Node = None):
#             self.val = val
#             self.prev_node = prev_node
#             self.next_node = next_node
#
#     def __init__(self, k: int):
#         self.max_size = k
#         self.cur_size = 0
#         self.head = None
#         self.tail = None
#
#     def _print_vals(self):
#         cur = self.head
#         ret = ""
#         while cur:
#             ret += ", " + str(cur.val)
#             cur = cur.next_node
#         print(ret[2:])
#
#     def insertFront(self, value: int) -> bool:
#         if self.isFull(): return False
#         self.cur_size += 1
#         if self.cur_size == 1:
#             self.head = self.tail = self.Node(value)
#             self._print_vals()
#             return True
#         tmp = self.Node(value, next_node=self.head)
#         self.head.prev_node = tmp
#         self.head = tmp
#         self._print_vals()
#         return True
#
#     def insertLast(self, value: int) -> bool:
#         if self.isFull(): return False
#         self.cur_size += 1
#         if self.cur_size == 1:
#             self.head = self.tail = self.Node(value)
#             self._print_vals()
#             return True
#         tmp = self.Node(value, prev_node=self.tail)
#         self.tail.next_node = tmp
#         self.tail = tmp
#         self._print_vals()
#         return True
#
#     def deleteFront(self) -> bool:
#         if self.isEmpty():
#             return False
#         self.cur_size -= 1
#         if self.isEmpty():
#             self.tail = self.head = None
#             return True
#         self.head = self.head.next_node
#         return True
#
#     def deleteLast(self) -> bool:
#         if self.isEmpty():
#             return False
#         self.cur_size -= 1
#         if self.isEmpty():
#             self.tail = self.head = None
#             return True
#         self.tail = self.tail.prev_node
#         return True
#
#     def getFront(self) -> int:
#         if self.isEmpty(): return -1
#         return self.head.val
#
#     def getRear(self) -> int:
#         if self.isEmpty(): return -1
#         return self.tail.val
#
#     def isEmpty(self) -> bool:
#         return self.cur_size == 0
#
#     def isFull(self) -> bool:
#         return self.cur_size == self.max_size


# # Your MyCircularDeque object will be instantiated and called as such:
# if __name__ == '__main__':
#     obj = MyCircularDeque(5)
#     param_1 = print("obj.insertFront(3)", obj.insertFront(3))
#     param_2 = print("obj.insertLast(2)", obj.insertLast(2))
#     param_3 = print("obj.deleteFront()", obj.deleteFront())
#     param_4 = print("obj.deleteLast()", obj.deleteLast())
#     param_5 = print("obj.getFront()", obj.getFront())
#     param_6 = print("obj.getRear()", obj.getRear())
#     param_7 = print("obj.isEmpty()", obj.isEmpty())
#     param_8 = print("obj.isFull()", obj.isFull())
