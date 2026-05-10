
with open("speeding.in", "r") as f:
    N, M = map(int, f.readline().split())
    road = []
    for _ in range(N):
        length, speed_limit = map(int, f.readline().split())
        road.append([length, speed_limit])
    speed = []
    for _ in range(M):
        length, bessie_speed = map(int, f.readline().split())
        speed.appenfd([length, bessie_speed])

i = 0
j = 0
maxx = 0
for k in range(100):
    if road[i][0] == 0:
        i += 1
    if speed[j][0] == 0:
        j += 1
    maxx = max(maxx, speed[j][1] - road[i][1])
    road[i][0] -= 1
    speed[j][0] -= 1

with open("speeding.out", 'w') as fl:
    fl.write(f"{maxx}")


