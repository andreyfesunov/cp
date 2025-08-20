# https://leetcode.com/problems/count-square-submatrices-with-all-ones/

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        k = len(matrix[0])

        dp = [[0] * k for _ in range(n)]
        s = 0

        for i in range(n):
            for j in range(k):
                r = 0

                if matrix[i][j] == 0:
                    continue

                if i != 0 and j != 0:
                    r = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

                r += 1

                dp[i][j] = r
                s += r

        return s
        
