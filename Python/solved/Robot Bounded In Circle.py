# Done
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dir_final = 0
        pos = [0, 0]
        go = {0: (0, 1), 1: (0, 1), 2: (0, -1), 3: (0, -1)}
        for action in instructions:
            if action == "G":
                x, y = go[dir_final % 4]
                pos[0] += x
                pos[1] += y
            elif action == "L":
                dir_final -= 1
            elif action == "R":
                dir_final += 1
        if dir_final % 4 != 0 or pos == [0, 0]:
            return True


obj = Solution()
instructions = "LLGRL"
instructions = "RRRLLRGRLLRLGLLLGRGGGRLLRRGRRLGGRLRRRRLRRLLRR"
instructions = "GLRLLGLL"
print(obj.isRobotBounded(instructions))
