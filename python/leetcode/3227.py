# https://leetcode.com/problems/vowels-game-in-a-string/description/

class Solution:
    def doesAliceWin(self, s: str) -> bool:
        return any(c in "aeiou" for c in s)
