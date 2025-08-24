# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        longest, zeros, start, n = 0, 0, 0, len(nums)

        for i in range(n):
            zeros += 1 if nums[i] == 0 else 0

            while zeros > 1:
                zeros -= 1 if nums[start] == 0 else 0
                start += 1

            longest = max(longest, i - start)
