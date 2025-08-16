# https://leetcode.com/problems/maximum-69-number/


class Solution:
    def maximum69Number(self, num: int) -> int:
        s = str(num)
        i = s.find("6")

        if i == -1:
            return int(s)

        return int(s[:i] + "9" + s[i + 1 :])


if __name__ == "__main__":
    print(Solution().maximum69Number(9999))
