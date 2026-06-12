from collections import Counter

with open("blocks.in", 'r') as f:
    n = int(f.readline())
    sets = []
    for i in range(n):
        sets.append(f.readline().strip().split())

c4 = Counter({})
for i in range(n):
    w1 = sets[i][0]
    w2 = sets[i][1]
    c1 = Counter(w1)
    c2 = Counter(w2)
    c3 = Counter({})

    for ch in "abcdefghijklmnopqrstuvwxyz":
        c3[ch] = max(c1[ch], c2[ch])
    c4 += c3

with open("blocks.out", 'w') as fl:
    for ch in "abcdefghijklmnopqrstuvwxyz":
        fl.write(f"{c4[ch]}\n")