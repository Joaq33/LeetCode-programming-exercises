class Solution:
    def hammingWeight(self, n: int) -> int:
        """
        easy answer without getting into binary operators
        """
        ans = 0
        for c in bin(n)[2:]:
            if c == '1':
                ans += 1
        return ans
