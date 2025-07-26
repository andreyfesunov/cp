# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/


def z(s: str) -> list[int]:
    n = len(s)
    l = 0
    r = 0
    vec = [0 for _ in range(0, n)]

    for i in range(1, n):
        if i <= r:
            vec[i] = min(r - i + 1, vec[i - l])
        while i + vec[i] < n and s[vec[i]] == s[i + vec[i]]:
            vec[i] = vec[i] + 1
        if i + vec[i] - 1 > r:
            r = i + vec[i] - 1
            l = i

    return vec


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        query = f"{needle}#{haystack}"
        vec = z(query)
        l = len(needle)

        for i in range(0, len(query)):
            if l == vec[i]:
                return i - l - 1

        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


if __name__ == "__main__":
    haystack = "truvis"
    needle = "vis"

    print(Solution().strStr(haystack, needle))
