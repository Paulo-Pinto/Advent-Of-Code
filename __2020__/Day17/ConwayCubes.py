class Point:
    def __init__(self, px, py, pz, val):
        self.px = px
        self.py = py
        self.pz = pz
        if val == "#":
            self.val = 1
        elif val == ".":
            self.val = 0
        else:
            print("val is incorrect!")

    def __str__(self):
        return chave(self.val)

    def __full__(self):
        return (
            "["
            + chave(self.px)
            + " , "
            + chave(self.py)
            + " , "
            + chave(self.pz)
            + "] "
            + chave(self.val)
        )


bags = dict()  # global dictionary that keeps the bags that can contain other bags

length = 3
with open("input") as fp:
    res = list(char for char in fp.read().strip("\n"))
    print(res)

points = dict()

x = 0
y = -1
z = -1
i = 0
for point in res:
    x += 1

    # print(point)
    if i % length == 0:  # this is y++
        y += 1
        x = 0
        # print("y++")

    if i % (length * length) == 0:  # this is z++
        z += 1
        y = 0
        x = 0
        # print("z++")

    chave = str(x) + str(y) + str(z)
    points[chave] = Point(x, y, z, point)

    i += 1

sizeZ = (length * 2) + 1

for p in points:
    value = points[p]
    print(p, value.val)
