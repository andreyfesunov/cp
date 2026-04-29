def is_even(n: int) -> bool:
    return n & 1 == 0

n = int(input())

print(n // 2 if is_even(n) else - (n // 2 + 1))
