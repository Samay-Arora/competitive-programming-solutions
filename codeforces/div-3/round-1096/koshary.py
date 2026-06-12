n = int(input())

for i in range(n):
    l = []
    l = input().strip().split()
    l[0], l[1] = int(l[0])%2, int(l[1])%2
    if l[0]+l[1] <= 1:
        print("YES\n")
    else:
        print("NO\n")