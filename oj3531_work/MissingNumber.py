"""MissingNumber"""
box = []
missing = []
n = int(input())
while True:
    num = int(input())
    if not num:
        break
    box.append(num)

reang = sorted(box)

for i in range(1,n+1):
    if i not in reang:
        missing.append(i)

for num in missing:
    print(num)
