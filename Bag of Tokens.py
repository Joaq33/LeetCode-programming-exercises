from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        if not tokens or P < tokens[0]:
            return 0
        score = 0
        left, right = 0, len(tokens) - 1
        while left <= right:
            if P >= tokens[left]:
                P -= tokens[left]
                left += 1
                score += 1
            elif right-left <= 1:
                return score
            else:
                P += tokens[right]
                right -= 1
                score -= 1
        return score
    def bagOfTokensScore2(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        if not tokens or P < tokens[0]:
            return 0
        left = score = last = 0
        right = len(tokens) - 1
        while left <= right:
            if tokens[left] <= P:
                score += 1
                P -= tokens[left]
                left += 1
                last = 0
            elif score == 0:
                return 0
            else:
                score -= 1
                P += tokens[right]
                right -= 1
                last += 1
        return score + last

obj = Solution()

tokens = [71, 55, 82]
P = 54
assert (ret := obj.bagOfTokensScore(tokens, P)) == 0, ret

tokens = [100, 200]
P = 150
assert (ret := obj.bagOfTokensScore(tokens, P)) == 1, ret

tokens = [81, 91, 31]
P = 73
assert (ret := obj.bagOfTokensScore(tokens, P)) == 1, ret

tokens = [100, 200]
P = 150
assert (ret := obj.bagOfTokensScore(tokens, P)) == 1, ret

tokens = [100, 200, 300, 400]
P = 200
assert (ret := obj.bagOfTokensScore(tokens, P)) == 2, ret

tokens = [100]
P = 50
assert (ret := obj.bagOfTokensScore(tokens, P)) == 0, ret

print("Tests passed.")
