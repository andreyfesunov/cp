from bisect import bisect_right

def read_list() -> list[int]:
    return list(map(int, input().split()))

input()
a = read_list()
for query in read_list():
    print(bisect_right(a, query))
