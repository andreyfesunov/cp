from math import gcd

def solve(a: int, b: int) -> int:
    if a == 1:
        return b * b

    g = gcd(a, b)

    if g == 1:
        return a * b
    if g == a:
        return b * (b // a)

    return b * (a // g)


attempts = int(input())

for _ in range(attempts):
    (a, b) = [int(k) for k in input().split(" ")]

    print(solve(a, b))
