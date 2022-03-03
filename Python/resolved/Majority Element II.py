# Done
from collections import defaultdict
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        limit = int(len(nums) / 3)
        count = defaultdict(int)
        ans = set()
        for n in nums:
            count[n] += 1
            if count[n] > limit:
                ans.add(n)
        return list(ans)


if __name__ == '__main__':
    obj = Solution()

    nums = [3, 2, 3]
    assert (ret := obj.majorityElement2(nums)) == [3], ret

    print("Tests Passed")
