# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/

import math

class Solution:
    def areaOfMaxDiagonal(self, d: List[List[int]]) -> int:
        max_diag, max_area, n = 0, 0, len(d)

        for i in range(n):
            diag = d[i][0] ** 2 + d[i][1] ** 2

            if diag > max_diag:
                max_diag = diag
                max_area = d[i][0] * d[i][1]
            elif diag == max_diag:
                max_area = max(max_area, d[i][0] * d[i][1])

        return max_area
