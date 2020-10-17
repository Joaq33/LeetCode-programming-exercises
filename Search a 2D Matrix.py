from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or matrix == [[]]:
            return False

        def search(nums: List[int]) -> int:
            left, right = 1, len(nums) - 1
            while left <= right:
                pivot = (left + right) // 2
                print(nums[pivot])
                if target == nums[pivot]:
                    return True
                if target > nums[pivot]:
                    left = pivot + 1
                else:
                    right = pivot - 1
            return False

        if len(matrix) == 1:
            if matrix[0][0] == target:
                return True
            return search(matrix[0])
        left, right = 0, len(matrix) - 1
        while right != left:
            pivot = (left + right) // 2 + 1
            if matrix[pivot][0] == target:
                return True
            elif matrix[pivot][0] < target:
                left = pivot
            else:
                right = pivot - 1
        if matrix[left][0] == target:
            return True
        return search(matrix[left])


obj = Solution()

matrix = [[1], [3]]
target = 1
assert True == (ret := obj.searchMatrix(matrix, target)), ret

matrix = [[1, 3]]
target = 1
assert True == (ret := obj.searchMatrix(matrix, target)), ret

matrix = [[1]]
target = 1
assert True == (ret := obj.searchMatrix(matrix, target)), ret

matrix = [[1], [3]]
target = 3
assert True == (ret := obj.searchMatrix(matrix, target)), ret

matrix = [[1]]
target = 0
assert False == (ret := obj.searchMatrix(matrix, target)), ret

matrix = [[]]
target = 1
assert False == (ret := obj.searchMatrix(matrix, target)), ret

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]
target = 3
assert True == (ret := obj.searchMatrix(matrix, target)), ret

print("Tests passed.")
