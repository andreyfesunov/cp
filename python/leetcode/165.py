# https://leetcode.com/problems/compare-version-numbers/

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        arr1, arr2 = version1.split("."), version2.split(".")

        max_len = max(len(arr1), len(arr2))

        arr1_padded = [int(i) for i in (arr1 + ['0'] * (max_len - len(arr1)))]
        arr2_padded = [int(i) for i in (arr2 + ['0'] * (max_len - len(arr2)))]

        for i in range(max_len):
            if arr1_padded[i] > arr2_padded[i]:
                return 1
            elif arr1_padded[i] < arr2_padded[i]:
                return -1

        return 0
