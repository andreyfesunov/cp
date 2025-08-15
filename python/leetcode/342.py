# https://leetcode.com/problems/power-of-four/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        mask = int("0b01010101010101010101010101010101", 2)
        return n > 0 and mask | n == mask and n & (n - 1) == 0
