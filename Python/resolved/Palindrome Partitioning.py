# Done
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]: # copied
        if not s:
            return []

        dp = {0: [[]], 1: [[s[0]]]}

        for i in range(1, len(s)):
            dp[i + 1] = []

            for j in range(0, i + 1):
                if self.is_palindrome(s[j:i + 1]):
                    for prev in dp[j]:
                        dp[i + 1].append(prev + [s[j:i + 1]])

        return dp[len(s)]

    def is_palindrome(self, s):
        return s == s[::-1]
    def partition2(self, s: str) -> List[List[str]]: # incomplete
        if len(s) == 1:
            return [[s]]
        def is_palindrome(substring):
            if len(substring) == 1:
                return True
            left, right = 0, len(substring) - 1
            while right - left > 0:
                if substring[left] != substring[right]:
                    return False
                right -= 1
                left += 1
            return True

        def dfs(substring):
            val = []
            if is_palindrome(substring):
                val.append([substring])

            for i in range(1, len(substring)):
                # print(substring[:i])
                temp1 = dfs(substring[:i])
                # print(substring[i:])
                temp2 = dfs(substring[i:])
                for item in temp1:
                    for item2 in temp2:
                        temp3 = item + item2
                        if len(s) == len(temp3):
                            continue
                        val.append(item + item2)
                        # if temp3 not in val:
                        #     val.append(item + item2)

            return val

        # print(is_palindrome("ab"))
        return [[st for st in s]] + dfs(s)


obj = Solution()

s = "a"
assert [["a"]] == (
    ret := obj.partition(s)), ret

s = "aabba"
assert [["a", "a", "b", "b", "a"], ["a", "a", "bb", "a"], ["a", "abba"], ["aa", "b", "b", "a"], ["aa", "bb", "a"]] == (
    ret := obj.partition(s)), ret

s = "aab"
assert [["a", "a", "b"], ["aa", "b"]] == (ret := obj.partition(s)), ret

s = "aaba"
assert [['a', 'a', 'b', 'a'], ['a', 'aba'], ['aa', 'b', 'a']] == (ret := obj.partition(s)), ret

print("Tests passed.")
