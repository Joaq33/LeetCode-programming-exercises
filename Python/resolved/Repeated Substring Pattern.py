# Done
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        print(len(s))
        for index in (index for index in range(1, len(s)) if len(s) % index == 0):
            if s[:index] * int(len(s)/index) == s:
                return True
        return False


obj = Solution()
s = "abcabcabcabc"

print(obj.repeatedSubstringPattern(s))
