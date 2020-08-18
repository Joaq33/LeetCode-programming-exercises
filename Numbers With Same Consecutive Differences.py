# Done
class Solution:
    def numsSameConsecDiff(self, N: int, K: int):
        if N == 0 or N == 1:
            return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        if K == 0:
            return [int(str(item) * N) for item in range(1, 10)]

        def rec_findnextdigit(previous: int, nleft: int):
            temp = []
            if -1 < previous + K < 10:
                if nleft == 1:
                    temp += [str(previous + K)]
                else:
                    recursed = rec_findnextdigit(previous + K, nleft - 1)
                    for item in recursed:
                        temp += [str(previous + K) + item]
            if -1 < previous - K < 10:
                if nleft == 1:
                    temp += [str(previous - K)]
                else:
                    recursed = rec_findnextdigit(previous - K, nleft - 1)
                    for item in recursed:
                        temp += [str(previous - K) + item]
            return temp

        def memoize(f):
            memo = {}

            def helper(x, y):
                if (x, y) not in memo:
                    memo[(x, y)] = f(x, y)
                return memo[x, y]

            return helper

        rec_findnextdigit = memoize(rec_findnextdigit)

        used = [0]
        ans = []
        for item in range(10 - K):
            if item not in used:
                recursed = rec_findnextdigit(item, N - 1)
                for i in recursed:
                    ans += [int(str(item) + i)]
                used.append(item)
            recursed = rec_findnextdigit(item + K, N - 1)
            for i in recursed:
                ans += [int(str(item + K) + i)]
            used.append(item + K)
        return ans


coso = Solution()
N = 2
K = 1
print(coso.numsSameConsecDiff(N, K))
