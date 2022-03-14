# Done

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        closing_equivalent = {"(": ")", "[": "]", "{": "}"}
        for letter in s:
            if letter in "([{":
                stack += letter
            else:
                if len(stack) == 0:
                    return False
                ultima = stack.pop()
                if closing_equivalent[ultima] != letter:
                    return False
        return len(stack) == 0


obj = Solution()

s = "){"
assert False == (ret := obj.isValid(s)), ret

s = "()"
assert True == (ret := obj.isValid(s)), ret

s = "([)]"
assert False == (ret := obj.isValid(s)), ret

print("Tests passed.")
