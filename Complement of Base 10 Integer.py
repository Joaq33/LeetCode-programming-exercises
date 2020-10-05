class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return 2 ** len("{0:b}".format(N)) - 1 ^ N


obj = Solution()
N = 5
assert (ret := obj.bitwiseComplement(N)) == 2, ret

print("Tests passed.")
