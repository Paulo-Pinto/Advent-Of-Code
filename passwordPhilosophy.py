def checkPasswordPolicy():
    counter = 0  # initialize counter

    fl = open("files/passwords.txt", "r").readlines()  # open file

    for line in fl:
        split = line.split()  # split the values form the text

        # get min and max values
        minimum = int(split[0].split("-")[0])
        maximum = int(split[0].split("-")[1])

        letter = split[1].split(":")[0]  # get the letter to searc for in password

        password = split[2]  # get password

        occurrences = password.count(letter)  # get number of times a letter is used in the password

        if minimum <= occurrences <= maximum:  # check if the occurences are within the stated values
            counter += 1  # increment counter

        # print(minimum, maximum, letter, password)

    print(counter)


def checkPasswordPolicyPosition():
    counter = 0  # initialize counter

    fl = open("files/passwords.txt", "r").readlines()  # open file

    for line in fl:
        split = line.split()  # split the values form the text

        # get first and second legal character spaces ( +1 because index zero is a lie)
        first = int(split[0].split("-")[0])-1
        second = int(split[0].split("-")[1])-1

        letter = split[1].split(":")[0]  # get the letter to search for in password

        firstLetter = split[2][first]  # get password
        secondLetter = split[2][second]  # get password

        if (firstLetter == letter) ^ (secondLetter == letter):  # check if the occurences are within the stated values
            counter += 1  # increment counter
            print(split)
        # print(minimum, maximum, letter, password)

    print(counter)
