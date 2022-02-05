import numpy as np

with open('input_5') as f:
    data_hydro = [(line.rstrip("\n").split(" -> ")) for line in f]


def hydro(data_hydro, part="one"):
    line_map = np.zeros((1000, 1000))

    for x in data_hydro:

        x1, y1 = x[0].split(",")
        x2, y2 = x[1].split(",")

        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

        if part == "two":
            # part two
            if x1 != x2:
                if y1 != y2:
                    # diagonal
                    for i in range(max(x1, x2) - min(x1, x2) + 1):

                        # theres must be a way to simplify this

                        if x1 < x2:
                            x = x1 + i
                        else:
                            x = x1 - i

                        if y1 < y2:
                            y = y1 + i
                        else:
                            y = y1 - i

                        line_map[x, y] += 1;

        # vertical, y moves
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                line_map[x1, i] += 1;

        # horizontal, x moves
        if y1 == y2:
            for i in range(min(x1, x2), max(x1, x2) + 1):
                line_map[i, y1] += 1;

    counter = np.unique(line_map, return_counts=True)

    # add up all occurences of numbers >= 2
    return sum(counter[1][2:])


print(hydro(data_hydro, part="one"))
print(hydro(data_hydro, part="two"))
