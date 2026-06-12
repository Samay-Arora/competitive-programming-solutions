with open('whereami.in', 'r') as f:
    N = int(f.readline())
    mail = list(f.readline().strip())

final = 0
for i in range(1, N):
    lists = []
    sets = set()
    for j in range(N):
        window = mail[j:j+i]
        lists.append(window)
        sets.add(tuple(window))
    if len(lists) == len(sets):
        final = i
        break


with open('whereami.out', 'w') as f:
    f.write(f"{final}")

