def get_facts(x: int) -> list[int]:
    facts = []

    fact = 6
    multiplier = 4

    while fact <= x:
        facts.append(fact)

        fact *= multiplier
        multiplier += 1

    return facts

def popcount(x: int) -> int:
    return bin(x).count("1")

def solve(x: int) -> int:
    facts = get_facts(x)
    facts_len = len(facts)
    result = popcount(x)

    for mask in range(1 << facts_len):
        s = 0
        cnt_mask = 0
        
        for index in range(facts_len):
            if mask & (1 << index):
                s += facts[index]
                cnt_mask += 1

        if s > x:
            continue

        result = min(result, cnt_mask + popcount(x - s))

    return result

attempts = int(input())

for _ in range(attempts):
    print(solve(int(input())))
