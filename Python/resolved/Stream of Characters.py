# Done (optimal memory usage)
from collections import defaultdict


class StreamChecker:

    def __init__(self, words):
        self.queried_word = ""
        self.dict_sets = defaultdict(lambda: set())
        for word in words:
            self.dict_sets[word[-1]].add(word)

    def query(self, letter: str) -> bool:
        self.queried_word += letter
        for word in self.dict_sets[letter]:
            if word == self.queried_word[-len(word):]:
                return True
        return False



# Your StreamChecker object will be instantiated and called as such:
words = ["cde", "abc", "f", "ba", "kl","bcd"]
obj = StreamChecker(words)
letters = [["a"], ["b"], ["c"], ["d"], ["e"]]
for [letter] in letters:
    param_1 = obj.query(letter)
