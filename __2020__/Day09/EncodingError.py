from itertools import combinations
import time

import __2020__.functions.funs as funs


def part1(preamble):
    with open("input") as fp:
        res = list(map(int, (x.strip() for x in fp.readlines())))

    for i in range(0, len(res) - preamble + 1):
        found = 0
        resUsable = res[0:preamble]  # first <preamble> elements of res list

        for numbers in combinations(
            resUsable, 2
        ):  # iterate every combination of 2 elements from resUsable
            if (
                sum(numbers) == res[preamble]
            ):  # check the sum of our combination against the number we need
                found = 1  # we've found a sum
                res = res[1:]  # go forward one index
                break
            else:
                found = 0

        if found == 0:  # we didn't find a sum for our culprit
            return str(res[preamble]) + " is invalid"


def part2(preamble):
    with open("input") as fp:
        res = list(map(int, (x.strip() for x in fp.readlines())))

    backupRes = res
    numberToFind = 0
    found = 0

    for i in range(0, len(res) - preamble + 1):
        found = 0
        resUsable = res[0:preamble]  # first <preamble> elements of res list

        for numbers in combinations(
            resUsable, 2
        ):  # iterate every combination of 2 elements from resUsable
            if (
                sum(numbers) == res[preamble]
            ):  # check the sum of our combination against the number we need
                found = 1  # we've found a sum
                res = res[1:]  # go forward one index
                break
            else:
                found = 0

        if found == 0:  # we didn't find a sum for our culprit
            numberToFind = res[preamble]
            break

    index = backupRes.index(numberToFind)
    found = 0
    numberList = (
        list()
    )  # list where we will keep our numbers that add up to the number we want to find
    e = index
    soma = 0

    while 1:
        e -= 1
        if found == 1:  # ladies and gents, we found (= 1) our number
            # print(soma, numberList, i)
            print(max(numberList) + min(numberList))
            break

        numberList = list()
        i = e
        soma = 0

        while 1:
            i -= 1  # get last number

            if i == 0:  # no indexes left
                break

            soma += backupRes[i]
            numberList.append(backupRes[i])

            if soma == numberToFind:  # ladies and gents, we found (= 1) our number
                found = 1
                break

            if soma > numberToFind:  # sum is bigger than our number
                soma = 0
                break


# not pretty :(


funs.executionTime(1, part1, 25)
funs.executionTime(2, part2, 25)

print(funs.fileToList("input", ""))
