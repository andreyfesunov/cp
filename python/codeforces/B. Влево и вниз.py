from math import gcd

def solve(a: int, b: int, k: int) -> int:
    m = max(a, b)

    if m <= k:
        return 1

    g = gcd(a, b)
    
    if m // g <= k:
        return 1

    return 2

attempts = int(input())

for _ in range(attempts):
    (a, b, k) = [int(t) for t in input().split()]
    print(solve(a, b, k))
