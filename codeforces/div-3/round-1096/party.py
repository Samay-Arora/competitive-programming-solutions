from collections import Counter

x = int(input())

for i in range(x):
    t = int(input())
    count = Counter(input())
    if count['('] == count[')']:
        print('YES')
    else:
        print('NO')kf
        