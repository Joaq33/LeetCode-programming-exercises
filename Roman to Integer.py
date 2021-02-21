# Done
class Solution:
    def romanToInt(self, s: str) -> int:
        val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = last = 0
        for letter in s:
            cur = val[letter]
            # print(cur,last)
            if cur > last:
                ans += cur - last * 2
            else:
                ans += cur
            last = cur
        return ans


obj = Solution()

assert 9 == (ret := obj.romanToInt("IX")), ret

assert 4 == (ret := obj.romanToInt("IV")), ret

assert 3 == (ret := obj.romanToInt("III")), ret

print("Tests passed.")
