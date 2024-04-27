# Done
class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0
        cur = ""
        cur_lar = 0
        for letter in s:
            if letter == cur:
                cur_lar += 1
            else:
                ans = max(ans, cur_lar)
                cur = letter
                cur_lar = 1
        ans = max(ans, cur_lar)
        return ans


obj = Solution()

s = "leetcode"
assert 2 == (ret := obj.maxPower(s)), ret

s = "abbcccddddeeeeedcba"
assert 5 == (ret := obj.maxPower(s)), ret

print("Tests passed.")
