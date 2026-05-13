n = int(input())
a = list(map(int, input().split()))
result = True
for i in range(0, n // 2):
    if a[i] != a[n - i - 1]:
        result = False
print("YES" if result else "NO")
