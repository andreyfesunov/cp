# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_idx: dict[str, int] = {}
        left = max_len = 0

        for right, char in enumerate(s):
            prev_idx = char_idx[char] if char in char_idx else None

            if prev_idx is not None and prev_idx >= left:
                left = prev_idx + 1

            char_idx[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    test = "abba"

    print(Solution().lengthOfLongestSubstring(test))
