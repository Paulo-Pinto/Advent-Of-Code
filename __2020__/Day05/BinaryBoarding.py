availableSeats = list(range(85, 884))  # 1023 = 127 * 8 + 7 (max ID)
occupiedSeats = list()  # used to calculate the biggest seatId


def findSeat():
    fl = open("seats.txt", "r").read().split()

    for line in fl: #skim every line for seats
        countSeat(line) # analyse the seat

    print("Biggest Value is " + str(max(occupiedSeats)))
    print("Our seat is " + str(availableSeats[0]))


def countSeat(binaryCode):
    rowCharsQuant = 7  # ammount of chars determining the row
    row = 0
    for i in range(0, rowCharsQuant):  # get rows
        if binaryCode[i] == "B":  # add half of 2^i
            row += pow(2, rowCharsQuant - 1 - i)  # 64 + 32 +...+ 1, max 127

    colCharsQuant = 3  # ammount of chars determining the col
    col = 0
    for j in range(0, colCharsQuant):
        if binaryCode[j + rowCharsQuant] == "R":
            col += pow(2, colCharsQuant - 1 - j)  # 4 + 2 + 1, max 7

    seatId = (row * 8) + col
    # print(binaryCode, seatId)
    occupiedSeats.append(seatId)  # add new occupiedSeat
    availableSeats.remove(seatId)  # remove occupiedSeat from availableSeats
