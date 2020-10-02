# Done
from collections import deque


class RecentCounter:
    # probar con deque
    def __init__(self):
        self.new = deque()
    def ping(self, t: int) -> int:
        bigger_than = t-3000
        posibles = self.new
        while posibles and (posibles[0] < bigger_than):
            posibles.popleft()
        posibles.append(t)
        return len(posibles)


# Your RecentCounter object will be instantiated and called as such:
def caller(pings, cur):
    tmp = []
    for [i] in pings:
        tmp.append(cur.ping(i))
    return tmp


obj = RecentCounter()
assert (ret := caller([[1], [100], [3001], [3002]], obj)) == [1, 2, 3, 3], ret

print("Tests passed.")