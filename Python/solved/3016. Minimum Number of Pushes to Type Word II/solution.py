from collections import Counter


class Solution:
    def minimumPushes(self, word: str) -> int:
        c = Counter(word)
        most_common = c.most_common()
        weighted_letters = [(i // 8 + 1) * x for i, (z, x) in enumerate(most_common)]
        # print("weighted_letters", weighted_letters)
        return sum(weighted_letters)



print("hola")