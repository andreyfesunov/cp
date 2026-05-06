from itertools import accumulate

def read_list() -> list[int]:
    return [int(k) for k in input().split()]

n = int(input())
v = read_list()
u = sorted(v)

prefix_v = [0, *list(accumulate(v))]
prefix_u = [0, *list(accumulate(u))]

for _ in range(int(input())):
    (type, l, r) = read_list()
    if type == 1:
        print(prefix_v[r] - prefix_v[l - 1])
    else:
        print(prefix_u[r] - prefix_u[l - 1])
