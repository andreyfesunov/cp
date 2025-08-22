# https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_i, min_j, max_i, max_j = 999, 999, 0, 0

        n, m = len(grid), len(grid[0])

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    min_j = min(min_j, j)
                    max_i = max(max_i, i)
                    max_j = max(max_j, j)
        
        return (max_i - min_i + 1) * (max_j - min_j + 1)
