# Done
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        optimal memory usage
        Might have better runtime storing combinations in a hash
        :param beginWord: 
        :param endWord: 
        :param wordList: 
        :return: 
        """
        def is_derived(cur, target):
            first_case = False
            for index, letter in enumerate(cur):
                if target[index] != letter:
                    if first_case:
                        return False
                    first_case = True
            return True
        queue = [beginWord]
        level = 1
        while queue:
            next_queue = []
            for word in queue:
                if word == endWord:
                    return level
                cur_i = 0
                while cur_i < len(wordList):
                    if is_derived(word, wordList[cur_i]):
                        next_queue.append(wordList[cur_i])
                        wordList.pop(cur_i)
                    else:
                        cur_i += 1
            queue = next_queue
            level += 1
        return 0


obj = Solution()

beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
assert 5 == (ret := obj.ladderLength(beginWord, endWord, wordList)), ret

print("Tests passed.")
