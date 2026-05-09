inp = input().strip().split()
inp = [int(x) for x in inp]

inp.sort()

a = int(inp[0])
b = int(inp[1])
c = int(inp[-1] - (a + b))

print(str(a) + " " + str(b) + " " + str(c))