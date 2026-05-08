num_cows = int(input())
max_pay = (list(map(int, input().strip().split())))
max_pay.sort()
min_pay = 10**9
curr_sum = 0
max_sum = 0
num_pay = 0

for i in range(len(max_pay)):
    curr_sum = max_pay[i] * (num_cows - i)
    if curr_sum > max_sum:
        max_sum = curr_sum
        min_pay = max_pay[i]


print(max_sum, min_pay)