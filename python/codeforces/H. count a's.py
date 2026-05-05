# https://codeforces.com/group/c3FDl9EUi9

from itertools import accumulate

data = input()
prefix = list(accumulate(list(data), func=lambda x, y: x + (1 if y == "a" else 0), initial=0))

for _ in range(int(input())):
    (l, r) = [int(k) for k in input().split()]
    print(prefix[r] - prefix[l - 1])
