# Done


class Solution:
    def numDecodings(self, s: str) -> int: # copied
        if not s:
            return 0

        dp = [0] * (len(s) + 1)
        dp[0] = 1
        for i in range(len(s)):
            if self.isValid(s[i]):
                dp[i + 1] = dp[i]
            if i > 0 and self.isValid(s[i - 1:i + 1]):
                dp[i + 1] += dp[i - 1]
        return dp[-1]

    def isValid(self, s):
        if len(s) == 1 and 0 < int(s) < 10:
            return True
        if len(s) == 2 and 10 <= int(s) <= 26:
            return True
    def numDecodings2(self, s: str) -> int: # incomplete
        prev = ""
        ans = 0
        for n in s:
            if prev == "1":
                ans += 1
            elif prev == "2":
                if int(n) < 8:
                    ans += 1
            prev = n
        return ans


obj = Solution()

s = "0"
assert 0 == (ret := obj.numDecodings(s)), ret

s = "226"
assert 3 == (ret := obj.numDecodings(s)), ret

s = "12"
assert 2 == (ret := obj.numDecodings(s)), ret

print("Tests passed.")
