with open("measurement.in", "r") as file:
    lines = file.readlines()
    prod = []
   
    for line in lines[1:]:
        day, name, change = line.strip().split()
        prod.append((int(day), name, int(change)))
    prod.sort()

    num_entries = int(lines[0])

names = [entry[1] for entry in prod]

cur_prod = {}

for name in names:
    cur_prod[name] = 7

change = [entry[2] for entry in prod]

top_changes = 0
prev_top = []
cur_top = []

for i in range(len(change)):
    cur_prod[names[i]] += change[i]
    max_val = max(cur_prod.values())
    for name in names:
        if cur_prod[name] == max_val:
            cur_top.append(name)
    if cur_top != prev_top:
        top_changes += 1
    prev_top = cur_top
    cur_top = []

with open("measurement.out", "w") as file:
    file.write(str(top_changes))