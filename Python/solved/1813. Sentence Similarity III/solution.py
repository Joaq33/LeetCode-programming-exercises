from icecream import ic


class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        """
        time complexity: O(n)
        space complexity: O(1)
        :param sentence1: str - The first sentence to compare.
        :param sentence2: str - The second sentence to compare.
        :return: bool - True if the sentences are similar, False otherwise.
        :rtype: bool
        """
        s1 = sentence1.split(" ")
        s2 = sentence2.split(" ")

        if len(s1) < len(s2):
            s1, s2 = s2, s1

        for i in range(len(s2)):
            ic(s1[i], s2[i])
            if s1[i] != s2[i]:
                # ic(len(s2), i, s1[i:], s1[-len(s2)+i:], s2[i:])
                if s1[-len(s2) + i:] == s2[i:]:
                    return True
                return False
        return True
