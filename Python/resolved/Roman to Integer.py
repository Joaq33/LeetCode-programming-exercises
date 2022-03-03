# Done
class Solution:
    def romanToInt2(self, s: str) -> int:
        lookup = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        previousVal = -1
        for i in range(len(s)):
            currentVal = lookup[s[len(s) - 1 - i]]
            print(previousVal,currentVal)
            if previousVal > currentVal:
                currentVal *= -1
            ans = ans + currentVal
            previousVal = currentVal
        return ans

    def romanToInt(self, s: str) -> int:
        val = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = last = 0
        for letter in s:
            cur = val[letter]
            if cur > last:
                ans += cur - last * 2
            else:
                ans += cur
            last = cur
        return ans


obj = Solution()

assert 11 == (ret := obj.romanToInt("XI")), ret

assert 9 == (ret := obj.romanToInt("IX")), ret

assert 4 == (ret := obj.romanToInt("IV")), ret

assert 3 == (ret := obj.romanToInt("III")), ret

print("Tests passed.")
