from functools import lru_cache

for _ in range(int(input())):
    n = int(input())

    @lru_cache(maxsize=None)
    def try_reach(k: int) -> bool:
        if k == n:
            return True
        if k > n:
            return False
        return try_reach(k * 10) or try_reach(k * 20)

    print("YES" if try_reach(1) else "NO")
    
