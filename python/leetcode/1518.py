# https://leetcode.com/problems/water-bottles/description/

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        count = 0
        rest = 0
        
        while numBottles != 0:
            count += numBottles
            rest += numBottles
            numBottles = 0
            
            numBottles += rest // numExchange
            rest -= numBottles * numExchange

        return count
