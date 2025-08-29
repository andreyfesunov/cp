# https://leetcode.com/problems/alice-and-bob-playing-flower-game/


class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (n - n // 2) * (m // 2) + (n // 2) * (m - m // 2)
