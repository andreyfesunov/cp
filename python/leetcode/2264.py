# https://leetcode.com/problems/largest-3-same-digit-number-in-string/

import re


class Solution:
    def largestGoodInteger(self, num: str) -> str:
        matches = re.findall(r"(\d)\1\1", num)

        if matches:
            return str(max([int(i) for i in matches])) * 3

        return ""
