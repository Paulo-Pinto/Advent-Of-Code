def readFile():
    fl = open("ConsoleInstructions.txt", "r").readlines()  # open file

    commands = dict(list())  # dictionary of lists, the list will contain commands
    i = 1

    for line in fl:
        command = list()
        lineValues = line.split(" ")

        command.append(lineValues[0])  # add command to list
        command.append(lineValues[1])  # add value
        command.append(0)  # the command hasnt been executed

        commands[i] = command  # add to dictionary
        i += 1

    return commands


def part1():
    return "The accumulated value is " + str(runCommands(readFile())[0])


def part2():
    commands = readFile()

    for command in commands.values():  # check different changes in the boot

        if command[0] == "jmp":  # switch the command
            command[0] = "nop"
            result = runCommands(commands)
            if result[2] == 1:  # the console finished booting up
                return "Change jmp to nop in position " + str(command[2]) + \
                       " to boot the console correctly and get the accumulated value of " + str(result[0])

            command[0] = "jmp"  # revert the switch for a clean slate

        if command[0] == "nop":  # switch the command
            command[0] = "jmp"
            result = runCommands(commands)
            if result[2] == 1:  # the console finished booting up
                return "Change nop to jmp in position " + str(command[2]) + \
                       " to boot the console correctly and get the accumulated value of " + str(result[0])

            command[0] = "nop"  # revert the switch for a clean slate

    return "There isn't a change to be made"


def runCommands(commandsCopy):
    pos = 1  # position being analysed in the dictionary
    ctr = 0
    end = 0  # track if the end has been reached
    while 1:

        if pos not in commandsCopy:  # position is outside the boot code, hence it has finished
            # print("The game console has booted up correctly")
            end = 1
            break

        command = commandsCopy[pos]
        # print(command, pos, ctr)

        if command[2] == 1:  # if it's 1 the command has already been executed
            break

        if command[0] == "acc":
            ctr += int(command[1])  # increment accumulated value

        if command[0] == "jmp":
            pos += int(command[1])  # increment position
        else:  # if its "nop" or "acc"
            pos += 1

        command[2] = 1

    for command in commandsCopy.values():  # reset the commands
        command[2] = 0

    return ctr, pos, end