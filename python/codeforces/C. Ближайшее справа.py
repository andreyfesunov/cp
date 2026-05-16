from bisect import bisect_left

def read_list() -> list[int]:
    return list(map(int, input().split()))

input()
a = read_list()
for query in read_list():
    print(bisect_left(a, query) + 1)
