def read_file():
    with open("input_3") as f:
        return [list(line.rstrip("\n")) for line in f]


def calc_gamma_epsilon(data_b):
    gamma = list()
    epsilon = list()

    lists = list()

    for i in range(len(data_b[0])):
        lists.append(list())

    for x in data_b:
        for pos in range(len(x)):
            lists[pos].append(x[pos])

    for l in lists:
        #     print(l)
        if l.count("0") > (len(data_b) / 2):
            gamma.append("0")
            epsilon.append("1")
        else:
            gamma.append("1")
            epsilon.append("0")

    return gamma, epsilon


def calc_oxy_co2(data_binary, choice):
    data_bin_copy = data_binary.copy()
    oxygen, co2 = 0, 0

    for i in range(len(data_bin_copy[0])):

        aux = data_bin_copy.copy()
        gamma, epsilon = calc_gamma_epsilon(aux)

        # print(i,len(data_bin_copy))

        if choice == "oxygen":
            for x in aux:
                # print(x, x[i], gamma[i], not x[i] == gamma[i])
                if not x[i] == gamma[i]:
                    data_bin_copy.remove(x)

            if len(data_bin_copy) <= 2:
                oxygen = "".join(max(data_bin_copy))
                break
        else:
            for x in aux:
                # print(x, x[i], gamma[i], not x[i] == gamma[i])
                if not x[i] == epsilon[i]:
                    data_bin_copy.remove(x)

            if len(data_bin_copy) <= 2:
                co2 = "".join(min(data_bin_copy))
                break

    return oxygen if choice == "oxygen" else co2


data = read_file()
len(data)

gamma, epsilon = calc_gamma_epsilon(data)

gamma_val = int("".join(gamma), 2)
epsilon_val = int("".join(epsilon), 2)

print(gamma_val, epsilon_val, gamma_val * epsilon_val)

oxygen_int = int(calc_oxy_co2(data, "oxygen"), 2)
co2_int = int(calc_oxy_co2(data, "co2"), 2)

print(oxygen_int, co2_int, oxygen_int * co2_int)
