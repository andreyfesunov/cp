from itertools import accumulate

def read_list() -> list[int]:
    return [int(k) for k in input().split()]

(n, k) = read_list()
hours = read_list()
hours_prefix = [0, *list(accumulate(hours))]
weeks_prefix = []

for i in range(0, n - k + 1):
    weeks_prefix.append((hours_prefix[i + k] - hours_prefix[i]) / (n - k + 1))

print(sum(weeks_prefix))
