from itertools import accumulate

def read_list() -> list[int]:
    return [int(k) for k in input().split()]

for _ in range(int(input())):
    (n, k) = read_list()
    prefix = [0, *list(accumulate(sorted(read_list())))]
    result = 0
    for i in range(k + 1):
        result = max(result, prefix[n - (k - i)] - prefix[2 * i])
    print(result)
