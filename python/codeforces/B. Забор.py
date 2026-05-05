from itertools import accumulate

(n, k) = [int(k) for k in input().split()]
data = [int(k) for k in input().split()]
prefix = [0, *list(accumulate(data))]

result = sum(data)
result_index = 0

for i in range(k, n + 1):
    if prefix[i] - prefix[i - k] <= result:
        result = prefix[i] - prefix[i - k]
        result_index = i - k + 1

print(result_index)
