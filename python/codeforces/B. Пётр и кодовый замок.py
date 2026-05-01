def can_rotate(degrees: list[int]) -> bool:
    l = len(degrees)

    for mask in range(1 << l):
        a, b = 0, 0 

        for i in range(l):
            if mask & (1 << i):
                a += degrees[i]
            else:
                b += degrees[i]

        if abs(a - b) % 360 == 0:
            return True

    return False

attempts = int(input())
degrees = [int(input()) for _ in range(attempts)]
   
print("YES" if can_rotate(degrees) else "NO")
