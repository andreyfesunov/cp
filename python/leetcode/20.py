# https://leetcode.com/problems/valid-parentheses/


class Solution:
    open_list = ["(", "[", "{"]
    close_map = {")": "(", "]": "[", "}": "{"}

    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in self.open_list:
                stack.append(char)
                continue

            if len(stack) == 0:
                return False

            output = stack.pop()

            if not self.close_map[char] == output:
                return False

        return len(stack) == 0


if __name__ == "__main__":
    testcase = "()[]{}"

    print(Solution().isValid(testcase))
