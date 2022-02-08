def read_segments():
    with open('input_8') as f:
        return list([line.strip("\n").split(" | ") for line in f])


def get_correspondences():
    return {
        'a': '',
        'b': '',
        'c': '',
        'd': '',
        'e': '',
        'f': '',
        'g': ''
    }


def get_length():
    return {
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
    }


def solve_inputs():
    counter_1478 = 0
    all_solves = []
    # codes for all digits
    digits = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9',
    }

    for codes in read_segments():
        correspondences = get_correspondences()

        # store codes based on their length
        length = get_length()

        for code in codes[0].split(" "):
            length[len(code)].append(code)

        #

        # 7 - 1 get A, guess C F
        seven = [x for x in length[3][0]]
        one = [x for x in length[2][0]]
        correspondences['a'] = "".join([char for char in seven if char not in one])
        correspondences['c'] = one
        correspondences['f'] = one

        # 4 guess B D
        four = [x for x in length[4][0]]
        correspondences['b'] = [char for char in four if char not in one]
        correspondences['d'] = correspondences['b']

        # find 6 (has F OR C)
        for x in length[6]:
            # XOR, true/false -> true
            c_0 = correspondences['c'][0]
            c_1 = correspondences['c'][1]

            if c_0 in x and c_1 not in x:
                temp = c_0
                correspondences['c'] = c_1
                correspondences['f'] = temp
                break

            if c_0 not in x and c_1 in x:
                temp = c_1
                correspondences['c'] = c_0
                correspondences['f'] = temp
                break

        # find 3 (has A, C, F), solves B D and guess E G
        # print(temp_corr)
        for x in length[5]:
            if correspondences['a'] in x and correspondences['c'] in x and correspondences['f'] in x:

                two_last_elements = list(x)
                # remove known
                two_last_elements.remove(correspondences['a'])
                two_last_elements.remove(correspondences['c'])
                two_last_elements.remove(correspondences['f'])

                # two_last_ele has d, we solve b and d
                for i in range(2):
                    if two_last_elements[i] in correspondences['d']:
                        correspondences['b'].remove(two_last_elements[i])
                        correspondences['b'] = "".join(correspondences['b'])
                        correspondences['d'] = "".join(two_last_elements[i])
                        two_last_elements.remove(two_last_elements[i])
                        break

                correspondences['g'] = "".join(two_last_elements[0])

        # last one
        correspondences['e'] = "abcdefg"
        for v in correspondences.values():
            # print(v)
            if len(v) == 1:
                correspondences['e'] = correspondences['e'].replace(v, "")

        # solve last codes for this line in the file
        solves = []

        for ele in codes[1].split(" "):
            str = ""
            for key, value in correspondences.items():
                # everytime a key appears, sub it for the value in the correspondence
                str += "".join([key for x in ele if x == value])
            solves.append(str)

        temp_solves = int("".join([digits[s] for s in solves]))
        all_solves.append(temp_solves)

        for solve in solves:
            counter_1478 += 1 if digits[solve] in ["1", "4", "7", "8"] else 0
            # print(f"{solve} is {digits[solve]}")
    return counter_1478, all_solves
    # return ctr


answer = solve_inputs()

print(f"part 1 : {answer[0]}\npart 2 : {sum(answer[1])}")

