from typing import List


# from icecream import ic


# ic.configureOutput(includeContext=True)
# ic.prefix =''

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        ans = []
        v = 1
        for _ in range(n):
            # print(v)
            ans.append(v)
            if v * 10 <= n:
                v *= 10
            else:
                while v % 10 == 9 or v + 1 > n:
                    v //= 10
                v += 1
        return ans
# {


# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#         strn = str(n)
#
#         def df_lexical(prefix: str, cur: int, min_iterator: int, max_iterator: int) -> List[int]:
#             if cur == 0:
#                 return None
#             ret = []
#
#             def append_and_print(val):
#                 print(val)
#                 ret.append(val)
#
#             for i in range(min_iterator, max_iterator):
#                 append_and_print(prefix + i)
#                 tmp = df_lexical(prefix+str(i), cur // 10, 0, 10)
#                 if tmp:
#                     ret.append(tmp)
#
#             return ret
#
#         ans = df_lexical('', n, 1, int(strn[0]))
#         return ans

# class Solution:
#     def lexicalOrder(self, n: int) -> List[int]:
#         # l = len(str(n))  # remove this later for the o(1) requirement
#
#         def dp_lexical(cur, before, pad):
#             print(pad, "=" * 60)
#             print(pad, "cur:", cur, "before:", before)
#             # print('entering:', cur, before)
#             # ic()
#             # if cur is None:
#             #     return None
#             cans = []
#             leading_digit = int(str(cur)[0])
#             print(pad, "leading_digit:", leading_digit)
#
#             for i in range(leading_digit + 1):
#                 print(pad, "i:", i, "cur:", cur)
#                 tmp_val = int(before + str(i))
#                 print(pad, "tmp_val:", tmp_val)
#                 if tmp_val == 0 and before == '':
#                     continue
#                 print(pad, "apending:", i)
#                 cans.append(tmp_val)
#
#                 if cur > 9:
#                     next_cur = int(str(cur)[1:])
#                     # ic("next_cur", next_cur)
#                     print(pad, "next_cur:", next_cur, "before+str(i):", before + str(i))
#                     sub = dp_lexical(next_cur, before + str(i), pad + "    ")
#                     # if sub:
#                     cans += sub
#
#             if before == '':
#                 next_cur = int(str(cur)[1:])
#                 sub = dp_lexical(next_cur, before, pad + "    ")
#                 # if sub:
#                 cans += sub
#             print("returning:", cans)
#             return cans
#
#         # ans = []
#         ans = dp_lexical(n, before="", pad="")
#         return ans
#         # for len_it in range(len(n)):
