import time


def executionTime(part, func, *args):
    start_time = time.time()
    print(func(*args))
    execTime = (time.time() - start_time) * 1000
    print("Part " + str(part) + ": %.5s ms\n" % execTime)


def fileToList(fileName, *divider):
    res = [line.strip().split().split(*divider) for line in open(fileName, "r").readLines()]


def readToIntMatrix(filename):
    with open(filename) as f:
        return [list(map(int, x.strip("\n"))) for x in f.readlines()]


def checkSurroundingCells(data, row, col, f):
    # top - left
    if row >= 1 and col >= 1:
        f(row - 1, col - 1)

    # top
    if row >= 1:
        f(row - 1, col)

    # top - right
    if row >= 1 and col < (len(data) - 1):
        f(row - 1, col + 1)

    # left
    if col >= 1:
        f(row, col - 1)

    # right
    if col < (len(data) - 1):
        f(row, col + 1)

    # bot - left
    if row < (len(data) - 1) and col >= 1:
        f(row + 1, col - 1)

    # bot
    if row < (len(data) - 1):
        f(row + 1, col)

    # top - right
    if row < (len(data) - 1) and col < (len(data) - 1):
        f(row + 1, col + 1)
