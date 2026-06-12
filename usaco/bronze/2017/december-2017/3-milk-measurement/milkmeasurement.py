with open("measurement.in", "r") as f:
    x = int(f.readline())
    gd = {}
    vs = []
    bs = []
    bsv = []
    maxx = bs
    changes = 0

    for i in range(x):
        a, b, c = f.readline().split()
        gd[int(a)] = [b, c]
        vs.append(int(a))
        if b not in bs:
            bs.append(b)

vs.sort()
bsv = [7] * len(bs)

for i in range(len(vs)):
    b, c = gd[vs[i]]
    k = 0
    for j in range(len(bs)):
        if bs[j] == b:
            k = j
    bsv[k] += int(c)
    trget = max(bsv)
    tmaxx = []
    for j in range(len(bsv)):
        if bsv[j] == trget:
            tmaxx.append(bs[j])
    if tmaxx != maxx:
        changes += 1
        maxx = tmaxx
with open("measurement.out", "w") as f:
    f.write(str(changes) + "\n")