def read_file():
    with open('input_2') as f:
        return [line.rstrip("\n").split(" ") for line in f]


def part_one(data_dive):
    depth, length = 0, 0

    for move in data_dive:
        if move[0] == "forward":
            length += int(move[1])
        if move[0] == "up":
            depth -= int(move[1])
        if move[0] == "down":
            depth += int(move[1])

    print(depth, length, depth * length)


def part_two(data_dive):
    depth, length, aim = 0, 0, 0

    for move in data_dive:
        if move[0] == "forward":
            length += int(move[1])
            depth += aim * int(move[1])
        if move[0] == "up":
            aim -= int(move[1])
        if move[0] == "down":
            aim += int(move[1])

    print(depth, length, depth * length)


data = read_file()
part_one(data)
part_two(data)
