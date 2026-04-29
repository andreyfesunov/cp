attempts = int(input())

for _ in range(attempts):
    (a, b) = [int(k) for k in input().split(" ")]
    print((b * (a // b + 1) - a) if a % b != 0 else 0)
