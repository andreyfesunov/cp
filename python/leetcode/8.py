import re


class Solution:
    def myAtoi(self, s: str) -> int:
        digit = re.search(r"^\s*([+-]?\d+)", s)
        if not digit:
            return 0

        num = int(digit.group(1))

        if num < -(2**31):
            return -(2**31)
        elif num > 2**31 - 1:
            return 2**31 - 1

        return num
