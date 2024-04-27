from icecream import ic
from collections import deque


class Solution:

    # def longestIdealString(self, s: str, k: int) -> int:
    #     """MLE """
    #     # s = [ord(i) for i in s]
    #     ans = 0
    #
    #     queue = deque()
    #     memo = {}
    #
    #     queue.append((None, 0, -1))
    #     while queue:
    #         lastval, cur, pos = queue.popleft()
    #         pos += 1
    #         item = ord(s[pos])
    #         if lastval is None or -k <= lastval - item <= k:
    #             if len(s) == pos + 1:
    #                 ans = max(cur + 1, ans)
    #                 continue
    #             if (item, cur + 1, pos) not in memo:
    #                 memo[(item, cur + 1, pos)] = True
    #                 # memo.add((item, cur + 1, pos))
    #                 queue.append((item, cur + 1, pos))
    #         if len(s) == pos + 1:
    #             ans = max(cur, ans)
    #             continue
    #         if (lastval, cur, pos) not in memo:
    #             # memo.add((lastval, cur, pos))
    #             memo[(lastval, cur, pos)] = True
    #             queue.append((lastval, cur, pos))
    #
    #     return ans
    #
    def longestIdealString(self, s: str, k: int) -> int:
        """
        correct
        it runs in O(26n)
        it iterates the entire string once, storing the max value for each letter if it is in range inside a helper
        array
        :param s:
        :param k:
        :return:
        """
        array = [0 for i in range(27)]
        for i in s:
            mv = 0
            for j in range(-k, k + 1):
                if 0 <= j + ord(i) - ord('a') < 27:
                    mv = max(mv, array[j + ord(i) - ord('a')])
            array[ord(i) - ord('a')] = mv + 1

        return max(array)

    def longestIdealString(self, s: str, k: int) -> int:
        """best answer, optimized version of previous aproach
        it uses the max function to skip the manual range iteration
        I optimized the memory by transposing by k instead of creating l with a lenght of 128
        :param s:
        :param k:
        :return:
        """
        l = [0] * (27 + k)
        for c in s:
            i = ord(c) - 97 + k
            l[i] = max(l[i - k: i + k + 1]) + 1
        return max(l)


import unittest


class Test(unittest.TestCase):
    def test_one(self):
        s = "acfgbd"
        k = 2
        expected = 4
        self.assertEqual(expected, Solution().longestIdealString(s, k))

    def test_two(self):
        s = "eduktdb"
        k = 15
        expected = 5
        self.assertEqual(expected, Solution().longestIdealString(s, k))

    def test_three(self):
        s = "bacd"
        k = 1
        expected = 3
        self.assertEqual(expected, Solution().longestIdealString(s, k))

    def test_fourth(self):
        # s = "dyyonfvzsretqxucmavxegvlnnjubqnwrhwikmnnrpzdovjxqdsatwzpdjdsneyqvtvorlwbkb"
        s = "dyyonfvzsretqxucmavxegvlnnjubqnwrhwik"
        k = 7
        expected = 19
        self.assertEqual(expected, Solution().longestIdealString(s, k))

    def test_fifth(self):
        s = "dyyonfvzsretqxucmavxegvlnnjubqnwrhwikmnnrpzdovjxqdsatwzpdjdsneyqvtvorlwbkb"
        # s = "dyyonfvzsretqxucmavxegvlnnjubqnwrhwik"
        k = 7
        expected = 42
        self.assertEqual(expected, Solution().longestIdealString(s, k))

    def test_sixth(self):
        s = "ksppfqkvtbivirhmgmkbeuyyqowldqnbbgeadpektsixhssubrcsrsoqvngtqfxiknxbogoemmcjohvioyaskmdvshkioqlelwqxjrgidhzvnfsjdbyhccgewcajsjtscjkzbsqpcrtyyroajstexqgxssimkctxddiicrycrmfxkvgnpccpiawmzwefjrnatjbalminnlyjvwmerfiglqysqzsdoktbayhtqsahhzpdzxhrvypyqmsjjdcylyzmelnjhqmiqqvtdvqeecdtpabataedwtommhjlwzdeilmbqsdhsumqavebljocamuweuxoytmzraaiusmesvswmcoqbncsghrihjojrugzcazpgdgjtovhbdytyzntywlfchfyahdsgdovgrdbvdujwdsojqzluxpxcukhsvsbcxeudaezeukfoktamuuieldqqdgbfwtxrfhrsmikkfybwqaaazgruruzvqkzcljufwsqremjoswcgjjctkrwsbfgvarznfhmmdnmdemasuwoshzsprkyawqreyzcjhpuihfpeizjkplyxxqttyeyopvbpzhwllkbgyeykkunogyyevsiglznmyixuimkrbffiiledmdcazrhvdwqjirvyxdtdlovuocobzexdsdxslkrzreaevwywaryeafydjlpccklipyhfwgafihcsimsquckxsnnftaviuumngctfmbrtuxqjwlkwydiislrntqrulmecenrrlnovrwfzxqaagnszvoogwfpwuhkojsxvjambsxszfnwjxckmecmpqaxbwdrqekanoxvoguxfocnxkgoptqxadtpglnlrllaynknfdzbsg"
        # s = "dyyonfvzsretqxucmavxegvlnnjubqnwrhwik"
        k = 21
        expected = 833
        self.assertEqual(expected, Solution().longestIdealString(s, k))
