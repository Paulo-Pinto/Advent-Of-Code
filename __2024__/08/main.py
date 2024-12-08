from itertools import combinations
from collections import defaultdict


def read_file(filename="test"):

    matrix = []
    with open(filename) as fp:

        for line in fp.readlines():
            matrix.append([x for x in line.strip("\n")])

    return matrix


def get_antennas():
    antennas = defaultdict(list)

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):

            node = matrix[r][c]

            if node != ".":
                antennas[node].append((r, c))
    return antennas


def is_out_of_bounds(matrix, x, y):

    if x < 0 or y < 0:
        return 1

    if x >= len(matrix[0]) or y >= len(matrix):
        return 1

    return 0


def get_freqs_part_1(matrix):
    freqs = set()
    for k, v in get_antennas().items():
        # print(k)

        for a, b in combinations(v, 2):
            # print(a, b)

            diff_r = abs(a[0] - b[0])
            diff_c = abs(a[1] - b[1])

            a_r, a_c, b_r, b_c = 0, 0, 0, 0

            # todo : there has to be a way of simplifying this

            if a[0] < b[0]:
                a_r = min(a[0], b[0]) - diff_r
                b_r = max(a[0], b[0]) + diff_r
            else:
                a_r = max(a[0], b[0]) + diff_r
                b_r = min(a[0], b[0]) - diff_r

            if a[1] < b[1]:
                a_c = min(a[1], b[1]) - diff_c
                b_c = max(a[1], b[1]) + diff_c
            else:
                a_c = max(a[1], b[1]) + diff_c
                b_c = min(a[1], b[1]) - diff_c

            if not is_out_of_bounds(matrix, a_r, a_c):
                freqs.add((a_r, a_c))

            if not is_out_of_bounds(matrix, b_r, b_c):
                freqs.add((b_r, b_c))

    return freqs


def get_freqs_part_2(matrix):
    freqs = set()
    for k, v in get_antennas().items():
        # print(k)

        for a, b in combinations(v, 2):
            # print(a, b)
            diff_r = abs(a[0] - b[0])
            diff_c = abs(a[1] - b[1])

            a_r, a_c, b_r, b_c = 0, 0, 0, 0

            for _ in range(len(matrix)):

                # todo : there has to be a way of simplifying this

                if a[0] < b[0]:
                    a_r = min(a[0], b[0]) - (diff_r * _)
                    b_r = max(a[0], b[0]) + (diff_r * _)
                else:
                    a_r = max(a[0], b[0]) + (diff_r * _)
                    b_r = min(a[0], b[0]) - (diff_r * _)

                if a[1] < b[1]:
                    a_c = min(a[1], b[1]) - (diff_c * _)
                    b_c = max(a[1], b[1]) + (diff_c * _)
                else:
                    a_c = max(a[1], b[1]) + (diff_c * _)
                    b_c = min(a[1], b[1]) - (diff_c * _)

                if not is_out_of_bounds(matrix, a_r, a_c):
                    freqs.add((a_r, a_c))

                if not is_out_of_bounds(matrix, b_r, b_c):
                    freqs.add((b_r, b_c))

                if is_out_of_bounds(matrix, a_r, a_c) and is_out_of_bounds(matrix, b_r, b_c):
                    # print("ALL OUT OF BOUNDS. STOP.")
                    break

    return freqs


def show_board(matrix, freqs):
    for freq_r, freq_c in list(freqs):
        matrix[freq_r][freq_c] = "#"

    print("\n".join(["".join([str(cell) for cell in row]) for row in matrix]))


matrix = read_file("prod")


print(len(get_freqs_part_1(matrix)))
print(len(get_freqs_part_2(matrix)))
