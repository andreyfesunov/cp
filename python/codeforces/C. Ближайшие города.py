from itertools import accumulate

def read_list() -> list[int]:
    return [int(k) for k in input().split()] 

def read_int() -> int:
    return int(input())

for _ in range(read_int()):
    n = read_int()
    diff = read_list()

    cost_up = [0] * (n)
    cost_down = [0] * (n)

    for index in range(1, n):
        if index == 1:
            cost_up[index] = 1
        else:
            cost_up[index] = 1 if diff[index] - diff[index - 1] < diff[index - 1] - diff[index - 2] else diff[index] - diff[index - 1]

    for index in range(n - 2, -1, -1):
        if index == n - 2:
            cost_down[index + 1] = 1
        else:
            cost_down[index + 1] = 1 if diff[index + 1] - diff[index] < diff[index + 2] - diff[index + 1] else diff[index + 1] - diff[index]

    prefix_up = list(accumulate(cost_up))
    prefix_down = list(accumulate(cost_down))

    for _ in range(read_int()):
        (x, y) = read_list()

        if x > y:
            print(prefix_down[x - 1] - prefix_down[y - 1])
        else:
            print(prefix_up[y - 1] - prefix_up[x - 1])

