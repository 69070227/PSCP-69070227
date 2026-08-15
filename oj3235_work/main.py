'''กระต่ายอ้วนตัวอ้วน'''
bunny = int(input())
count = 0
max_weight = 0
max_name = 0
for _ in range(bunny):
    name, weight = input().split()
    weight = int(weight)
    if weight > 15:
        count += 1
    if weight > max_weight:
        max_weight = weight
        max_name = name

print(count)
print(max_name)
