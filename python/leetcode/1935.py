# https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        for word in text.split(" "):
            count += 1
            for sym in word:
                if sym in brokenLetters:
                    count -= 1
                    break

        return count
