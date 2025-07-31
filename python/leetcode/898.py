# https://leetcode.com/problems/bitwise-ors-of-subarrays/

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ans = set()
        prev = set()
        for num in arr:
            curr = {num}
            for val in prev:
                curr.add(val | num)
            ans.update(curr)
            prev = curr
        return len(ans)

if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([1, 11, 6, 11], 4),
        ([1, 2, 4], 6),
    ]

    for arr, expected in test_cases:
        assert sol.subarrayBitwiseORs(arr) == expected