import re

from numpy.core.defchararray import isalnum

fields = "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"
fieldsNoCID = "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"


def countValidPassports():
    ctrCods = 0
    ctrValid = 0
    fl = open("input").read()

    fieldsLidos = re.findall(r"\S+|\n", fl)

    string = ""
    for i in range(0, len(fieldsLidos) - 1):
        if fieldsLidos[i] == "\n":
            if fieldsLidos[i + 1] == "\n":
                if ctrCods >= 7:  # its valid!
                    ctrValid += 1
                    # print(str(ctrValid))
                ctrCods = 0
                # print()
        else:
            # print(fieldsLidos[i])
            cod = fieldsLidos[i].split(":")[0]
            value = fieldsLidos[i].split(":")[1]

            if checkCodVal(cod, value):
                ctrCods += 1
                # print("!!")

            string += fieldsLidos[i]
    print(str(ctrValid))


def checkCodVal(cod, val):
    if cod == "byr":
        return 1920 <= int(val) <= 2002

    if cod == "iyr":
        return 2010 <= int(val) <= 2020

    if cod == "eyr":
        return 2020 <= int(val) <= 2030

    if cod == "hgt":
        return checkHgt(val)

    if cod == "hcl":
        return "#" in str(val) and isalnum(val[-6:])

    if cod == "ecl":
        return checkEcl(val)

    if cod == "pid":
        return checkPid(val)

    if cod == "cid":
        return False  # we dont check cid so it doesn't count as a field

    return False  # it's not a valid code


def checkByr(val):
    return 1920 <= int(float(val)) <= 2002


def checkIyr(val):
    return 2010 <= int(val) <= 2020


def checkEyr(val):
    return 2020 <= int(val) <= 2030


def checkHcl(val):
    return 2020 <= int(val) <= 2030


def checkHgt(val):
    return "#" in str(val) and isalnum(val[-6:])


def checkHgt(val):
    if "cm" in str(val):
        return 150 <= int(val.replace("cm", "")) <= 193

    if "in" in str(val):
        return 59 <= int(val.replace("in", "")) <= 76

    return False  # val doesnt have cm or in


def checkEcl(val):
    eyeColours = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    for colour in eyeColours:
        if colour in str(val):
            return True
    return False  # the eye colour isnt in the database


def checkPid(val):
    if len(val) == 10:
        return False  # length must be 9

    for n in str(val):
        if not n.isdigit():
            return False

    return True  # pid only contains numbers


# ex 1
def countPassportsWithFields():
    counter = 0

    fl = open("input").read().splitlines()

    string = ""
    for line in fl:
        if line != "":
            string += line  # add values if it's not a new line
        else:  # when its a new line check passport
            if checkPassport(string):
                counter += 1
            string = ""

    if checkPassport(
        string
    ):  # check last password, since there isn't a new line at the end of the file
        counter += 1

    print(counter)


def checkPassport(passport):
    for field in fieldsNoCID:

        field.split()

        if passport.count(field) != 1:
            return False

    return True
