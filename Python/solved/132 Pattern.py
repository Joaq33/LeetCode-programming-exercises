from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack, s3 = [], -float('inf')
        for num in nums[::-1]:
            if num < s3:
                return True
            while stack and stack[-1] < num:
                s3 = stack.pop()
            stack.append(num)
        return False

    def find132pattern2(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        minim, maxim = first, second = nums[0], nums[1]
        for cur in nums[2:]:
            print(minim, cur, maxim)
            if minim < cur < maxim:
                return True
            first = second
            second = cur
            minim = min(minim, first)
            maxim = max(maxim, cur)
        return False


obj = Solution()

# nums = [1, 2, 3, 4, -4, -3, -5, -1]
# assert (ret := obj.find132pattern(nums)) == False, ret
#
# nums = [3, 5, 0, 3, 4]
# assert (ret := obj.find132pattern(nums)) == True, ret
#
# nums = [1, 2, 5, 4]
# assert (ret := obj.find132pattern(nums)) == True, ret
#
# nums = [3, 1, 4, 2]
# assert (ret := obj.find132pattern(nums)) == True, ret
#
# nums = [1, 2, 3, 4]
# assert (ret := obj.find132pattern(nums)) == False, ret

nums = [3, 1, 4, 2]
assert (ret := obj.find132pattern(nums)) == True, ret

print("Tests passed.")
