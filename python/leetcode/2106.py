# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps/

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        left = 0
        total = 0
        max_fruits = 0

        for right in range(n):
            total += fruits[right][1]

            while left <= right:
                left_pos = fruits[left][0]
                right_pos = fruits[right][0]
                steps = min(abs(startPos - left_pos), abs(startPos - right_pos)) + (right_pos - left_pos)

                if steps > k:
                    total -= fruits[left][1]
                    left += 1
                else:
                    break

            max_fruits = max(max_fruits, total)

        return max_fruits
        
if __name__ == "__main__":
    print(Solution().maxTotalFruits([[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], 5, 4))