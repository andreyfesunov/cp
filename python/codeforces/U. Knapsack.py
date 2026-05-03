# https://codeforces.com/group/MWSDmqGsZm/contest/223339/problem/U

(n, max_weight) = [int(k) for k in input().split()]

items = []
for _ in range(n):
    (w, v) = [int(k) for k in input().split()]
    items.append((w, v))

result = 0

for mask in range(1 << n):
    attempt_weight = 0
    attempt_total = 0

    for i in range(n):
        if mask & (1 << i):
            (w, v) = items[i]
            attempt_weight += w
            attempt_total += v

    if attempt_weight <= max_weight:
        result = max(result, attempt_total)

print(result)
