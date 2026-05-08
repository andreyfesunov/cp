from itertools import accumulate

prefix = list(accumulate(range(1, 2 * (10 ** 5) + 1), func=lambda x, y: x + sum(map(int, list(str(y))))))

for _ in range(int(input())):
    n = int(input())
    result = prefix[n - 1]
    print(result)
