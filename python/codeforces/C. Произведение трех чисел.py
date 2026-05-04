from itertools import permutations

def find_divisors(x: int) -> list[int]:
    divs = []
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            divs.append(i)
            if i * i != x:
                divs.append(x // i)
    return divs

def find_three_divisors(x: int) -> list[int]:
    divs = find_divisors(x)
    for (a, b, c) in permutations(divs, 3):
        if a * b * c == x:
            return [a, b, c]
    return []

for _ in range(int(input())):
    x = int(input())
    result = find_three_divisors(x)

    if not result:
        print("NO")
    else:
        print("YES")
        print(" ".join([str(k) for k in result]))
