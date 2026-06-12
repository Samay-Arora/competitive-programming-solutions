p, k = int(input()) + 2, 0
while (2 ** k) < p: k += 1
print(2**k - p)