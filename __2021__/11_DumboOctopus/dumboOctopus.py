def read_file():
    with open("input_11") as f:
        return [list(map(int, x.strip("\n"))) for x in f.readlines()]


def print_board(b):
    for row in b:
        print(row)


# globals
octopi = read_file()
flash_ctr = 0
flashed = []


# check if all octopi are flashing
def check_simultaneous_flash():
    global octopi

    # rows
    for r in octopi:
        if len(set(r)) != 1:  # if the length of the set is 1, all the numbers are the same (set has no duplicates)
            return False

    # cols
    for c in range(len(octopi)):
        seen = [octopi[0][c]]  # store the first value in column
        for r in range(len(octopi)):
            if octopi[r][c] not in seen:  # it must be always the same value
                return False

    return True


def part_1():
    global octopi, flashed, flash_ctr
    octopi = read_file()

    step = 0
    while step <= 300:
        flashed = []
        if step == 100:
            return f"step {step} flashes {flash_ctr} times"

        for row in range(len(octopi)):
            for col in range(len(octopi)):
                increase(row, col)

        step += 1


def part_2():
    global octopi, flashed
    octopi = read_file()

    step = 0
    while True:
        flashed = []
        if check_simultaneous_flash():
            return f"step {step} is the first one to flash simultaneously"

        for row in range(len(octopi)):
            for col in range(len(octopi)):
                increase(row, col)

        step += 1

        # safe space
        if step == 999:
            return


# increase octopus value by one and flashes if conditions met
def increase(row, col):
    global octopi, flashed

    # if octopus has flashed in this step, it can't act again
    if (row, col) not in flashed:
        octopi[row][col] += 1
        if octopi[row][col] > 9:
            flash(row, col)


# check cells around
def flash(row, col):
    global octopi, flash_ctr, flashed
    flash_ctr += 1
    flashed.append((row, col))
    octopi[row][col] = 0

    # top - left
    if row >= 1 and col >= 1:
        increase(row - 1, col - 1)

    # top
    if row >= 1:
        increase(row - 1, col)

    # top - right
    if row >= 1 and col < (len(octopi) - 1):
        increase(row - 1, col + 1)

    # left
    if col >= 1:
        increase(row, col - 1)

    # right
    if col < (len(octopi) - 1):
        increase(row, col + 1)

    # bot - left
    if row < (len(octopi) - 1) and col >= 1:
        increase(row + 1, col - 1)

    # bot
    if row < (len(octopi) - 1):
        increase(row + 1, col)

    # top - right
    if row < (len(octopi) - 1) and col < (len(octopi) - 1):
        increase(row + 1, col + 1)


print(part_1())
print(part_2())

# this took me around 50 minutes, I'm getting faster at this :) aiming for 10m/part
