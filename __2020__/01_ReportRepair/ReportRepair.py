# import functions.funs as funs
import time


def twoNumberSum():
    # open file & read lines
    fl = open("input", "r").readlines()

    for x in fl:
        for y in fl:  # iterate all numbers by themselves
            # print(int(x) + int(y)) # check values
            if (int(x) + int(y)) == 2020:  # if sum == 2020
                # print(x, y)
                print(int(x) * int(y))
                return

def twoNumberSumOneFor():
    # open file
    f = open("input", "r")

    # file lines
    fl = f.readlines()
    for x in fl:
        # print(int(x) + int(y)) # check values
        y = 2020 - int(x)
        if y in fl:  #
            # print(x, y)
            print(int(x) * int(y))
            return


def threeNumberSum():
    # open file
    f = open("input", "r")

    # file lines
    fl = f.readlines()
    for x in fl:
        for y in fl:  # iterate all numbers by themselves
            for z in fl:  # iterate all numbers by themselves once more
                # print(int(x) + int(y)) # check values
                if (int(x) + int(y) + int(z)) == 2020:  # if sum == 2020
                    print(x, y, z)
                    print(int(x) * int(y) * int(z))
                    exit()  # exits when spotted

twoNumberSum()

# funs.executionTime(1, twoNumberSum)
# funs.executionTime(2, twoNumberSumOneFor, 25)
