def get_tricky_sum(i: int) -> int:
    s = i * (i + 1) // 2
    pow = 1
    while pow <= i:
        s -= pow * 2
        pow *= 2
    return s

attempts = int(input())

for _ in range(attempts):
    print(get_tricky_sum(int(input())))
