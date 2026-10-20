"""LineSorting"""

n = int(input())
box = []
for _ in range(n):
    box.append(input())

result = sorted(box, key = len)
for i in result:
    print(i)
