from itertools import accumulate

def read_list() -> list[int]:
    return [int(k) for k in input().split()]

for _ in range(int(input())):
    (n, q) = read_list()
    a = read_list()
    prefix = [0, *list(accumulate(a))]
    for _ in range(q):
        (l, r, k) = read_list()
        result = "YES" if (prefix[-1] + ((r - l + 1) * k - (prefix[r] - prefix[l - 1]))) & 1 == 1 else "NO" 
        print(result)

