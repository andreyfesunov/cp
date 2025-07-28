# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/


import functools


class Solution:
    # https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/editorial/?envType=daily-question&envId=2025-07-28#approach-2-memoization

    def __count_subsets(
        self,
        memo: dict[int, dict[int, int]],
        nums: list[int],
        index: int,
        current_or: int,
        target_or: int,
    ) -> int:
        if index in memo and current_or in memo[index]:
            return memo[index][current_or]

        if index == len(nums):
            return 1 if current_or == target_or else 0

        if not index in memo:
            memo[index] = {}

        memo[index][current_or] = self.__count_subsets(
            memo, nums, index + 1, current_or, target_or
        ) + self.__count_subsets(
            memo, nums, index + 1, current_or | nums[index], target_or
        )

        return memo[index][current_or]

    def countMaxOrSubsets(self, nums: list[int]) -> int:
        memo: dict[int, dict[int, int]] = {}
        target_or = functools.reduce(lambda x, y: x | y, nums)

        return self.__count_subsets(memo, nums, 0, 0, target_or)


# TODO: check after dp

if __name__ == "__main__":
    test = [2, 2, 2]

    print(Solution().countMaxOrSubsets(test))
