def read_file(filename="test"):

    with open(filename) as fp:
        return [int(x) for x in fp.readline().strip("\n")]


def gen_layout(disk_map):

    layout = []
    ctr = 0

    for idx, d in enumerate(disk_map):

        if idx % 2 == 0:
            for _ in range(d):
                layout.append(str(ctr))
            ctr += 1
        else:
            for _ in range(d):
                layout.append(".")

    return layout


def gen_new_layout(layout):
    new_layout = []
    last = len(layout) - 1
    for idx in range(len(layout)):
        # print(layout, new_layout, idx, last)

        l = layout[idx]

        if idx == last + 1 or idx == last:
            new_layout.append(layout[last])
            break

        if l == ".":

            while layout[last] == ".":
                last -= 1

            new_layout.append(layout[last])

            last -= 1
        else:
            new_layout.append(layout[idx])

    return new_layout


# part 1 ~ 1:30 took a long time to realize IDs can be multidigit ... thanks for the hint reddit
def part_1(disk_map):
    layout = gen_layout(disk_map)
    new_layout = gen_new_layout(layout)

    # print(disk_map)
    # print(layout)
    # print(new_layout)

    sum = 0
    for idx, x in enumerate(new_layout):
        sum += idx * int(x)
    return sum


def gen_ranges(layout):

    ranges = []

    curr = layout[0]
    ctr = 0

    for idx in range(1, len(layout)):
        ctr += 1
        next = layout[idx]

        if curr != next:
            # print(curr, next)
            ranges.append((ctr, curr))
            ctr = 0
            curr = next
    else:
        ranges.append((ctr + 1, next))

    return ranges


def gen_new_layout_2(ranges):
    new_layout = []

    while len(ranges) > 0:

        curr_l, curr_d = ranges.pop(0)

        if curr_d != ".":
            for _ in range(curr_l):
                new_layout.append(curr_d)
        else:
            next_l = 0
            while curr_l - next_l > 0:

                for next_l, next_d in ranges[::-1]:

                    if next_d == ".":
                        continue

                    if next_l <= curr_l:
                        # print(f"Matched {next_l * next_d}")
                        for _ in range(next_l):
                            new_layout.append(next_d)

                        curr_l -= next_l

                        ranges[ranges.index((next_l, next_d))] = (next_l, ".")

                else:
                    # print("No match")
                    for _ in range(curr_l):
                        new_layout.append(curr_d)

                    curr_l = 0

    return new_layout


# part 2 ~ 30m -> tough but ranges and queues realllly helped
def part_2(disk_map):
    layout = gen_layout(disk_map)
    ranges = gen_ranges(layout)
    new_layout = gen_new_layout_2(ranges)

    # print(disk_map)
    # print(layout)
    # print(*new_layout)

    sum = 0
    for idx, x in enumerate(new_layout):
        if x != ".":
            sum += idx * int(x)

    return sum


disk_map = read_file("prod")

print(part_1(disk_map))
print(part_2(disk_map))
