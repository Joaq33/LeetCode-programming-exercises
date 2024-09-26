class Node:
    def __init__(self, start, end, prev_node=None, next_node=None):
        self.start = start
        self.end = end
        self.prev_node = prev_node
        self.next_node = next_node


class MyCalendar:
    """
    o(n) time
    o(n) space
    """
    def __init__(self):
        self.events = None

    def book(self, start: int, end: int) -> bool:
        if self.events is None:
            self.events = Node(start=start, end=end)
            return True

        cur = self.events
        while True:
            if cur.start < start:
                if cur.end < start:
                    if cur.next_node:
                        cur = cur.next_node
                    else:
                        cur.next_node = Node(start=start, end=end, prev_node=cur)
                        return True
                elif cur.end == start:
                    if not cur.next_node:
                        cur.end = end
                        return True
                    if end <= cur.next_node.start:
                        cur.end = end
                        return True
                    else:
                        return False
                else:
                    return False

            elif cur.start == start:
                return False

            else:
                if end < cur.start:
                    if cur.prev_node:
                        tmp = Node(start=start, end=end, prev_node=cur.prev_node, next_node=cur)
                        cur.prev_node.next_node = tmp
                        cur.prev_node = tmp

                    else:
                        cur.prev_node = Node(start=start, end=end, next_node=cur)
                        self.events = cur.prev_node
                    return True
                elif end == cur.start:
                    cur.start = start
                    return True
                else:
                    return False
