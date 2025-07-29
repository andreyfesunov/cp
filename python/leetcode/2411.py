# https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/

import functools


class Solution:
    def smallestSubarrays(self, nums: list[int]) -> list[int]:
        n = len(nums)
        last = [0] * 32
        res = [1] * n

        for i in reversed(range(n)):
            num = nums[i]
            
            for bit in range(32):
                if num & (1 << bit):
                    last[bit] = i
                    
            data = [last[bit] - i + 1 for bit in range(32) if last[bit]]

            res[i] = max(data) if data else 1

        return res


if __name__ == "__main__":
    print(Solution().smallestSubarrays([1,0,2,1,3]))
