# [Divide Array in Sets of K Consecutive Numbers](https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/)

Given an array of integers `nums` and a positive integer `k`, check
whether it is possible to divide this array into sets of `k` consecutive
numbers.

Return `true` *if it is possible*. Otherwise, return `false`.

 

**Example 1:**

    Input: nums = [1,2,3,3,4,4,5,6], k = 4
    Output: true
    Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].

**Example 2:**

    Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
    Output: true
    Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].

**Example 3:**

    Input: nums = [1,2,3,4], k = 3
    Output: false
    Explanation: Each array should be divided in subarrays of size 3.

 

**Constraints:**

- `1 <= k <= nums.length <= 10`^`5`^
- `1 <= nums[i] <= 10`^`9`^

 

**Note:** This question is the same
as 846: [https://leetcode.com/problems/hand-of-straights/](https://leetcode.com/problems/hand-of-straights/){target="_blank"}\

Hint 1

If the smallest number in the possible-to-split array is V, then numbers
V+1, V+2, \... V+k-1 must contain there as well.

\

Hint 2

You can iteratively find k sets and remove them from array until it
becomes empty.

\

Hint 3

Failure to do so would mean that array is unsplittable.
