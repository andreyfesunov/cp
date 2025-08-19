# https://leetcode.com/problems/number-of-zero-filled-subarrays/

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n, c, r = len(nums), 0, 0
        
        for i in range(n + 1):
            if i <= n - 1 and nums[i] == 0:
                c += 1
            elif c != 0:
                r += int((1 + c) / 2 * c)
                c = 0

        return r
