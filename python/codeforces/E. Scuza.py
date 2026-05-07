from itertools import accumulate

def read_list() -> list[int]:
    return [int(k) for k in input().split()]

for _ in range(int(input())):
    (n, q), a, ks = read_list(), read_list(), read_list()
    height = list(accumulate(a))
    m = list(accumulate(a, func=lambda x, y: max(x, y)))
    result = []
    for k in ks:
        l, r = 0, n
        while l < r:
            mid = (l + r) // 2
            if k >= m[mid]:
                l = mid + 1
            else:
                r = mid 

        result.append(height[l - 1] if l != 0 else 0)

    print(" ".join(map(str, result)))
