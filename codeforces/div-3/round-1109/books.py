x = int(input())

for i in range(x):
    y = int(input())
    z = list(map(int, input().split()))
    status = True
    for i in range(len(z)-1):
        ex = 0
        ex = z[i] - (i+1)
        if ex < 0:
            status = False
        z[i+1] += ex
    if z[-1] < y:
        status = False
    if status == False:
        print("NO")
    else: print("YES")