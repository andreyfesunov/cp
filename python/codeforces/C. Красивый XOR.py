from abc import ABC
from dataclasses import dataclass

class Result(ABC):
    pass

@dataclass
class SuccessResult(Result):
    parts: list[int]

    def __str__(self) -> str:
        l = len(self.parts)

        if l == 0:
            return "0"

        return f"{l}\n{" ".join([str(k) for k in self.parts])}"

class FailureResult(Result):
    def __str__(self) -> str:
        return "-1"

def solve(a: int, b: int) -> Result:
    if a == b:
        return SuccessResult([])

    bbin = bin(b)[2:]
    abin = bin(a)[2:]

    len_bbin = len(bbin)
    len_abin = len(abin)

    if len_bbin > len_abin:
        return FailureResult()

    if len_bbin == len_abin:
        return SuccessResult([b ^ a])

    k = 2 ** len_abin - 1

    return SuccessResult([a ^ k, a ^ (a ^ k) ^ b])

attempts = int(input())

for _ in range(attempts):
    (a, b) = [int(k) for k in input().split()]
    print(solve(a, b))
