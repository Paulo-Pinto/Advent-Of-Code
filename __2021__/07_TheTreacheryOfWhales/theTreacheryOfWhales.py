import numpy as np


def read_crabs():
    with open('input_7') as f:
        return list(map(int, [line.split(",") for line in f][0]))


def calc_fuel(part="one"):
    fuel_costs = list()

    for potential_pos in range(0, max(crabs)):
        fuel = 0
        for crab_pos in crabs:
            # difference between current crab's position and the position they would have to move to
            diff = abs(crab_pos - potential_pos)

            if part == "one":
                fuel += diff
            else:
                fuel += sum(range(1 + diff))

        # print(i, total)
        fuel_costs.append(fuel)

    return fuel_costs


# cast to int
crabs = np.sort(read_crabs())

fuel_costs = calc_fuel(part="one")
print(min(fuel_costs), np.where(fuel_costs == np.min(fuel_costs))[0])

fuel_costs = calc_fuel(part="two")
print(min(fuel_costs), np.where(fuel_costs == np.min(fuel_costs))[0])
