def read_bingo_input():
    with open("input_4") as f:
        data_bingo = [(line.rstrip("\n").split()) for line in f]

    # clean data
    nums = data_bingo[0][0].split(",")
    boards_data = data_bingo[2:]

    ctr = 0
    temp_list = list()
    boards = list()

    for x in boards_data:

        if ctr % 6 == 5:
            # print(temp_list)
            boards.append(temp_list)
            temp_list = list()
        else:
            temp_list.append(x)

        ctr += 1

    return nums, boards


# functions
def print_board(b):
    for row in b:
        print(f"{row[0]: <4} {row[1]: <4} {row[2]: <4} {row[3]: <4} {row[4]: <4}")
    print("\n")


# calculate final result, numbers left on board * last number called
def calc_result(b, n):
    total = 0

    for row in b:
        for cell in row:
            # print(cell)
            if cell != "_":
                total += int(cell)

    print(total, n, total * n)
    return total * n


# check if provided board is complete
def check_board(b):
    # check horizontally
    for row in b:
        # 5 "_" horizontal line
        if row.count("_") == 5:
            return True

    # check vertically
    for col in range(len(b[0])):
        ctr = 0
        # col in row
        for row in b:

            if row[col] == "_":
                ctr += 1
            else:
                ctr = 0

            # 5 consecutive strikes -> its a vertical line
            if ctr == 5:
                return True

    return False


# part one
def game_flow(nums, boards_progress):
    for n in nums:
        # board
        for board in boards_progress:
            # row
            for row in board:
                # cell
                for i in range(len(row)):

                    if row[i] == n:
                        row[i] = "_"

                        if check_board(board):
                            print_board(board)
                            return calc_result(board, int(n))


# returns all incomplete boards
def get_incomplete_boards(boards):
    incomplete = list()

    for b in boards:
        if not check_board(b):
            incomplete.append(b)

    return incomplete


# part two
def game_flow2(nums, boards_progress):
    for n in nums:
        # board
        for board in boards_progress:
            # row
            for row in board:
                # cell
                for i in range(len(row)):

                    if row[i] == n:
                        row[i] = "_"

                        incompleted = get_incomplete_boards(boards_progress)

                        # if theres only one incomplete game
                        if len(incompleted) == 1:
                            return game_flow(nums, incompleted)


ns, b_progress = read_bingo_input()
print(game_flow(ns, b_progress))

ns, b_progress = read_bingo_input()
print(game_flow2(ns, b_progress))
