def read_file(filename="test"):

    matrix = []
    with open(filename) as fp:
        for line in fp.readlines():
            matrix.append([int(x) for x in line.strip("\n")])

    return matrix


def is_out_of_bounds(matrix, x, y):

    if x < 0 or y < 0:
        return 1

    if x >= len(matrix[0]) or y >= len(matrix):
        return 1

    return 0

COORD_MAP = {
    "n": (-1, 0),
    "s": (1, 0),
    "e": (0, 1),
    "w": (0, -1),
}

ctr = 0
def find_trail_pt1(matrix, r_start, c_start, seen = []):
    global ctr

    seen.append((r_start, c_start))

    if matrix[r_start][c_start] == 9:
        ctr += 1
        return

    r_next, c_next = r_start, c_start

    for r, c in COORD_MAP.values():
        r_next, c_next = r_start + r, c_start + c

        if (r_next, c_next) in seen: continue
        if is_out_of_bounds(matrix, r_next, c_next): continue

        if (matrix[r_start][c_start] + 1) == matrix[r_next][c_next]:
            find_trail_pt1(matrix, r_next, c_next, seen)

    return 0

trails = []
def find_trail_pt2(matrix, r_start, c_start, trail):
    global trails

    if matrix[r_start][c_start] == 9:
        trails.append(trail)
        return

    r_next, c_next = r_start, c_start

    for r, c in COORD_MAP.values():
        r_next, c_next = r_start + r, c_start + c

        if (r_next, c_next) in trail: continue
        if is_out_of_bounds(matrix, r_next, c_next): continue

        if (matrix[r_start][c_start] + 1) == matrix[r_next][c_next]:
            trail.append((r_next, c_next))

            find_trail_pt2(matrix, r_next, c_next, trail)

            trail.pop()


matrix = read_file("prod")

def part_1(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):

            node = matrix[r][c]

            if node == 0:
                find_trail_pt1(matrix, r, c, [])

    print(f"part 1: {ctr}")


def part_2(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):

            node = matrix[r][c]

            if node == 0:
                find_trail_pt2(matrix, r, c, [(r,c)])

    print(f"part 2: {len(trails)}")

part_1(matrix)
part_2(matrix)