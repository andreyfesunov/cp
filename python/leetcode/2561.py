from collections import Counter
from typing import List

class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        count1 = Counter(basket1)
        count2 = Counter(basket2)

        total = Counter(basket1 + basket2)
        for v in total.values():
            if v % 2 != 0:
                return -1

        diff1 = []
        diff2 = []
        for fruit in total:
            c1 = count1[fruit]
            c2 = count2[fruit]
            if c1 > c2:
                diff1.extend([fruit] * ((c1 - c2) // 2))
            elif c2 > c1:
                diff2.extend([fruit] * ((c2 - c1) // 2))

        if not diff1 and not diff2:
            return 0

        diff1.sort()
        diff2.sort(reverse=True)
        min_elem = min(basket1 + basket2)
        swaps = len(diff1)
        cost = 0

        for i in range(swaps):
            cost += min(diff1[i], diff2[i], 2 * min_elem)

        return cost

if __name__ == "__main__":
    solution = Solution()

    test_cases = [
        ([4,2,2,2], [1,4,1,2], 1),
        ([2,3,4,1], [3,2,5,1], -1),
        ([1,1,1,1,1], [1,1,1,1,1], 0),
        ([1,1,1,1,1], [1,1,1,1,1], 0),
        ([4,4,4,4,3], [5,5,5,5,3], 8)
    ]

    for basket1, basket2, expected in test_cases:
        assert solution.minCost(basket1, basket2) == expected