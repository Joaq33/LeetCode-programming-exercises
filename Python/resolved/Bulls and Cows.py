# Done
from collections import Counter


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        cnt = Counter(secret)
        bulls = cowsandbulls = 0
        for index, item in enumerate(guess):
            if cnt[item] > 0:
                cnt[item] -= 1
                cowsandbulls += 1
            if secret[index] == item:
                bulls += 1
        return str(bulls) + "A" + str(cowsandbulls - bulls) + "B"


obj = Solution()
secret ="1122"
guess = "1133"

print(obj.getHint(secret, guess))