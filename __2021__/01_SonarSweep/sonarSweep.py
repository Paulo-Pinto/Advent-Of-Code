def part_one():
    f = open('input_1')

    prev, ctr = 0, 0

    for line in f:
        curr = int(line)

        if prev == 0:
            prev = curr

        # increased
        if curr > prev:
            ctr += 1

        prev = curr

    print(ctr)


def part_two():
    with open('input_1') as f:
        data = [int(line.rstrip('\n')) for line in f]

    ctr = 0

    # the sliding window cancels the 2 elements in between,
    # so we just need to compare the first element of a letter
    # with the element that comes after the last element of said letter

    for i in range(len(data) - 3):
        if data[i + 3] - data[i] > 0:
            ctr += 1
    print(ctr)


part_one()
part_two()
