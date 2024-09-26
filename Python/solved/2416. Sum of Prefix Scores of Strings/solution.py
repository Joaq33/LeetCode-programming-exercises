from typing import List
from collections import defaultdict


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        """
        Time: O(n)
        Space: O(n)
        """

        word_count = len(words)
        sorted_indices = sorted(range(word_count), key=lambda i: words[i])
        print("sorted",sorted_indices)
        ans = []
        dict_helper = defaultdict(int)
        for word in words:
            for prefix_limit in range(1, len(word) + 1):
                dict_helper[word[:prefix_limit]] += 1
        for word in words:
            tmp_ans = 0
            for prefix_limit in range(1, len(word) + 1):
                tmp_ans += dict_helper[word[:prefix_limit]]
            ans.append(tmp_ans)
        return ans
