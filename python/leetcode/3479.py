# https://leetcode.com/problems/fruits-into-baskets-iii/


class Solution:
    tree: list[int] = []
    available: list[bool] = []
    baskets: list[int] = []

    def numOfUnplacedFruits(self, fruits: list[int], baskets: list[int]) -> int:
        n = len(fruits)

        self.tree = [0] * (4 * n)
        self.available = [True] * n
        self.baskets = baskets

        self.build(1, 0, n - 1)
        unplaced = 0

        for fruit in fruits:
            idx = self.query_leftmost(1, 0, n - 1, fruit)

            if idx != -1:
                self.update(1, 0, n - 1, idx)
            else:
                unplaced += 1

        return unplaced

    def build(self, node: int, start: int, end: int) -> None:
        if start == end:
            self.tree[node] = self.baskets[start] if self.available[start] else 0
        else:
            mid = (start + end) // 2
            self.build(node * 2, start, mid)
            self.build(node * 2 + 1, mid + 1, end)
            self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query_leftmost(self, node: int, start: int, end: int, fruit: int) -> int:
        if start == end:
            if self.available[start] and self.baskets[start] >= fruit:
                return start
            else:
                return -1

        if self.tree[node] < fruit:
            return -1

        mid = (start + end) // 2

        left = self.query_leftmost(2 * node, start, mid, fruit)
        if left != -1:
            return left

        return self.query_leftmost(node * 2 + 1, mid + 1, end, fruit)

    def update(self, node: int, start: int, end: int, idx: int) -> None:
        if start == end:
            self.available[idx] = False
            self.tree[node] = 0  # No longer available
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(2 * node, start, mid, idx)
            else:
                self.update(2 * node + 1, mid + 1, end, idx)

            self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])
