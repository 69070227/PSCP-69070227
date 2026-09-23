"""[LEARNING LOGS] Arcade of Time: Store Check"""

num, check = map(int, input().split())

time = [0] * 1441
current = 0

for i in range(num):
    start, stop = map(int, input().split())

    time[start] += 1
    time[stop] -= 1


for i in range(1441):
    current += time[i]
    time[i] = current

check_time = list(map(int, input().split()))
for i in range(check):
    print(time[check_time[i]], end=" ")
