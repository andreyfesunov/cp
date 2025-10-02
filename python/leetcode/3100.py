# https://leetcode.com/problems/water-bottles-ii/description/

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        count = 0
        rest = 0
        
        while numBottles != 0:
            count += numBottles
            rest += numBottles
            numBottles = 0
            
            numBottles += 1 if rest - numExchange >= 0 else 0
            rest = max(0, rest - numExchange)
            numExchange += 1

        return count
