from bisect import bisect_left, bisect_right

def read_int() -> int:
    return int(input())

def read_list() -> list[int]:
    return list(map(int, input().split()))

n = read_int()
a = sorted(read_list())

for _ in range(read_int()):
    (l, r) = read_list()
    print(bisect_right(a, r) - bisect_left(a, l))
