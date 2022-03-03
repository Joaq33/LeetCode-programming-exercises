# Done

class Solution:
    def intToRoman(self, num: int) -> str: #generalized
        ref = dict()
        ref[1] = "I"
        ref[5] = "V"
        ref[10] = "X"
        ref[50] = "L"
        ref[100] = "C"
        ref[500] = "D"
        ref[1000] = "M"
        ans = ""
        for pivot in (10 ** i for i in reversed(range(4))):
            (factor, num) = divmod(num, pivot)
            if factor < 4:
                ans += ref[pivot] * factor
            elif factor == 4:
                ans += ref[pivot] + ref[pivot * 5]
            elif factor == 9:
                ans += ref[pivot] + ref[pivot * 10]
            else:
                ans += ref[pivot*5] + ref[pivot]*(factor-5)
        return ans
    def intToRoman2(self, num: int) -> str: #copied
        order = "IVXLCDM"
        num_dict = {}
        num_dict["I"] = 1
        num_dict["V"] = 5
        num_dict["X"] = 10
        num_dict["L"] = 50
        num_dict["C"] = 100
        num_dict["D"] = 500
        num_dict["M"] = 1000

        result = ""
        if num >= 1000:
            (x, y) = divmod(num, 1000)
            result += "M" * x
            num = y
        if num >= 100:
            (x, y) = divmod(num, 100)
            if x == 9:
                result += "CM"
            elif x >= 5:
                result += "D"
                result += "C" * (x - 5)
                num = y
            elif x == 4:
                result += "CD"
            else:
                result += "C" * x
            num = y
        if num >= 10:
            (x, y) = divmod(num, 10)
            if x == 9:
                result += "XC"
            elif x >= 5:
                result += "L"
                result += "X" * (x - 5)
            elif x == 4:
                result += "XL"
            else:
                result += "X" * x
            num = y
        if num <= 9:
            if num == 9:
                result += "IX"
            elif num >= 5:
                result += "V"
                result += "I" * (num - 5)
            elif num == 4:
                result += "IV"
            else:
                result += "I" * num
        return result



obj = Solution()

num = 1994
assert "MCMXCIV" == (ret := obj.intToRoman(num)), ret

num = 58
assert "LVIII" == (ret := obj.intToRoman(num)), ret

num = 9
assert "IX" == (ret := obj.intToRoman(num)), ret

num = 3
assert "III" == (ret := obj.intToRoman(num)), ret

num = 4
assert "IV" == (ret := obj.intToRoman(num)), ret

print("Tests passed.")
