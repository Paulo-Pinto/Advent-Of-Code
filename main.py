import time

import numberSum
import passwordPhilosophy
import tobogganTrajectory
import passportProcessing
import binaryBoarding
import customCustoms
import handyHaversacks


def main():
    # numberSum.twoNumberSum()
    # numberSum.twoNumberSumOneFor()
    # numberSum.threeNumberSum()
    # passwordPhilosophy.checkPasswordPolicy()
    # passwordPhilosophy.checkPasswordPolicyPosition()
    # tobogganTrajectory.checkSlope(3,1)
    # tobogganTrajectory.checkVariousSlopes()
    # passportProcessing.countPassportsWithFields()
    # passportProcessing.countValidPassports()
    # passportProcessing.countValidPassports()
    # binaryBoarding.findSeat()
    # customCustoms.customsMinimumOneVote()

    # start_time = time.time()
    # customCustoms.customsMinimumOneVote()
    # execTime = (time.time() - start_time) * 1000
    # print("Part 1: %.5s ms\n" % execTime)
    #
    # start_time = time.time()
    # customCustoms.customsAllVoted()
    # execTime = (time.time() - start_time) * 1000
    # print("Part 2: %.5s ms\n" % execTime)

    start_time = time.time()
    handyHaversacks.countBags()
    execTime = (time.time() - start_time) * 1000
    print("Part 1: %.5s ms\n" % execTime)


    print("!")


if __name__ == "__main__":
    main()
