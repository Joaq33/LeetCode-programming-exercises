class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        try:
            indx = word.index(ch)
        except:
            return word
        return word[indx::-1] + word[indx + 1:]
