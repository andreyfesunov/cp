MIN_VALUE, MAX_VALUE = 1, 1000000

(n, l, r, x) = [int(k) for k in input().split()]
c = [int(k) for k in input().split()]
result = 0

for mask in range(1 << n):
    mask_min, mask_max, sum = MAX_VALUE, MIN_VALUE, 0

    for i in range(n):
        if mask & (1 << i):
            sum += c[i]
            mask_min = min(mask_min, c[i])
            mask_max = max(mask_max, c[i])

    if mask_max - mask_min >= x and l <= sum <= r:
        result += 1

print(result)
