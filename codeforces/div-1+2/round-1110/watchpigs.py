n = int(input())

for _ in range(n):
    x, y = map(int, input().split())
    z = list(input())
    s = 0
    if len(z) < 2*y:
        print('-1')
    else:
        for i in range(y):
            if z[i] != 'R':
                s += 1
        for i in range(-y, 0):
            if z[i] != 'L':
                s += 1
        print(s)