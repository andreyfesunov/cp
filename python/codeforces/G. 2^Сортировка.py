for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    data = list(map(int, input().split()))
    ok = [0] * (n - 1)

    for i in range(0, n - 1):
        ok[i] = data[i] < 2 * data[i + 1]

    total, result = 0, 0

    for i in range(0, k):
        total += ok[i]

    if total == k:
        result += 1

    for i in range(k, n - 1):
        total += ok[i]
        total -= ok[i - k]
        if total == k:
            result += 1 

    print(result)
