with open("mixmilk.in", "r") as file:
    lines = file.readlines()
    buckets = []
    for line in lines:
        buckets.append(list(map(int, line.strip().split())))
    print(buckets)

def mixingmilk(buckets, i, j):
    if buckets[i][1] <= (buckets[j][0] - buckets[j][1]):
        buckets[j][1] = (buckets[j][1] + buckets[i][1])
        buckets[i][1] = 0
    else:
        buckets[i][1] -= (buckets[j][0] - buckets[j][1])
        buckets[j][1] = buckets[j][0]

for num in range(1, 34):
    mixingmilk(buckets, 0, 1)
    mixingmilk(buckets, 1, 2)
    mixingmilk(buckets, 2, 0)

mixingmilk(buckets, 0, 1)

with open("mixmilk.out", "w") as file:
    file.write(str(buckets[0][1])+"\n")
    file.write(str(buckets[1][1])+"\n")
    file.write(str(buckets[2][1]))