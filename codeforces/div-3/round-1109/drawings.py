x = int(input())

for i in range(x):
    y = int(input())
    z = list(input())
    maxx = 0
    curr = 0
    for j in range(len(z)):
        if z[j] == '#':
            curr += 1
        else: curr = 0
        maxx = max(curr, maxx)
    if maxx%2 == 0:
        print(maxx//2)
    else: print(maxx//2 + 1)
