with open('shuffle.in', 'r') as f:
    n = int(f.readline())
    shuffle = list(map(int, f.readline().strip().split()))
    final = f.readline().strip().split()

prev = [0] * n

for _ in range(3):
    for i in range(1, n + 1):
        idx = 0
        for j in range(len(shuffle)):
            if i == shuffle[j]:
                idx = j
                prev[idx] = final[i - 1]
                break
    final = prev
    prev = [0] * n

with open('shuffle.out', 'w') as fl:
    for i in range(len(final)):
        fl.write(f"{final[i]}\n")

