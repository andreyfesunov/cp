from itertools import accumulate

def read() -> int:
    return int(input())

def read_list() -> list[int]:
    return [int(k) for k in input().split()]

n = read()
a = read_list()
m = read()
q = read_list()

prefix = list(accumulate(a))

for worm in q:
    l, r = 0, n - 1
    while l < r:
        m = (l + r) // 2
        if prefix[m] >= worm:
            r = m
        else:
            l = m + 1
    print(l + 1)
