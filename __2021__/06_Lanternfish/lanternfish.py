import numpy as np


def read_lanternfish():
    with open("input_6") as f:
        return [line.split(",") for line in f][0]


# brute force, doesnt work on 256
def simulate_lanternfish(state, days):
    state_length = len(state)

    # print(80-days,initial_state_length)

    # base case
    if days == 0:
        return state_length

    for i in range(state_length):
        if state[i] == 0:
            state.append(8)
            state[i] = 7

        state[i] = int(state[i]) - 1

    return simulate_lanternfish(state, days - 1)


def part_two():
    counter = np.unique(read_lanternfish(), return_counts=True)

    fishes = np.zeros(10)

    # set
    for i in range(len(counter[1])):
        fishes[i + 1] += counter[1][i]

    print(fishes)

    for i in range(256):
        fishes[9] = fishes[0]
        fishes[7] += fishes[0]
        fishes = np.roll(fishes, -1)

    total = 0
    for i in range(len(fishes) - 1):
        total += fishes[i]
    return round(total)


initial_state = read_lanternfish()
print(simulate_lanternfish(initial_state, 80))
print(part_two())
