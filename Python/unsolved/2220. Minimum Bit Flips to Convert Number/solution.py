from icecream import ic


class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ic(start, str(bin(start)))
        ic(goal, bin(goal))
        bstart = ic(bin(start)[:1:-1])
        bgoal = ic(bin(goal)[:1:-1])

        ans = abs(len(bgoal) - len(bstart))
        ic(ans, len(bgoal), len(bstart))
        ans += sum([a != b for a, b in zip(bstart, bgoal)])
        print(ans)
        return ans
