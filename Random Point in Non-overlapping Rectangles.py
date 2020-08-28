# Done

import random


class Solution:
    def __init__(self, rects):
        self.weights = [(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rects]
        self.rects = rects

    def pick(self):
        x1, y1, x2, y2 = random.choices(self.rects, weights=self.weights)[0]
        return [random.randint(x1, x2), random.randint(y1, y2)]


# Your Solution object will be instantiated and called as such:
rects = [[1, 1, 5, 5]]
# rects = [[[[-2,-2,-1,-1],[1,0,3,0],[4,6,5,6],[1,0,3,0],[4,6,7,9],[1,0,3,0],[4,6,10,6]]],[],[],[],[],[]]
obj = Solution(rects)
param_1 = obj.pick()
