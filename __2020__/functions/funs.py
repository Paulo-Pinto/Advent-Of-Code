import time


def executionTime(part, func, *args):
    start_time = time.time()
    print(func(*args))
    execTime = (time.time() - start_time) * 1000
    print("Part " + str(part) + ": %.5s ms\n" % execTime)


def fileToList(fileName, *divider):
    res = [line.strip().split().split(*divider) for line in open(fileName, "r").readLines()]
