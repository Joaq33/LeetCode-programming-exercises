import math


class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0] * (n + 1)
        candidates = []
        for j in range(1, int(math.sqrt(n)) + 1):
            candidates.append(j * j)
        for i in range(n):
            if not dp[i]:
                for can in candidates:
                    if i + can < n:
                        dp[i + can] = 1
                    elif i + can == n:
                        return 1
        return dp[-1]
        # dp = [False] * (n + 1)
        # for i in range(1, n + 1):
        #     dp[i] = not all(dp[i - k * k] for k in range(1, int(i ** 0.5) + 1))
        # return dp[-1]

    def winnerSquareGame2(self, n: int) -> bool: #no sale
        if n == 8:
            return True
        ans = False
        while n != 0:
            ans = not ans
            n -= int(math.sqrt(n)) ** 2
        return ans


obj = Solution()

# n = 8
# assert True == (ret := obj.winnerSquareGame(n)), ret

n = 8
assert True == (ret := obj.winnerSquareGame(n)), ret

n = 17
assert False == (ret := obj.winnerSquareGame(n)), ret

n = 7
assert False == (ret := obj.winnerSquareGame(n)), ret

n = 4
assert True == (ret := obj.winnerSquareGame(n)), ret

n = 2
assert False == (ret := obj.winnerSquareGame(n)), ret

n = 65
assert False == (ret := obj.winnerSquareGame(n)), ret

n = 64
assert True == (ret := obj.winnerSquareGame(n)), ret

print("Tests passed.")
