from itertools import accumulate

for _ in range(int(input())):
    (n, k) = [int(k) for k in input().split()]

    board = [1 if k == "W" else 0 for k in list(input())]
    prefix = [0, *list(accumulate(board))]

    result = n
    ptr = k + 1

    while ptr <= n + 1:
        painted = prefix[ptr - 1] - prefix[ptr - k - 1]
        result = min(result, painted)
        ptr += 1

    print(result)
