class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = map(int, list(str(n)))
        k, l = -1, 0
        for i in range(len(digits) - 1):
            if digits[i] < digits[i + 1]:
                k = i

        if k == -1:
            digits.reverse()
            return -1

        for i in range(k + 1, len(digits)):
            if digits[i] > digits[k]:
                l = i

        digits[k], digits[l] = digits[l], digits[k]
        digits[k + 1:] = digits[:k:-1]
        result = int("".join(map(str, digits)))
        return -1 if result >= 0x7FFFFFFF else result


obj = Solution()

n = 12
assert 21 == (ret := obj.nextGreaterElement(n)), ret

n = 21
assert -1 == (ret := obj.nextGreaterElement(n)), ret

print("Tests passed.")
