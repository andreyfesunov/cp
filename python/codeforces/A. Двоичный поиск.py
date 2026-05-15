from bisect import bisect_right

input()
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for query in b:
    i = bisect_right(a, query) - 1
    result = "YES" if a[i] == query else "NO"
    print(result)
