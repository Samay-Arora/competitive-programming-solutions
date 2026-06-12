with open("square.in", "r") as file:
    lines = file.readlines()
    cords = []

    for line in lines:
        x1, y1, x2, y2 = map(int, line.strip().split())
        cords.append([x1, y1, x2, y2])

topx1 = 0
topy1 = 0
topx2 = 0
topy2 = 0

if cords[0][0] < cords[1][0]:
    topx1 = cords[0][0]
else:
    topx1 = cords[1][0]

if cords[0][1] < cords[1][1]:
    topy1 = cords[0][1]
else:
    topy1 = cords[1][1]

if cords[0][2] > cords[1][2]:
    topx2 = cords[0][2]
else:
    topx2 = cords[1][2]

if cords[0][3] > cords[1][3]:
    topy2 = cords[0][3]
else:
    topy2 = cords[1][3]


if abs(int(topx1) - int(topx2)) > abs(int(topy1) - int(topy2)):
    area = abs(int(topx1) - int(topx2)) ** 2
else:
    area = abs(int(topy1) - int(topy2)) ** 2

with open("square.out", "w") as file:
    file.write(str(area))