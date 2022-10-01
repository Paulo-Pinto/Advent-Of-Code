class Bag:
    def __init__(self, colourType, colour):
        self.bagsThatAllow = set()
        self.quant = 0
        self.colourType = colourType
        self.colour = colour

    def addBagThatAllows(self, bag):
        self.bagsThatAllow.add(bag)

    def setQuant(self, quant):
        self.quant = quant

    def __str__(self):
        return self.colourType + " " + self.colour


bags = dict()  # global dictionary that keeps the bags that can contain other bags


def countBags():
    fl = open("input", "r").readlines()  # open file

    for line in fl:

        bagRead = line.split("contain")[0][:-6]  # remove "bags"
        bag = Bag(bagRead.split()[0], bagRead.split()[1])  # initialize this bag

        bagsContained = line.split("contain")[1]

        if bagsContained[1:3] != "no":  # these bags can contain bags
            for bagContained in bagsContained.split(","):
                bag.setQuant(bag.quant + int(bagContained.strip()[:1]))
                bagContained = bagContained.replace(".", "").strip()[2:]
                # remove "bags" & trailing whitespace
                if "bags" in bagContained:
                    bagContained = bagContained.replace("bags", "")[:-1]
                else:
                    bagContained = bagContained.replace("bag", "")[:-1]

                if bagContained not in bags:  # alter global dictionary
                    bags[
                        bagContained
                    ] = list()  # create list to keep the bags that this bag can contain

                # bag.setQuant(bag.quant + bagContained[-2:])
                bags[bagContained].append(bag)  # add to list

    uniqueList = set()  # create set to keep the number of bags that can contain yourBag
    yourBag = "shiny gold"
    bagsQuant = recursivaCountBags([yourBag], uniqueList)
    print(
        "Your bag can be contained in " + str(bagsQuant) + " bags"
    )  # quantity of bags that can contain yours


def recursiva(parents: list, uniqueList):
    for dad in parents:  # skim through all the bags in our parameters
        if dad in bags:  # check if our bag can contain bags
            # print(str(dad))
            for bag in bags[dad]:  # recursive case
                uniqueList.add(bag)  # add this bag to the set
                recursiva([str(bag)], uniqueList)

    # text = ""  # check uniqueList
    # for bag in uniqueList:
    #     text += str(bag) + ", "
    # print(text)

    return len(uniqueList)  # base case


def recursivaCountBags(parents: list, uniqueList):
    for dad in parents:  # skim through all the bags in our parameters
        if dad in bags:  # check if our bag can contain bags
            # print(str(dad))
            for bag in bags[dad]:  # recursive case
                uniqueList.add(bag)  # add this bag to the set
                recursivaCountBags([str(bag)], uniqueList)

    ctr = 0  # check uniqueList
    for bag in uniqueList:

        print(str(bag.quant))
        if bag in bags:
            for bagThatAllows in bags[bag]:
                ctr += bagThatAllows.quant
            ctr += bag.quant
    print(ctr)

    return len(uniqueList)  # base case
