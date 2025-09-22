# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        data, m, c = {}, 0, 0
        for num in nums:
            if not num in data:
                data[num] = 0
            
            data[num] += 1
            if data[num] > m:
                m = data[num]
                c = data[num]
            elif data[num] == m:
                c += data[num]
        
        return c
