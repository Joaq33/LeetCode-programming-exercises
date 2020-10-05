class Solution:
    def bitwiseComplement(self, N: int) -> int:
        if N == 0:
            return 1

        if N == 1:
            return 0

        up = 2
        while up <= N:
            up = up << 1

        return up - 1 - N

    def bitwiseComplement2(self, N: int) -> int:
        return 2 ** len("{0:b}".format(N)) - 1 ^ N


obj = Solution()
N = 5
assert (ret := obj.bitwiseComplement(N)) == 2, ret

print("Tests passed.")
