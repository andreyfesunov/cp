# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums, target):
        map = {}
        for i, el in enumerate(nums):
            key = target - el
            if key in map:
                return [map[key], i]
            map[el] = i
        return []
