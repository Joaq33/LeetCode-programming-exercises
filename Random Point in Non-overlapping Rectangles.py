# Done but not returning

import random


class Solution:

    def __init__(self, rects):
        self.probabilities = 0
        self.list_prob = []
        for rectangle in rects[0][0]:
            print(rectangle)
            ancho = rectangle[2] - rectangle[0]
            if ancho == 0:
                ancho = 1
            alto = rectangle[3] - rectangle[1]
            if alto == 0:
                alto = 1
            self.list_prob.append(ancho * alto)
            self.probabilities += ancho * alto

    def pick(self):

        pick = random.randrange(self.probabilities) + 1
        whichrec = -1
        while pick > 0:
            whichrec += 1
            pick -= self.list_prob[whichrec]
        return [-pick % 4, (-pick) // 4]


# Your Solution object will be instantiated and called as such:
rects = [[[[1, 1, 5, 5]]], [], [], []]
# rects = [[[[-2,-2,-1,-1],[1,0,3,0],[4,6,5,6],[1,0,3,0],[4,6,7,9],[1,0,3,0],[4,6,10,6]]],[],[],[],[],[]]
obj = Solution(rects)
param_1 = obj.pick()
