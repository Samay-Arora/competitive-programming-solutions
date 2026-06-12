with open("shell.in", "r") as file:
    lines = file.readlines()
    nums = 0
    shells = []
    
    for line in lines[1:]:
        s1, s2, g = line.strip().split()
        s1, s2, g = int(s1), int(s2), int(g)
        shells.append([s1 - 1, s2 - 1, g - 1])

curr = [0, 0, 0]
maxx = 0
for j in range(3):
    track = 0
    curr[j] = 1        
    for i in range(int(lines[0])):
        curr[shells[i][0]], curr[shells[i][1]] = curr[shells[i][1]], curr[shells[i][0]]
        if curr[shells[i][2]] == 1:
            track += 1
    maxx = max(maxx, track)
    curr = [0, 0, 0]

with open("shell.out", "w") as file:
    file.write(f"{maxx}")

