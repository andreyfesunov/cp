# https://leetcode.com/problems/fruits-into-baskets-ii/


class Solution:
    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        n = len(fruits)
        c = 0

        for i in range(n):
            fruit = fruits[i]

            basket = next((basket for basket in baskets if basket >= fruit), None)

            if basket is None:
                c += 1
            else:
                baskets.remove(basket)

        return c
