with open('breedflip.in', 'r') as f:
    l = int(f.readline())
    a = f.readline()
    b = f.readline()

total = 0

for i in range(1, len(a)):
    if a[i-1] != b[i-1]:
        if i != len(a)-1:
            if a[i] != b[i]:
                total += 0
            else: total += 1
        else: total += 1

with open('breedflip.out', 'w') as f:
    f.write(f"{total}")