from functools import lru_cache

@lru_cache(maxsize=None)
def get_ways(a: int, b: int) -> int:
    if a == b:
        return 1
    if a > b:
        return 0
    return get_ways(a + 1, b) + get_ways(a + 2, b) + get_ways(a + 3, b)

(a, b) = [int(k) for k in input().split()]

print(get_ways(a, b))
