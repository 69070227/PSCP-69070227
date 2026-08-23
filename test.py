"""esgjeg"""
n = int(input())
min_num = 9999999
max_num = -9999999
average = 0
for i in range(n):
    num = int(input())
    if num < min_num:
        min_num = num
    if num > max_num:
        max_num = num
    
    average += num

print(f"MIN: {min_num:.3f}")
print(f"MAX: {max_num:.3f}")
average = average / n

print(f"AVG: {average:.3f}")
