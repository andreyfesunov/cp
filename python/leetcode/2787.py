# https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/


class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        
        powers = []
        base = 1
        while base**x <= n:
            powers.append(base**x)
            base += 1
        
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for power in powers:
            for sum_val in range(n, power - 1, -1):
                dp[sum_val] = (dp[sum_val] + dp[sum_val - power]) % MOD
        
        return dp[n]


if __name__ == "__main__":
    print(Solution().numberOfWays(10, 2))
