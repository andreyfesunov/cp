# https://leetcode.com/problems/new-21-game/


class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k + maxPts - 1:
            return 1.0

        dp = [0.0] * (n + 1)
        dp[0] = 1.0

        window_sum = 1.0
        answer = 0.0

        for i in range(1, n + 1):
            dp[i] = window_sum / maxPts

            if i < k:
                window_sum += dp[i]
            else:
                answer += dp[i]

            drop_index = i - maxPts
            if drop_index >= 0 and drop_index < k:
                window_sum -= dp[drop_index]

        return answer
