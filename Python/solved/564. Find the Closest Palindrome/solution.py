class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if (n == "1" + "0" * (len(n) - 1)) or len(n) == 1:
            return str(int(n) - 1)
        if n == "9" * len(n):
            return str(int(n) + 2)

        if n == "1" + "0" * (len(n) - 2) + "1":
            return "9" * (len(n) - 1)

        first_half = n[:len(n) // 2 + len(n) % 2]

        last_half = n[len(n) // 2 + len(n) % 2:]

        first_half_ref = first_half[-1 - len(n) % 2::-1]

        if int(first_half_ref) == int(last_half):  # palindromes
            if len(first_half) > len(first_half_ref):  # 123, 12 (largo impar)
                if first_half[-1] == "0" and first_half[-2] == "1":
                    temp = str(int(first_half) + 1)
                    return temp + temp[-2::-1]
                temp = str(int(first_half) - 1)
                return temp + temp[-2::-1]

            temp = str(int(first_half) - 1)
            return temp + temp[::-1]

        if int(first_half_ref) > int(last_half):  # higher

            first_part = n[:len(n) // 2 + len(n) % 2]
            last_part = n[:len(n) // 2][::-1]

            ans1 = first_part + last_part

            # addition approach
            first_part = str(int(n[:len(n) // 2 + len(n) % 2]) - 1)
            last_part = first_part[:len(first_part) - len(n) % 2][::-1]

            ans2 = first_part + last_part
            if (int(ans1) - int(n)) < -(int(ans2) - int(n)):
                return ans1
            return ans2

        if int(first_half_ref) < int(last_half):  # lower
            first_part = n[:len(n) // 2 + len(n) % 2]
            last_part = n[:len(n) // 2][::-1]

            ans1 = first_part + last_part

            first_part = str(int(n[:len(n) // 2 + len(n) % 2]) + 1)
            last_part = first_part[:len(first_part) - len(n) % 2][::-1]

            ans2 = first_part + last_part
            if -(int(ans1) - int(n)) > int(ans2) - int(n):
                return ans2
            return ans1


    #
    # def nearestPalindromic(self, n: str) -> str:
    #     """
    #     brute approach time exceeded
    #     :param n:
    #     :return:
    #     """
    #
    #     def is_palindrome(_n: str) -> bool:
    #         if _n == _n[::-1]:
    #             return True
    #         return False
    #
    #     diff = 1
    #     while True:
    #         temp_n = str(int(n)-diff)
    #         if is_palindrome(temp_n):
    #             return temp_n
    #
    #         temp_n = str(int(n)+diff)
    #         if is_palindrome(temp_n):
    #             return temp_n
    #
    #         diff += 1
