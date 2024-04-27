# Done
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        if len(nums) == 2:
            if nums[0]+1 == nums[1]:
                return ["{}->{}".format(nums[0], nums[1])]
            else:
                return [str(nums[0]), str(nums[1])]
        cur = begin = nums[0]
        ans = []
        print(nums[1:-1])
        for n in nums[1:-1]:
            if n == cur+1:
                cur = n
            elif cur == begin:
                ans.append(str(begin))
                cur = begin = n
            else:
                ans.append("{}->{}".format(begin, cur))
                cur = begin = n
        n = nums[-1]
        if n == cur + 1:
            ans.append("{}->{}".format(begin, n))
        elif cur == begin:
            ans.append(str(begin))
            ans.append(str(n))
        else:
            ans.append("{}->{}".format(begin, cur))
            ans.append(str(n))
        return ans

obj = Solution()

nums = [0, 1, 2, 4, 5, 7]
assert (ret := obj.summaryRanges(nums)) == ["0->2", "4->5", "7"], ret

print("Tests passed.")
