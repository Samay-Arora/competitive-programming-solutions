with open('cowsignal.in', 'r') as f:
    lines = f.readlines()
    r1 = list(map(int, lines[0].strip().split()))

final = []
for i in range(r1[0]):
    curr = [c * r1[2] for c in lines[i+1].strip()]
    for i in range(r1[2]):
        final.append(curr)

with open('cowsignal.out', 'w') as f:
    for i in range(len(final)):
        f.write("".join(final[i]) + "\n")

