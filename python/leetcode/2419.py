# https://leetcode.com/problems/longest-subarray-with-maximum-bitwise-and/


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        l, max_num, max_len = 0, 0, 0

        for num in nums:
            if num > max_num:
                l = 1
                max_num = num
                max_len = l
            elif num == max_num:
                l += 1
                max_len = max(l, max_len)
            else:
                l = 0

        return max_len


if __name__ == "__main__":
    print(
        Solution().longestSubarray(
            [96317, 96317, 96317, 96317, 96317, 96317, 96317, 96317, 96317, 279979]
        )
    )
