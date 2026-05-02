def try_to_find_lucky(required_len: int) -> int | None:
    lucky = None

    for mask in range(1 << required_len):
        seq = list(bin(mask)[2:].zfill(required_len))
        if not seq.count("0") == required_len // 2 or not seq.count("1") == required_len // 2:
            continue

        v = int("".join(["4" if k == "0" else "7" for k in seq]))
        if v >= n:
            lucky = min_none(lucky, v)

    return lucky

def min_none(a: int | None, b: int) -> int:
    if a == None:
        return b
    
    return min(a, b)

n = int(input())
l = len(str(n))
lucky: int | None = None

while lucky == None:
    lucky = try_to_find_lucky(l)
    l += 1

print(lucky)
