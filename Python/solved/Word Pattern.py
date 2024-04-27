# Done

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        str = str.split()
        if len(pattern) != len(str):
            return False
        taken = set()
        dict_vals = dict()
        for index, letter in enumerate(pattern):
            if letter in dict_vals:
                if dict_vals[letter] != str[index]:
                    return False
            elif str[index] not in taken:
                dict_vals[letter] = str[index]
                taken.add(str[index])
            else:
                return False
        return True


obj = Solution()
pattern = "aaa"
str = "aa aa aa aa"
print(obj.wordPattern(pattern, str))
