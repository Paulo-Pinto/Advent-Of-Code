import numpy as np


# stores data as single line
def read_file(file):
    with open(file) as f:
        return [line.strip("\n") for line in f]


# stores data to 2d array (list of lists)
def read_file_2d(file):
    with open(file) as f:
        return np.array([x.replace("\n", "") for x in f.readlines()])


def calc_risk_level(data):
    risk_level_sum = 0

    # iterate rows
    for x in range(len(data)):
        # iterate cols
        for y in range(len(data[0])):
            cell = int(data[x][y])

            # check cell above
            if x - 1 >= 0:
                if int(data[x - 1][y]) <= cell:
                    continue

            # check cell below
            if x + 1 < len(data):
                if int(data[x + 1][y]) <= cell:
                    continue

            # check left cell
            if y - 1 >= 0:
                if int(data[x][y - 1]) <= cell:
                    continue

            # check right cell
            if y + 1 < len(data[0]):
                if int(data[x][y + 1]) <= cell:
                    continue

            # height + 1
            risk_level_sum += 1 + int(cell)
    return risk_level_sum


# iterates all cells, solving their basin size
def calc_basin_sizes(data):
    # store analysed cells
    seen = []
    # store size of basins
    sizes = []
    # iterate rows
    for x in range(len(data)):
        # iterate cols
        for y in range(len(data[0])):
            # if cell isnt 9 and hasn't been analysed
            if int(data[x][y]) != 9 and (x, y) not in seen:
                # print(x,y,data[x][y])
                seen.append((x, y))
                size, seen = explore_basin(data, x, y, seen, 1)
                sizes.append(size)

    # sort in ascending order
    sizes.sort()
    # switch to descending order
    sizes.reverse()
    # return first 3 (highest)
    return sizes[0:3]


# recursive, searches adjacent cells
# returns the current size of the basin (incrementally) and the analysed cells [seen]
def explore_basin(data, x, y, seen, size):
    # check cell above
    if x - 1 >= 0:
        x -= 1
        if int(data[x][y]) != 9 and (x, y) not in seen:
            # print(f"top {data[x][y]} | {(x, y)}")
            seen.append((x, y))
            size, seen = explore_basin(data, x, y, seen, size + 1)
        x += 1

    # check cell below
    if x + 1 < len(data):
        x += 1
        if int(data[x][y]) != 9 and (x, y) not in seen:
            # print(f"bot {data[x][y]} | {(x, y)}")
            seen.append((x, y))
            size, seen = explore_basin(data, x, y, seen, size + 1)
        x -= 1

    # check right cell
    if y + 1 < len(data[0]):
        y += 1
        if int(data[x][y]) != 9 and (x, y) not in seen:
            # print(f"right {data[x][y]} | {(x, y)}")
            seen.append((x, y))
            size, seen = explore_basin(data, x, y, seen, size + 1)
        y -= 1

    # check left cell
    if y - 1 >= 0:
        y -= 1
        if int(data[x][y]) != 9 and (x, y) not in seen:
            # print(f"left {data[x][y]} | {(x, y)}")
            seen.append((x, y))
            size, seen = explore_basin(data, x, y, seen, size + 1)
        y += 1

    # print(f"end {data[x][y]}")
    return size, seen


print(calc_risk_level(read_file_2d("input_9")))

result = calc_basin_sizes(read_file_2d("input_9"))
print(np.prod(result), result)

# I could probably have used a map of the low points from part 1
# to make part 2 easier but I solved part 1 first with a 1d array,
# so thought didn't come intuitively
