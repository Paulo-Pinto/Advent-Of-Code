def read_file():
    with open('input_10') as f:
        return list([line.strip("\n") for line in f])


closers = {
    ")": "(",
    "]": "[",
    "}": "{",
    ">": "<"
}

closers_points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}

# openers is closers reversed
openers = {}

for k, v in closers.items():
    openers[v] = k

openers_points = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}

def part_1():
    total = 0
    for row in read_file():

        last_open = []  # track last openers
        for e in row:  # is it an closer?

            if e in [")", "]", "}", ">"]:
                if closers[e] == last_open[len(last_open) - 1]:  # check if closer matches last opener
                    last_open = last_open[:-1]  # remove last opener
                else:  # add points and go to next row
                    # print(f"{ctr} : expected {openers[last_open[len(last_open) - 1]]}, but found {e} instead\n")
                    total += closers_points[e]
                    break
            else:
                last_open.append(e)  # add opener to end of list

    return total


def part_2():
    scores = []  # track all scores

    for row in read_file():

        last_open = []  # track last openers
        for index, e in enumerate(row):

            if e in [")", "]", "}", ">"]:  # is it a closer?
                if closers[e] == last_open[len(last_open) - 1]:  # check if closer matches last opener
                    last_open = last_open[:-1]  # remove last opener
                else:
                    break  # corrupted, go to next row

            else:
                last_open.append(e)  # add opener to end of list

            if index == len(row) - 1:  # on last index, calc score
                score = 0
                for opener in reversed(last_open):
                    score *= 5
                    score += openers_points[opener]
                scores.append(score)

    scores = sorted(scores)
    return scores[round((len(scores) + 1) / 2) - 1]  # alternatively statistics.median(len(scores))


print(part_1())
print(part_2())
