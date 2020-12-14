from collections import Counter


# WARNING: file MUST have 2 empty lines at the end

def customsMinimumOneVote():
    fl = open("input", "r").readlines()

    answered = 0
    answer = ""

    for line in fl:
        if line == "\n" or line == '':
            res = Counter(answer)  # get frequency of characters in our string
            # transform freq into list of all unique characters in the answer
            res = list(res)
            answered += len(res)
            answer = ""
        answer += line[:-1]  # -1 removes the \n

    print("Total answers: " + str(answered))


def customsAllVoted():
    fl = open("input", "r").readlines()

    ctrPpl = 0
    answered = 0
    answer = ""

    for line in fl:
        if line == "\n" or line == '':  # new line
            charsFrequencyList = list(answer)  # create a list from the answer string
            charsFrequency = dict()  # create dictionary

            for char in charsFrequencyList:  # populate dictionary from list
                if char in charsFrequency.keys():
                    charsFrequency[char] += 1  # increment value if it already exists
                else:
                    charsFrequency[char] = 1  # create value

            for key in charsFrequency:  # check dictionary for answers that don't count
                value = charsFrequency[key]
                if value != ctrPpl:  # if the letter's frequency is different from the number of people in the group
                    charsFrequency[key] = 0

            for key in charsFrequency:  # remove said answers
                value = charsFrequency[key]
                if value != 0:  # if the key has a value different from 0, increment the total answers by 1
                    # print(key, value)
                    answered += 1

            ctrPpl = -1  # account for new line
            answer = ""  # reset answer string

        answer += line[:-1]  # -1 removes the \n
        ctrPpl += 1  # add a person
    print("Total answers: " + str(answered))
