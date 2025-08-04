# https://leetcode.com/problems/fruit-into-baskets/


from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        n = len(fruits)
        left = 0
        count = defaultdict(int)
        max_basket = 0

        for right in range(n):
            count[fruits[right]] += 1

            while len(count) > 2:
                count[fruits[left]] -= 1
                if count[fruits[left]] == 0:
                    del count[fruits[left]]
                left += 1

            max_basket = max(max_basket, right - left + 1)

        return max_basket
