def checkSlope(x, y):  # x = right, y = down
    fl = open("input", "r").readlines()  # open file & read lines

    lines = (len([x.split(' ')[0] for x in fl]))  # count how many times you can split end of lines
    columns = len(fl[1]) - 1

    # print("lines: ", lines, " columns:", columns)

    # values to which we will increment x and y
    incX = x
    incY = y

    # x and y start at their increment positions, since [0][0] isn't accounted for
    x = incX
    y = incY

    i = 0  # universal counter
    counter = 0  # initialize counter
    while 1:
        i += 1

        # print("i =", i, " (", y, ") (", x, ")")
        # print(fl[y][x])
        if fl[y][x] == '#':  # if it's a tree, count it!
            # print("i =", i, " (", y, ") (", x, ")", fl[y][x])  # display the current
            counter += 1

        # x and y increment by their original values
        x += incX
        y += incY

        if x >= columns:  # if we've reached the end of the line, we must overload the extra value to the other side
            x -= columns

        if y >= lines:  # if we've reached the end of the file
            print(counter)  # show how many trees we've found
            return counter


def checkVariousSlopes():
    slope1 = checkSlope(1, 1)
    slope2 = checkSlope(3, 1)
    slope3 = checkSlope(5, 1)
    slope4 = checkSlope(7, 1)
    slope5 = checkSlope(1, 2)

    mult = slope1 * slope2 * slope3 * slope4 * slope5
    print(mult)
