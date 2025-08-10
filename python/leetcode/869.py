# https://leetcode.com/problems/reordered-power-of-2/

from itertools import permutations


class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        arr = permutations(int(i) for i in list(str(n)))

        for perm in arr:
            temp_arr = list(perm)

            if temp_arr[0] == 0:
                continue

            item = int("".join(str(i) for i in temp_arr))

            if item & (item - 1) == 0:
                return True

        return False


if __name__ == "__main__":
    print(Solution().reorderedPowerOf2(46))
