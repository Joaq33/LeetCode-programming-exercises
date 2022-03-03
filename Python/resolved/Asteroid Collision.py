# Done
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for asteroid in asteroids:
            while True:
                if len(ans) == 0:
                    ans = [asteroid]
                    break
                if asteroid > 0:  # cur positive
                    ans.append(asteroid)
                    break
                else:  # cur negative
                    if ans[-1] < 0:
                        ans.append(asteroid)
                        break
                    else:
                        if ans[-1] == -asteroid:
                            ans.pop()
                            break
                        elif ans[-1] < -asteroid:  # last positive < cur negative
                            ans.pop()
                        else:
                            break
        return ans


obj = Solution()

asteroids = [10, 2, -5]
assert (ret := obj.asteroidCollision(asteroids)) == [10], ret

asteroids = [5, 10, -5]
assert (ret := obj.asteroidCollision(asteroids)) == [5, 10], ret

asteroids = [-2, -1, 1, 2]
assert (ret := obj.asteroidCollision(asteroids)) == [-2, -1, 1, 2], ret

asteroids = [8, -8]
assert (ret := obj.asteroidCollision(asteroids)) == [], ret

print("Tests passed.")
