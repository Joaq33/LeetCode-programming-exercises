# Done
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) == 1:
            return False
        notinb = ""
        notina = ""
        first_change = False
        s_letters = set()
        repeated = False
        for index, (a, b) in enumerate(zip(A, B)):
            if a != b:
                if not first_change:
                    notina = b
                    notinb = a
                    first_change = True
                else:
                    if notina == a and notinb == b:
                        return A[index+1:] == B[index+1:]
                    else:
                        return False
            elif not repeated:
                if a not in s_letters:
                    s_letters.add(a)
                else:
                    repeated = True
        if first_change:
            return False
        return repeated


obj = Solution()

A = "abac"
B = "abad"
assert (ret := obj.buddyStrings(A, B)) == False, ret

A = "aa"
B = "bb"
assert (ret := obj.buddyStrings(A, B)) == False, ret

A = "ab"
B = "ba"
assert (ret := obj.buddyStrings(A, B)) == True, ret

A = "ab"
B = "ab"
assert (ret := obj.buddyStrings(A, B)) == False, ret

A = "abcd"
B = "badc"
assert (ret := obj.buddyStrings(A, B)) == False, ret
