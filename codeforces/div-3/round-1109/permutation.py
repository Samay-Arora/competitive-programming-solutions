from math import gcd

x = int(input())

for i in range(x):
    n, y, z = map(int, input().split())
    p = list(map(int, input().split()))
    
    g = gcd(y, z)
    status = True
    for j in range(n):
        if (p[j] - (j+1))%g != 0:
            status = False
    if status:
        print("YES")
    else:
        print("NO")