from itertools import accumulate

def read_list() -> list[int]:
    return [int(k) for k in input().split()]

(n, k) = read_list()
wins = [1 if t == "W" else 0 for t in list(input())]
wins_prefix = [0, *list(accumulate(wins))]
result = []
for _ in range(k):
    (l, r) = read_list()
    wins_count = wins_prefix[r] - wins_prefix[l - 1]
    loses_count = r - l + 1 - wins_count
    result.append("Y" if wins_count > loses_count else "N")
print("".join(result))
