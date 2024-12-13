
# def solve(ax, ay, bx, by, px, py):

# ax, ay = 94, 34
# bx, by = 22, 67
ax, ay = 26, 66
bx, by = 67, 21

# switch if b > a
if bx + by > ax + ay:
    tmpx, tmpy = ax, ay
    ax, ay = bx, by
    bx, by = tmpx, tmpy

px , py = 12748, 12176

ai, bi = 40, 40

currx = 0
distx = px - currx

back_flag = 0

for _ in range(2000):
    ai, bi = abs(ai), abs(bi)
    currx = (ax * ai) + (bx * bi)
    distx = px - currx

    if distx < 100:
        print(_, distx, ai, bi)

    # break out
    if distx == 0:
        print(px - ((ax * ai) + (bx * bi)), py - ((ay * ai) + (by * bi))) 
        break

    # end conditions
    if currx + ax == px:
        ai += 1
        continue

    if currx + bx == px:
        bi += 1
        continue

    # backpedal
    if back_flag:
        ai -= 1
        bi -= 1
        back_flag = 0
        continue

    # both would go overboard, back pedal
    if currx + ax > px and currx + bx > px:
        back_flag = 1
        continue 

    # normal increment

    if currx + ax > px and currx + bx <= px:
        bi += 1
        continue

    if currx + ax <= px:
        ai += 1
        continue

    if currx + bx <= px:
        bi += 1
        continue