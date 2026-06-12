x = []
x = list(map(int, input().strip().split()))

if x[1] != 0:
    for i in range(x[1]):
        print("Heads!")
if (x[0] - x[1]) != 0:
    for i in range((x[0] - x[1])):
        print("Tails!")