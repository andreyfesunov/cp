# https://leetcode.com/problems/maximum-unique-subarray-sum-after-deletion/


class Solution:
    def maxSum(self, nums: list[int]) -> int:
        positive = [num for num in nums if num > 0]

        if len(positive) == 0:
            return max(nums)

        return sum(set(positive))
