n = int(input())
# works but is too slow
for k in range(1, n):
    total = 0
    for i in range(n, 0, -1):
        total += i + max(1, i - k)
    print(total - 2)