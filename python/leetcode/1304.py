# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/desription/


class Solution:
    def sumZero(self, n: int) -> list[int]:
        return [
            i - n // 2 + (1 if n % 2 == 0 and i - n // 2 >= 0 else 0) for i in range(n)
        ]
