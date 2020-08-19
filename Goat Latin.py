# Done
class Solution:
    def toGoatLatin(self, S: str) -> str:
        if S == "":
            return ""
        ans = ""
        wordcounter = 1
        firstswap = True
        firstletter = ""
        for letter in S:
            if letter == " ":
                firstswap = True
                ans += firstletter + "ma" + "a" * wordcounter + " "
                wordcounter += 1
                firstletter = ""
            elif firstswap:
                firstswap = False
                vowel = bool(letter in "aeiouAEIOU")
                firstletter = letter * (not vowel)
                ans += letter * vowel
            else:
                ans += letter
        if S[-1] != " ":
            ans += firstletter + "ma" + "a" * wordcounter
        return ans


coso = Solution()
S = "The quick brown fox jumped over the lazy dog"
S = "Each word consists of lowercase and uppercase letters only"
print(coso.toGoatLatin(S))
