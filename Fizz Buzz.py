# Done
from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for number in range(1,n+1):
            phrase = ""
            if number%3==0:
                phrase += "Fizz"
            if number%5 == 0:
                phrase += "Buzz"
            if phrase == "":
                ans.append(str(number))
            else:
                ans.append(phrase)
        return ans

obj = Solution()
print(obj.fizzBuzz(6))