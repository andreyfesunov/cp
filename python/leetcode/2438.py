# https://leetcode.com/problems/range-product-queries-of-powers/


class Solution:
    def productQueries(self, n: int, queries: list[list[int]]) -> list[int]:
        MOD = 10**9 + 7

        powers = []
        power = 1

        while n > 0:
            if n & 1:
                powers.append(power)
            n >>= 1
            power <<= 1

        result = []
        for left, right in queries:
            product = 1
            for i in range(left, right + 1):
                product = (product * powers[i]) % MOD
            result.append(product)

        return result

