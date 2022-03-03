# Done


class Solution:
    def decodeString(self, s: str) -> str:
        def rec(cur, times):
            substring = ""
            nexttimes = ""
            while cur < len(s):
                if s[cur].islower():
                    substring += s[cur]
                elif s[cur].isnumeric():
                    nexttimes += s[cur]
                elif s[cur] == "[":
                    cur += 1
                    temp, cur = rec(cur, int(nexttimes))
                    substring += temp
                    nexttimes = ""
                    continue
                else:
                    cur += 1
                    return substring * times, cur
                cur += 1
            return substring * times
        return rec(0, 1)


obj = Solution()

s = "abc3[cd]xyz"
assert "abccdcdcdxyz" == (ret := obj.decodeString(s)), ret

s = "2[abc]3[cd]ef"
assert "abcabccdcdcdef" == (ret := obj.decodeString(s)), ret

s = "3[a2[c]]"
assert "accaccacc" == (ret := obj.decodeString(s)), ret

s = "3[a]2[bc]"
assert "aaabcbc" == (ret := obj.decodeString(s)), ret

print("Tests passed.")
