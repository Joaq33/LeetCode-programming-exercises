class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        arr = [None] * (N + 1)
        arr[0], arr[1] = 0, 1
        for i in range(2, N + 1):
            arr[i] = arr[i - 1] + arr[i - 2]
        return arr[-1]

    def fib2(self, N: int) -> int:  # copied
        a = 0
        b = 1
        if (N == 0):
            return a
        if (N == 1):
            return b
        N -= 2
        while (N >= 0):
            a, b = b, a + b
            N -= 1
        return b


obj = Solution()

N = 7
assert 13 == obj.fib(N)

print("Tests passed.")
