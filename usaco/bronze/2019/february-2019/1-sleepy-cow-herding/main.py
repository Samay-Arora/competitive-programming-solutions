with open('herding.in', 'r') as f:
    x = list(map(int, f.readline().split()))
    x.sort()

minn = 0

if x[2] - x[1] == 1 and x[1] - x[0] == 1:
    minn = 0
else:
    if x[1] - x[2] == 2 or x[2] - x[1] == 2:
        minn = 1
    elif x[1] - x[0] == 2 or x[0] - x[1] == 2:
        minn = 1
    else:
        minn = 2


maxx = max(x[2] - x[1], x[1] - x[0]) - 1

with open('herding.out', 'w') as f:
    f.write(f"{minn}\n{maxx}")