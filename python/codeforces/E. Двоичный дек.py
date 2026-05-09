from itertools import accumulate
from bisect import bisect_right

def read_list() -> list[int]:
    return [int(k) for k in input().split()]

for _ in range(int(input())):
    (n, s) = read_list()
    prefix = [0, *list(accumulate(read_list()))]
    result = None
    for l in range(n + 1):
        r = bisect_right(prefix, s + prefix[l]) - 1

        if prefix[r] - prefix[l] != s:
            continue

        if result is None:
            result = n - (r - l)
        else:
            result = min(result, n - (r - l))
        
    print(result if result is not None else -1)
